#!/usr/bin/env python3
"""Render a Flaw issue per organization whose system YAMLs fail the schema.

Scans every closed/<org>/systems/*.yaml and open/<org>/systems/*.yaml for the
solution-level fields the v3.0 schema requires, and writes one issue body per
organization that is missing any of them -- listing that organization's own
files, so the issue is actionable without the recipient having to work out
which of their files are affected.

Two shapes of body, because two things go wrong:

  * the solution block exists but lacks fields -- add the named keys
  * the solution block is absent entirely -- start from a worked example

Writes one <org>.md per affected organization into the output directory, and
prints the tab-separated manifest create_issues.sh consumes:

    <org>\t<assignable handles>\t<title>\t<labels>\t<affected>\t<total>\t<kind>

Bodies contain the literal {{ISSUE}} where the issue's own number belongs;
create_issues.sh substitutes it after the issue exists.

Usage:
    .github/scripts/gen_schema_field_issues.py [--out DIR] [--deadline TEXT] \
        > manifest.tsv

Requires: gh (authenticated, to read the assignable-users list), PyYAML.
"""
from __future__ import annotations

import argparse
import glob
import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
ROSTER = REPO_ROOT / ".github/issue-notify-roster.json"
REQUIRED = ("usable_capacity_tib", "availability")
# The review tooling branch. main predates several fixes, including the one
# that lets usable_capacity_tib be fractional.
TOOL_BRANCH = "reportgen-column-parity"

CLONE = f"""```bash
git clone --branch {TOOL_BRANCH} \\
    https://github.com/mlcommons/storage.git mlpstorage-review
cd mlpstorage-review
```"""

REPORTGEN_WARNING = """> [!WARNING]
> `reportgen` rewrites `results.csv` and `results.json` throughout the tree. **Do not
> include those in your PR** — staff regenerates them centrally. Commit only your
> `systems/*.yaml` files."""


def validate_section(org: str) -> str:
    """How to re-run validate, and what --submitters does not narrow.

    The flag is consumed only by the per-benchmark loader loop
    (submission_checker/loader.py). The system-description schema check, the
    structure check and the code-pool checks all run before that loop and are
    not filtered, so a scoped run still prints every organization's schema
    errors -- measured: warnings 191 -> 12 and informational 255 -> 13, errors
    256 -> 256. Saying "validate just your own submission" oversold it.
    """
    return f"""```bash
./mlpstorage validate /path/to/your/submissions_storage_v3.0 \\
    --submitters {org} --skip-output-file --csv /tmp/{org.lower()}-summary.csv
```

`--submitters` narrows the warnings and informational lines to your own runs,
but **not the errors** — the system-description schema check runs over the whole
tree whatever you pass it, so the lines above arrive mixed in with every other
organization's. Filter for your own path:

```bash
./mlpstorage validate /path/to/your/submissions_storage_v3.0 \\
    --submitters {org} --skip-output-file --csv /tmp/{org.lower()}-summary.csv \\
    | grep '/{org}/'
```"""

ROUTING = """### Your organization / role (From)

ReviewChairs

### Organization / role asked to respond (To)

{org}"""


def scan() -> tuple[dict[str, list[str]], dict[str, int], set[str]]:
    """-> (org -> affected paths, org -> total yamls, orgs with no solution block)."""
    affected: dict[str, list[str]] = {}
    total: dict[str, int] = {}
    no_solution: set[str] = set()
    for path in sorted(glob.glob(str(REPO_ROOT / "closed/*/systems/*.yaml"))
                       + glob.glob(str(REPO_ROOT / "open/*/systems/*.yaml"))):
        rel = str(Path(path).relative_to(REPO_ROOT))
        org = rel.split("/")[1]
        total[org] = total.get(org, 0) + 1
        try:
            doc = yaml.safe_load(open(path)) or {}
        except yaml.YAMLError as exc:
            print(f"WARNING: {rel} does not parse as YAML, skipping: {exc}", file=sys.stderr)
            continue
        solution = ((doc.get("system_under_test") or {}) or {}).get("solution")
        if not isinstance(solution, dict):
            affected.setdefault(org, []).append(rel)
            no_solution.add(org)
        elif any(field not in solution for field in REQUIRED):
            affected.setdefault(org, []).append(rel)
    return affected, total, no_solution


def file_list(paths: list[str]) -> str:
    items = "\n".join(f"- `{p}`" for p in paths)
    if len(paths) <= 10:
        return items
    return (f"<details>\n<summary>All {len(paths)} files — click to expand</summary>\n\n"
            f"{items}\n\n</details>")


