# Issue Management — MLPerf Storage v3.0 Submission Review

*Prepared by MLPerf Storage review staff, 2026-07-25.*

## Purpose

During the review window, submitters examine each other's submissions. This
repository's GitHub Issues are the channel for that: a submitter can ask
another organization a **question** about their submission, or report a
**potential flaw** in it. A label scheme makes the traffic filterable in both
directions, so every organization can see at a glance:

- the issues **they filed** against other submissions, and
- the issues **other organizations filed against theirs**.

## Filing an issue

Use the issue forms (Issues → **New issue**):

- **Question about a submission** — you want the other organization to
  clarify something. The form applies the `Question` label automatically.
- **Potential flaw in a submission** — you believe something in the
  submission is wrong. The form applies the `Flaw` label automatically, and
  asks for the affected submission path, your evidence, and (optionally) the
  Rules.md section you believe is implicated.

Both forms require two dropdown answers:

- **Your organization / role (From)** — who is filing;
- **Organization / role asked to respond (To)** — whose submission it
  concerns.

Each dropdown lists the 18 submitting organizations plus **ReviewChairs**,
**ANL** and **OpenLake**. Choose `ReviewChairs` in the To field to direct a
question or a flaw report at the review chairs rather than at another
submitter — for anything about the rules, the tooling, or the review process
itself.

## The label scheme

| Label | Count | Color | Meaning |
|---|---|---|---|
| `From <org>` | 18 (one per submitter) | blue | The organization that filed the issue |
| `To <org>` | 18 (one per submitter) | orange | The organization asked to respond |
| `From <party>` | 3 (ReviewChairs, ANL, OpenLake) | blue | Filed by that party |
| `To <party>` | 3 (ReviewChairs, ANL, OpenLake) | orange | Directed to that party |
| `Question` | 1 | purple | A question about a submission |
| `Flaw` | 1 | dark red | A potential flaw in a submission |

These 44 labels are the repository's **entire** label set — the GitHub
defaults have been removed so filtering stays unambiguous. Organization
names in labels match the directory names in this tree (e.g.
`Suzhou_Zishan_Longlin`, `holmesai_limited`).

Three parties are addressable besides the 18 submitting organizations:
`ReviewChairs`, the five v3.0 review chairs as a group (@FileSystemGuy,
@bbelgodere, @russfellows, @idevasena, @dslik); and `ANL` and `OpenLake`.

**Labels are applied automatically.** The form attaches the `Question` /
`Flaw` type label, and the `.github/workflows/issue-routing.yml` workflow
reads the two dropdown answers and applies the matching `From <party>` and
`To <party>` labels. This happens when the issue is filed, and again if it is
later edited to change an answer. Submitters therefore do not need triage
access, and no one has to wait for staff to file the issue correctly.

Only the values listed in `.github/issue-notify-roster.json` become labels, so
an unexpected answer is reported in the workflow log rather than silently
creating a new label.

## Getting notified

A GitHub label notifies nobody. To be notified when an issue is addressed to
your organization, add your GitHub usernames to your entry in
[`.github/issue-notify-roster.json`](.github/issue-notify-roster.json):

```json
"parties": {
  "YourOrg": ["your-github-handle", "a-colleague"],
}
```

The workflow then posts one comment mentioning those handles whenever an
issue is addressed **To** your organization, which is what actually triggers a
GitHub notification. An organization with an empty list is labeled but not
mentioned — which is the state every organization except `ReviewChairs`
starts in, so please open a PR adding your handles.

No one is notified for an issue their own organization filed, and the comment
is posted once per issue however many times it is edited.

## Filtering recipes

In the Issues tab search box (or bookmark the URLs):

| You want | Query |
|---|---|
| Issues my org filed | `is:issue label:"From <org>"` |
| Issues filed against my org | `is:issue label:"To <org>"` |
| Open flaws against my org | `is:issue is:open label:"To <org>" label:Flaw` |
| Open questions waiting on my org | `is:issue is:open label:"To <org>" label:Question` |
| Everything between two orgs | `is:issue label:"From <orgA>" label:"To <orgB>"` |
| Open items for the review chairs | `is:issue is:open label:"To ReviewChairs"` |

Example: `is:issue is:open label:"To nvidia" label:Flaw` lists the open
potential flaws reported against NVIDIA's submission.

## Lifecycle

1. **Filed** — submitter files via a form; type label attaches automatically.
2. **Labeled** — `From <party>` / `To <party>` are applied automatically from
   the dropdown answers, and the party addressed is notified by comment if it
   has handles in the roster.
3. **Response** — the `To` organization responds in the issue comments.
4. **Closed** — a `Question` closes when the asker is satisfied; a `Flaw`
   closes when it is resolved (fixed in-tree, withdrawn, or given a
   working-group disposition). Staff close issues that go stale after the
   review window ends.

## Related documents

- [`ApparentProblems.md`](ApparentProblems.md) — staff triage of every
  finding the validation tooling reports on this tree.
- [`CodeAnalysis.md`](CodeAnalysis.md) — staff audit of the 78 code images
  (explains the `CHECK-02` errors; no tampering found).
