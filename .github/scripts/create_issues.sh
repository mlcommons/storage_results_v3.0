#!/usr/bin/env bash
# Create one issue per organization from a manifest and a directory of bodies.
# Works for any of the generators in this directory -- the manifest carries the
# title and the label set, so this script does not care what is being sent.
#
#   .github/scripts/gen_broadcast_issues.py --out /tmp/bodies > /tmp/manifest.tsv
#   .github/scripts/create_issues.sh /tmp/manifest.tsv /tmp/bodies
#
# Manifest is tab-separated, one line per organization:
#
#   <org>  <comma-separated assignees>  <title>  <comma-separated labels>  [ignored...]
#
# Safe to re-run: an organization whose issue already exists under the same
# title is skipped, so a partial run can be finished without double-posting.
# Pass --dry-run to print what would be created and touch nothing.
#
# If a body contains the literal {{ISSUE}}, the issue is created with the
# placeholder neutralised and its body is then rewritten with the issue's own
# number -- the only way to tell a submitter "reference #N" when N does not
# exist until the issue does. A body without {{ISSUE}} is posted unchanged.
#
# .github/workflows/issue-routing.yml applies the From/To labels a second time,
# from the (From)/(To) sections in the body, and posts the comment that
# @mentions the organization. Setting the labels here as well means labelling
# does not depend on that workflow succeeding.
set -uo pipefail

DRY_RUN=0
[ "${1:-}" = "--dry-run" ] && { DRY_RUN=1; shift; }

MANIFEST="${1:?usage: $0 [--dry-run] <manifest.tsv> <bodies-dir>}"
BODIES="${2:?usage: $0 [--dry-run] <manifest.tsv> <bodies-dir>}"
REPO="mlcommons/submissions_storage_v3.0"

command -v gh >/dev/null || { echo "gh is required" >&2; exit 1; }

# One API call, not one per organization.
existing=$(gh issue list --state all --limit 500 --json title -q '.[].title')
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT

created=0 skipped=0 failed=0
while IFS=$'\t' read -r org assignees title labels _rest; do
  [ -z "${org:-}" ] && continue
  body="$BODIES/$org.md"

  if [ ! -f "$body" ]; then
    echo "FAIL  $org : no body at $body" >&2; failed=$((failed + 1)); continue
  fi
  if grep -Fxq "$title" <<< "$existing"; then
    echo "SKIP  $org : an issue titled \"$title\" already exists"
    skipped=$((skipped + 1)); continue
  fi

  if [ "$DRY_RUN" = 1 ]; then
    echo "DRY   $org : \"$title\" assignees=[${assignees:--}] labels=[$labels]"
    continue
  fi

  # Created with the placeholder neutralised, then rewritten below once the
  # number is known. Anyone reading in that window sees a marker, not a wrong
  # number.
  sed 's/{{ISSUE}}/PLACEHOLDER/g' "$body" > "$tmp/create.md"

  args=(--title "$title" --body-file "$tmp/create.md")
  IFS=',' read -ra labs <<< "$labels"
  for l in "${labs[@]}"; do [ -n "$l" ] && args+=(--label "$l"); done
  IFS=',' read -ra who <<< "$assignees"
  for h in "${who[@]}"; do [ -n "$h" ] && args+=(--assignee "$h"); done

  if ! url=$(gh issue create "${args[@]}" 2>"$tmp/err"); then
    echo "FAIL  $org : $(tr '\n' ' ' < "$tmp/err")" >&2; failed=$((failed + 1)); continue
  fi
  number=${url##*/}

  if grep -q '{{ISSUE}}' "$body"; then
    sed "s/{{ISSUE}}/$number/g" "$body" > "$tmp/final.md"
    if ! gh api "repos/$REPO/issues/$number" -X PATCH -F body=@"$tmp/final.md" \
         >/dev/null 2>"$tmp/err"; then
      echo "PARTIAL $org -> $url created, but its body still says PLACEHOLDER: $(tr '\n' ' ' < "$tmp/err")" >&2
      failed=$((failed + 1)); continue
    fi
  fi

  echo "OK    $org -> $url"
  created=$((created + 1))
  # Creating issues back-to-back can trip GitHub's secondary rate limit.
  sleep 4
done < "$MANIFEST"

echo "---"
echo "created=$created skipped=$skipped failed=$failed"
[ "$failed" -eq 0 ]