def field_table() -> str:
    return """| Field | Value |
|---|---|
| `usable_capacity_tib` | Usable capacity of the storage under test, in TiB, minimum 1. **Fractional values are accepted** — report it as measured rather than rounding it to a whole number. |
| `availability` | Exactly one of `available`, `preview`, `RDI`. |"""


def missing_fields_body(org: str, paths: list[str], total: int, deadline: str) -> str:
    n = len(paths)
    scope = "all " if n == total else ""
    # An org submitting in both divisions has two systems/ dirs; one glob would
    # silently miss half its files.
    globs = " ".join(sorted({p.rsplit("/", 1)[0] + "/*.yaml" for p in paths}))
    branch = f"{org.lower()}-capacity-availability"
    return f"""**This is a new schema requirement that your submission predates**, not
something you got wrong at submission time. The v3.0 system-description schema now
requires two fields in every `systems/<name>.yaml` that did not exist when yours were
written: `usable_capacity_tib` and `availability`.

**Deadline: {deadline}.**

`mlpstorage validate` reports this for each affected file:

```
system_under_test -> solution -> usable_capacity_tib: Field required
system_under_test -> solution -> availability: Field required
```

### Affected {'file' if n == 1 else 'files'} — {scope}{n} of {org}'s {total} system \
{'description' if total == 1 else 'descriptions'}

{file_list(paths)}

### What to add

Two keys under `system_under_test:` → `solution:`, at the same indentation as
`capabilities:`:

```yaml
system_under_test:
    solution:
        ...
        capabilities:
            ...
        usable_capacity_tib:  <your usable capacity in TiB>   # <-- add
        availability:         <available | preview | RDI>     # <-- add
```

{field_table()}

### Get the current review tooling

Use the tip of this branch, **not `main`** — `main` predates several fixes, including
the one that lets `usable_capacity_tib` be fractional.

{CLONE}

### Check your work

{validate_section(org)}

Regenerate the results tables and check your own numbers:

```bash
./mlpstorage reports reportgen --results-dir /path/to/your/submissions_storage_v3.0
```

Open the top-level `results.csv`, find your rows, and confirm they read the way you
expect — the SUT capacity and availability columns are fed straight from the two
fields you are adding.

{REPORTGEN_WARNING}

### While you are in there

Please clear anything else validate flags against your system descriptions. Adding
these two fields is the only *schema* error in your YAMLs today, but validate reports
other findings too, and it is much cheaper for everyone to handle them in one PR than
one at a time.

### Open the PR

```bash
cd /path/to/your/submissions_storage_v3.0
git checkout main && git pull
git checkout -b {branch}

# add the two fields to each affected file
$EDITOR {globs}

git add {globs}      # ONLY the yaml files
git commit -m "{org}: add usable_capacity_tib and availability to system descriptions"
git push -u origin {branch}

gh pr create --title "{org}: add the new system-description schema fields" \\
             --body "Adds usable_capacity_tib and availability. Refs #{{{{ISSUE}}}}"
```

Please reference this issue (`#{{{{ISSUE}}}}`) in the PR description so the two stay linked.

{ROUTING.format(org=org)}
"""


