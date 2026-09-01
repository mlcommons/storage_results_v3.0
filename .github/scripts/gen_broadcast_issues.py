#!/usr/bin/env python3
"""Render one broadcast issue body per submitting organization.

Reads three things that already live in this repository, so the org list and
the review assignments never have to be retyped:

  .github/scripts/message.md        the message template (edit this to change
                                    what gets sent)
  .github/issue-notify-roster.json  the list of parties and their handles
  AssignedReviewers.md              who reviews whom

Writes one <org>.md per organization into the output directory, and prints a
tab-separated manifest that create_issues.sh consumes:

    <org>\t<assignable handles>\t<title>\t<labels>\t<orgs they review>\t<read-only>

Assignment and notification are different things. Only accounts with write
access can go in an issue's Assignees field, but an @mention notifies any
GitHub user. The manifest therefore separates the two, and the read-only column
is informational -- those people are still notified, by issue-routing.yml.

Usage:
    .github/scripts/gen_broadcast_issues.py [--out DIR] [--title-prefix TEXT] > manifest.tsv

Requires: gh, authenticated (used only to read the assignable-users list).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = REPO_ROOT / ".github/scripts/message.md"
ROSTER = REPO_ROOT / ".github/issue-notify-roster.json"
REVIEWERS_DOC = REPO_ROOT / "AssignedReviewers.md"
DOC_URL = ("https://github.com/mlcommons/submissions_storage_v3.0"
           "/blob/main/AssignedReviewers.md")


def parse_assignments(doc: str) -> dict[str, list[str]]:
    """Map reviewer org -> orgs it reviews, from the doc's own headings.

    The "Your assignment" section lists each reviewing organization as an h3
    and each organization it reviews as an "h4 arrow" beneath it.
    """
    body = doc.split("## Your assignment", 1)[1]
    out: dict[str, list[str]] = {}
    current = None
    for line in body.splitlines():
        reviewer = re.match(r"^### (.+?)\s*$", line)
        reviewed = re.match(r"^#### → (.+?) — ", line)
        if reviewer:
            current = reviewer.group(1).strip()
            out.setdefault(current, [])
        elif reviewed and current:
            out[current].append(reviewed.group(1).strip())
    return out


def assignable_logins() -> set[str]:
    """Logins with write access -- the only accounts an issue can be assigned to."""
    result = subprocess.run(
        ["gh", "api", "repos/mlcommons/submissions_storage_v3.0/assignees",
         "--paginate", "-q", ".[].login"],
        capture_output=True, text=True, check=True,
    )
    return {line.strip().lower() for line in result.stdout.splitlines() if line.strip()}


def render(template: str, org: str, reviews: list[str]) -> str:
    return (template
            .replace("{{TARGETS}}", ", ".join(f"**{r}**" for r in reviews))
            .replace("{{PLURAL}}", "submission" if len(reviews) == 1 else "submissions")
            .replace("{{DOC_URL}}", DOC_URL)
            .replace("{{ORG}}", org))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=Path("ops-issue-bodies"),
                    help="directory for the rendered bodies (default: ./ops-issue-bodies)")
    ap.add_argument("--title-prefix",
                    default="[Operations] Peer review status and deadlines",
                    help="issue title; the organization name is appended after an em dash")
    ap.add_argument("--labels", default="Operations,From ReviewChairs",
                    help="labels applied to every issue; 'To <org>' is added per org")
    args = ap.parse_args()

    roster = json.loads(ROSTER.read_text())["parties"]
    orgs = [k for k in roster if k != "ReviewChairs"]
    assignments = parse_assignments(REVIEWERS_DOC.read_text())

    # A silently-missing assignment would send someone an issue telling them to
    # review nothing, so refuse to render anything until the two files agree.
    unassigned = [o for o in orgs if not assignments.get(o)]
    if unassigned:
        print(f"ERROR: no review assignment found in {REVIEWERS_DOC.name} for: "
              f"{', '.join(sorted(unassigned))}", file=sys.stderr)
        return 1
    unlisted = sorted(set(assignments) - set(orgs))
    if unlisted:
        print(f"ERROR: {REVIEWERS_DOC.name} assigns reviews to parties absent from "
              f"{ROSTER.name}: {', '.join(unlisted)}", file=sys.stderr)
        return 1

    template = TEMPLATE.read_text()
    writable = assignable_logins()
    args.out.mkdir(parents=True, exist_ok=True)

    for org in sorted(orgs, key=str.lower):
        (args.out / f"{org}.md").write_text(render(template, org, assignments[org]))
        handles = roster[org]
        can_assign = [h for h in handles if h.lower() in writable]
        read_only = [h for h in handles if h.lower() not in writable]
        if not can_assign:
            print(f"WARNING: no assignable handle for {org}; its issue will have "
                  f"no assignee (mentions still reach {', '.join(read_only) or 'nobody'})",
                  file=sys.stderr)
        print("\t".join([org, ",".join(can_assign),
                         f"{args.title_prefix} — {org}",
                         f"{args.labels},To {org}",
                         ",".join(assignments[org]), ",".join(read_only)]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