def no_solution_body(org: str, paths: list[str], total: int, deadline: str,
                     errors: str) -> str:
    branch = f"{org.lower()}-system-description"
    return f"""**This is a new schema requirement that your submission predates**, not
something you got wrong at submission time — but your case needs more than the two
new fields, so please read this one carefully.

**Deadline: {deadline}.**

`{paths[0]}` contains only a `clients:` block. The `solution:` block — which
describes the storage under test itself — is absent entirely, along with
`deployment:`. `mlpstorage validate` reports:

```
{errors}
```

### Affected file

{file_list(paths)}

### Start from a worked example

Six complete, schema-valid system descriptions ship with the tool, in
`mlpstorage_py/system_description/` of the storage repo (see the clone command
below). Copy the `solution:` and `deployment:` blocks out of whichever is closest to
your architecture and edit the values:

| Example | Storage location | Product API | Describes |
|---|---|---|---|
| `example_NAS.yaml` | remote | file | A generic Enterprise NAS solution |
| `example_NFS.yaml` | remote | file | A generic NFS solution |
| `example_PFS.yaml` | remote_and_local | file | A parallel filesystem, with client-local store |
| `example_cloud.yaml` | remote | file | A cloud-hosted filesystem |
| `example_drive.yaml` | local | block | Single direct-attach NVMe drive |
| `example_remote_block.yaml` | remote | block | A remote-block solution |

Between them they cover all three `availability` values (`available`, `preview`,
`RDI`) and both optional and required capacity fields, so whichever you start from
already has the new fields filled in correctly.

The schema itself — every field, its type and its permitted values — is
`mlpstorage_py/system_description/schema.yaml`, and the two new fields are:

{field_table()}

### The other errors

`friendly_description` for your client is the empty string and needs some text. Both
client network interfaces are declared `state: up` with an empty `traffic: []`; an
interface that is up must list what it carries, or be marked down if it was unused.

### Get the current review tooling

Use the tip of this branch, **not `main`** — `main` predates several fixes, including
the one that lets `usable_capacity_tib` be fractional. The example files above are in
this checkout.

{CLONE}

### Check your work

{validate_section(org)}

Regenerate the results tables and check your own numbers:

```bash
./mlpstorage reports reportgen --results-dir /path/to/your/submissions_storage_v3.0
```

Open the top-level `results.csv`, find your row, and confirm it reads the way you
expect — the SUT columns are fed straight from the `solution:` block you are adding.

{REPORTGEN_WARNING}

### While you are in there

Please clear anything else validate flags against your system description, so it is
all handled in one PR rather than one finding at a time.

### Open the PR

```bash
cd /path/to/your/submissions_storage_v3.0
git checkout main && git pull
git checkout -b {branch}

# add the solution: and deployment: blocks, and fix the client errors
$EDITOR {paths[0]}

git add {paths[0]}                    # ONLY the yaml file
git commit -m "{org}: complete the system description"
git push -u origin {branch}

gh pr create --title "{org}: complete the system description" \\
             --body "Adds the solution and deployment blocks. Refs #{{{{ISSUE}}}}"
```

Please reference this issue (`#{{{{ISSUE}}}}`) in the PR description so the two stay linked.

{ROUTING.format(org=org)}
"""


def validator_errors(path: str) -> str:
    """Whatever mlpstorage's schema validator says about one file, if it is importable.

    The tool is a separate repository, so this degrades to a generic line rather
    than failing -- the issue is still useful without the verbatim output.
    """
    try:
        from mlpstorage_py.system_description.schema_validator import validate_file
    except Exception:
        return ("system_under_test -> solution: Field required\n"
                "system_under_test -> deployment: Field required")
    return "\n".join(str(e) for e in validate_file(str(REPO_ROOT / path)))


def assignable_logins() -> set[str]:
    result = subprocess.run(
        ["gh", "api", "repos/mlcommons/submissions_storage_v3.0/assignees",
         "--paginate", "-q", ".[].login"],
        capture_output=True, text=True, check=True,
    )
    return {line.strip().lower() for line in result.stdout.splitlines() if line.strip()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=Path("schema-issue-bodies"),
                    help="directory for the rendered bodies")
    ap.add_argument("--deadline", default="Tuesday, August 11th",
                    help="deadline quoted in the body")
    ap.add_argument("--labels", default="Flaw,From ReviewChairs",
                    help="labels applied to every issue; 'To <org>' is added per org")
    args = ap.parse_args()

    affected, total, no_solution = scan()
    if not affected:
        print("Every system YAML has the required fields; nothing to send.",
              file=sys.stderr)
        return 0

    roster = json.loads(ROSTER.read_text())["parties"]
    writable = assignable_logins()
    args.out.mkdir(parents=True, exist_ok=True)

    for org in sorted(affected, key=str.lower):
        paths = affected[org]
        if org in no_solution:
            body = no_solution_body(org, paths, total[org], args.deadline,
                                    validator_errors(paths[0]))
            title = ("[Flaw] System description is missing the solution and "
                     f"deployment blocks — {org}")
            kind = "no-solution-block"
        else:
            body = missing_fields_body(org, paths, total[org], args.deadline)
            title = ("[Flaw] System description YAMLs are missing "
                     f"usable_capacity_tib and availability — {org}")
            kind = "missing-fields"
        assert "{{ISSUE}}" in body, f"{org}: body lost its issue placeholder"
        (args.out / f"{org}.md").write_text(body)

        handles = roster.get(org, [])
        can_assign = [h for h in handles if h.lower() in writable]
        if not can_assign:
            print(f"WARNING: no assignable handle for {org}; its issue will have "
                  "no assignee", file=sys.stderr)
        print("\t".join([org, ",".join(can_assign), title, f"{args.labels},To {org}",
                         str(len(paths)), str(total[org]), kind]))

    print(f"# {len(affected)} organizations, "
          f"{sum(len(v) for v in affected.values())} files", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
