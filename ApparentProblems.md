# Apparent Problems — MLPerf Storage v3.0 Submissions

*Prepared by MLPerf Storage review staff, 2026-07-28. Last revised
2026-08-17: Suzhou_Zishan_Longlin answered review issue
[#198](https://github.com/mlcommons/submissions_storage_v3.0/issues/198)
by removing the client-attached InfiniBand switch from all four of its
GalaxSphere system YAMLs
([#204](https://github.com/mlcommons/submissions_storage_v3.0/pull/204))
per the switch-scoping ruling, refreshing the four PDFs to match, and
the tables were regenerated over it: its twenty-one rows' `RU's` each
fell from 2 to 1 and their `Provisioned Power (W)` corrected from 4.8
to 1.6 kW, with no validate count moving at all. Before that, on
2026-08-14, twice: later that day, InspurData answered review issue
[#199](https://github.com/mlcommons/submissions_storage_v3.0/issues/199)
by correcting all five of its system YAMLs
([#201](https://github.com/mlcommons/submissions_storage_v3.0/pull/201))
— its storage-node PSU configuration is 2×1600 W, matching its PDF, and
the client-attached QM9790 switch is removed from the rack-unit scope
per the same switch-scoping ruling — and the tables were regenerated
over it: its seven rows' `RU's` each fell by 1 and their `Provisioned
Power (W)` cells corrected to 8.0/9.6 kW, with no validate count moving
at all. Earlier the same day, Everpure itemized the storage hardware for
its five systems ([#200](https://github.com/mlcommons/submissions_storage_v3.0/pull/200))
— `product_nodes` with per-node PSU power data — clearing the largest
slice of the *Storage hardware not itemized* family, and the tables have
been regenerated over it: its six rows' `RU's` cells fell by 16 apiece
(the declared totals had counted its eight-switch test-infrastructure
fabric, which the scoping rule excludes) and their `Provisioned Power
(W)` cells now publish, 66.8–130.8 kW. The itemization also raises 40
new schema errors — the custom fabric modules and blade enclosures have
no values for the schema's required CPU and memory fields — which the
review chairs have accepted as a test-design limitation, not a
submission defect; see *Custom hardware the schema cannot describe*
below. Previously, on 2026-08-13, the submitter formerly listed as
`Microsoft` became **Azure** at its own request (issue #196), following
the `nvidia` → **NVIDIA**, `holmesai_limited` → **HolmesAI** and
`farmgpu` → **FarmGPU** renames of the two days before — name changes
only; all forty-eight affected rows keep their Public IDs and no
measurement changed. On 2026-08-11, HPE
replaced its `K3000-kvcache` llama3.1-8b measurement with a rerun and the
tables were regenerated over it; the rerun references a code image that is
not yet in the pool. Before that, on 2026-08-10, OpenLake withdrew its vector_database
result at its own request, and the review chairs withdrew the ten
large-model subset checkpointing rows identified by
[mlcommons/storage#841](https://github.com/mlcommons/storage/issues/841).
**The backfill is finished**: all 99 system YAMLs now carry
`usable_capacity_tib` and `availability`, and `Availability` and `Usable
Capacity (TiB)` are populated for every published row. Since 2026-07-28 the
error count has moved from 38 down to 19 and now to 54 — the rise is
entirely the 40 accepted-limitation lines above; net of that family the
count fell to 14 — while warnings have fallen from 176 to 143 and
informational lines from 242 to 205. The results tables have been
regenerated: the field now publishes 150 rows across 19 organizations, down
from 171 across 20.*

## Summary

Running `mlpstorage validate` against this repository surfaces 54 errors,
143 warnings and 205 informational lines that bear on the submissions,
across the 19 submitting organizations.

**40 of those errors are a single family, and they are accepted**: the
custom fabric modules and blade enclosures in Everpure's newly itemized
storage hardware have no values for the schema's required CPU and memory
fields, and the review chairs have ruled that gap a test-design
limitation, not a submission defect — see *Custom hardware the schema
cannot describe* below. **5 more are what remains of a second family**:
two organizations describe an on-premises system with external storage
but leave `product_nodes` empty, so the storage-side hardware — and its
power supplies — is not itemized. Two published columns derive from that
section: the declared `RU's` totals have nothing to add up to, and the
`Provisioned Power (W)` column publishes blank for those rows. Everpure
cleared this family for its five systems on 2026-08-14; YanRongTech and
TuringData remain. See *Storage hardware not itemized* below.
Discounting both families, the error count is 9. The newest of those is
HPE's: its kvcache rerun references a code image that was never uploaded
to the pool — see *HPE kvcache rerun code image missing* below.

The schema backfill that dominated the previous three revisions is **done**.
It fell from 60 errors to 22 to zero as, in turn, HPE and InspurData, then
FarmGPU and ZettaLane, supplied `usable_capacity_tib` and `availability`;
Nutanix's outstanding file left with its withdrawal.

Every other item below is a genuine property of the submission data —
none are validator noise.

The findings fall into three groups: **bookkeeping gaps** left by upload
pruning, which look alarming but are mechanical; **advisory warnings** that
need reviewer judgment; and a small set of **submissions whose data cannot
be read by the tooling**, listed under *Report-generator observations* —
those are the ones that materially affect the published tables.

## Withdrawals from v3.0

Nine organizations have had results withdrawn — six at their own request,
and three in the review chairs' withdrawal of the large-model subset rows
(below). In total **29 rows and 16 system descriptions** have left the field
since the tables were first published, and the organization count has fallen
from 21 to 19.

| Organization | Withdrew | Public IDs |
|---|---|---|
| ANL | Whole submission — 8 rows, 9 systems, both divisions | `v3.0-0001`–`v3.0-0005`, `v3.0-0174`–`v3.0-0176` |
| Everpure | 5 rows — 2 RetinaNet training, 2 kv_cache, and its entire OPEN division | `v3.0-0020`–`v3.0-0023`, `v3.0-0177` |
| Suzhou_Zishan_Longlin | 3 llama3-8b checkpointing rows | `v3.0-0091`, `v3.0-0097`, `v3.0-0103` |
| Nutanix | Whole submission — 1 row, 1 system | `v3.0-0180` |
| TTA | 1 llama3-8b checkpointing row | `v3.0-0108` |
| OpenLake | 1 vector_database row | `v3.0-0076` |
| Nebius | 3 large-model subset checkpointing rows, 3 systems (chairs, storage#841) | `v3.0-0055`, `v3.0-0057`, `v3.0-0059` |
| NewFW | 6 large-model subset checkpointing rows (chairs, storage#841) | `v3.0-0062`–`v3.0-0064`, `v3.0-0068`–`v3.0-0070` |
| SAMSUNG | 1 large-model subset checkpointing row (chairs, storage#841) | `v3.0-0077` |

Everpure's withdrawals emptied three of its systems, so those system
descriptions went with the results; five systems remain, all CLOSED.
OpenLake's withdrawal emptied `openlake_hc44_1c1s` — the vector_database row
was the only benchmark that system published — so its description left too;
the organization stays in the tables with its other system,
`openlake-hbv4-1c1s-final`, and its checkpointing row `v3.0-0075`.
Suzhou_Zishan_Longlin keeps all four of its systems and TTA keeps its single
one, `seahorse-storage`, which still publishes four other workloads.

The Nebius, NewFW and SAMSUNG rows are the ten CLOSED checkpointing runs of
70B, 405B and 1250B in subset mode. Rules.md 4.3.5 defines subset mode only
for the 8B model, but the published rule text was missing the word "not" and
the tool enforced the typo, so these runs launched and validated through the
gap ([mlcommons/storage#841](https://github.com/mlcommons/storage/issues/841)).
The withdrawal also protects the submitters: a subset run measures one 8-GPU
node writing a single data-parallel slice — 114 GB, 94 GB or 161 GB instead
of the 912 GB, 5.29 TB or 18 TB a full run writes — so these rows published
single-node bandwidth beside whole-cluster numbers, 1.6–17 GiB/s writes
against full-run medians of 70, 156 and 294 GiB/s for the same models. Left
standing they would have read as results one to two orders of magnitude
below the field, when they are really a different, much smaller experiment —
non-comparable by construction, and unfairly unflattering to the
organizations that submitted them. Nebius's three subset systems carried
nothing else, so their descriptions left with them; NewFW's two Solidigm
systems and SAMSUNG's `MEMORY_AE` keep their 8B checkpointing, kv_cache,
training and vector_database workloads, and all three organizations stay in
the tables.

Every withdrawn Public ID is **retired**. None is reissued to anything else,
so every citation of a surviving ID elsewhere in this document and in the
review issues remains valid.

Findings that belonged to the departed organizations have been removed rather
than left standing against them: ANL's `crux-eagle` repackage, its
`polaris-nvme` unpublishable row, three §4.7.1 OPEN failover-callout gaps and
three §2.1.24 timestamp gaps; Nutanix's unfilled system description and the
question of which of its two kv_cache runs was intended; and the two Everpure
kv_cache leaves whose `.mlps-code-image` pointers resolved to nothing.

## Context: what staff already resolved in-tree

- **Pruned log placeholders** — 400 DLIO log/output files that exceeded
  GitHub size limits were pruned during upload; each was given a 16-byte
  `PRUNED BY STAFF` placeholder so file-presence checks distinguish
  deliberate pruning from missing files. The pass now covers the whole
  tree, including ZettaLane's RetinaNet runs, which arrived without their
  per-rank `output.json` files and without one `training_datagen.stdout.log`.
  This cleared the last of the `2.1.19 runFiles` and `2.1.14 datagenFiles`
  errors: **there are now none of either in the tree.**
- **Everpure system descriptions recovered and then refreshed** — Everpure's
  seven closed-division systems had no `.pdf`, which also failed the
  "results without pdf" check: 14 errors, now cleared. The PDFs were recovered
  from the raw-upload archives, and Everpure then supplied a refreshed set of
  all seven system descriptions, both `.yaml` and `.pdf`. The refreshed PDFs
  are one per system — the recovered set had a single document standing in for
  six of them, which is also what produced the 51-hosts-versus-32-hosts
  mismatch noted earlier in the review.
- **System-description backfill complete** — every one of the tree's 99
  system YAMLs now carries `usable_capacity_tib` and `availability`. FarmGPU
  (6 files) and ZettaLane (5) were the last two organizations outstanding.
  See *System-description schema fields* below for what the fields feed.
- **Results tables regenerated** — every `results.csv` / `results.json` has
  been regenerated against the current tree. The change is exactly the
  withdrawals plus the system-description edits merged since the tables were
  first published reaching them: 171 rows before, 150 after, the twenty-one
  removed rows exactly those withdrawn, none added, and **no surviving row's
  `Public ID` moved**. The only changed cells were `RU's` (46),
  `Availability` (50), `Usable Capacity (TiB)` (50) and `Type` (27), all of
  them following an edit a submitter made to a system description; the two
  regenerations after OpenLake's withdrawal and after the chairs' ten-row
  subset withdrawal changed no cell at all. No staff regeneration has
  changed a measurement anywhere in the tree. A later regeneration, after
  HPE's kvcache rerun, touched only that row (`v3.0-0149`): its Code and
  Logs links now point at the code image the rerun recorded, and four of its
  metric cells shifted in the twelfth significant digit — reproduction noise
  from the tables in HPE's merge having been generated with a different
  build of the tool, not a data change. The two regenerations of
  2026-08-14, after Everpure's hardware itemization and InspurData's
  #199 corrections, touched exactly twelve and fourteen cells
  respectively, and the regeneration of 2026-08-17, after
  Suzhou_Zishan_Longlin's #198 switch-scope correction, forty-two — in
  every case two per affected row; the next three bullets have the
  detail.
- **Everpure storage hardware itemized** — Everpure supplied `product_nodes`
  itemizations for all five of its systems
  ([#200](https://github.com/mlcommons/submissions_storage_v3.0/pull/200),
  2026-08-14): per-group quantities, rack units and PSU power blocks for
  its fabric modules, blade chassis and data nodes. This closes the
  Everpure slice of *Storage hardware not itemized* — through the previous
  revision, the largest. The regenerated tables changed its six rows
  (`v3.0-0014`–`v3.0-0019`) in exactly two cells each. The `RU's` cells
  fell by 16 apiece (43→27, 48→32, 53→37, 53→37, 63→47, 63→47): the
  previously declared totals had counted the eight SN5600 switches of
  Everpure's dedicated test-infrastructure fabric, 2U each, which the
  review chairs' switch-scoping ruling excludes — a client-attached switch
  is test infrastructure, not storage solution
  ([mlcommons/storage#846](https://github.com/mlcommons/storage/pull/846))
  — and the corrected totals now equal the itemized sums. The
  `Provisioned Power (W)` cells, blank since the column was introduced,
  now publish: 66.8, 82.8, 98.8 (two rows) and 130.8 (two rows) kW.
- **InspurData switch scope and PSU data corrected** — answering review
  issue [#199](https://github.com/mlcommons/submissions_storage_v3.0/issues/199),
  InspurData corrected all five of its system YAMLs
  ([#201](https://github.com/mlcommons/submissions_storage_v3.0/pull/201),
  2026-08-14): the client-attached QM9790 switch left the rack-unit and
  power scope per the chairs' switch-scoping ruling, and the KH-50000
  systems' storage-node PSU configuration was corrected from 4×2000 W to
  2×1600 W per node, matching its PDF. The regenerated tables changed
  its seven rows (`v3.0-0024`–`v3.0-0030`) in exactly two cells each:
  `RU's` fell by 1 (the switch's rack unit; 3→2 on the four AS13000G7
  rows, 7→6 on the three KH-50000 rows) and `Provisioned Power (W)`
  corrected from 11.2 to 8.0 kW and from 27.2 to 9.6 kW respectively.
  The itemized rack units again sum to the declared totals, and no
  validate count moved.
- **Suzhou_Zishan_Longlin switch scope corrected** — answering review
  issue [#198](https://github.com/mlcommons/submissions_storage_v3.0/issues/198),
  Suzhou_Zishan_Longlin removed the client-attached InfiniBand switch
  (one rack unit, 2×1600 W PSUs) from all four of its GalaxSphere
  system YAMLs
  ([#204](https://github.com/mlcommons/submissions_storage_v3.0/pull/204),
  2026-08-17) per the chairs' switch-scoping ruling, corrected each
  `total_rack_units` from 2 to 1, and refreshed the four PDFs to match
  — which also settles the rack-unit discrepancy the issue had raised,
  where the PDFs' declared total of 1 disagreed with the YAMLs' 2. The
  regenerated tables changed its twenty-one rows (`v3.0-0083` through
  `v3.0-0106`, less the three withdrawn llama3-8b checkpointing ids) in
  exactly two cells each: `RU's` fell from 2 to 1 and `Provisioned
  Power (W)` corrected from 4.8 to 1.6 kW — the remaining metadata
  node's single 1600 W PSU. The itemized rack units again equal the
  declared totals, and no validate count moved.
- **Code and Logs hyperlinks repaired** — every Code and Logs anchor in every
  results table pointed at `<division>/<org>/code-<hash>/`, but the
  content-addressed code-image pool is mode-agnostic by design and lives at
  `<org>/code-<hash>/`, shared across the CLOSED and OPEN divisions. All
  **356** links in the tree therefore resolved to nothing. The report
  generator has been fixed and the tables regenerated; all now resolve,
  with one later exception: `v3.0-0149`'s links point at the code image
  HPE's kvcache rerun recorded, which is not yet in the pool — see *HPE
  kvcache rerun code image missing* below.
- **Restored `*_metadata.json` files** — 85 metadata files pruned during
  upload were recovered from the raw-upload archives and committed
  (Azure 25, Everpure 25 closed + 1 open, Nebius 16, ANL 3 closed + 6
  open, NVIDIA 7, Alluxio 2 — ANL's nine have since left the tree with its
  withdrawal). This cleared 84 of the 87 missing-metadata warnings. Two
  `open/FarmGPU` leaves are the only ones that still lack theirs.
- **Results tables** — every `results.csv` / `results.json` is produced by the
  current report generator, which now generates the `Public ID`, `Type`,
  `Access Protocol`, `Availability`, `Usable Capacity (TiB)` and
  `Integrated Client Storage (TiB)` cells rather than leaving them for manual
  entry.
- **Stale results tables** — 26 `results.csv` / `results.json` files that
  the report generator does not produce and had never overwritten have been
  removed. They arrived with the original submission uploads in a format
  that predates the current results schema, and disagreed with the
  generated tables around them. Every affected system remains covered by
  the generated tables; no run directory was touched.

## Remaining errors

Of the 54 error lines, 50 are rule-keyed findings; the other 4 are
roll-up statements that restate them.

### Storage hardware not itemized — 5 errors, 2 orgs

`product_nodes is required for onprem deployment when storage_location is
'remote' — the storage-side hardware and its power supplies must be itemized
(the results table's Provisioned Power (W) cell is derived from them)`,
reported under `2.1.7`. Five system YAMLs describe an on-premises system whose
storage is external to the clients, yet carry no `product_nodes` section at
all. Two published columns depend on that section: the declared
`total_rack_units` (the `RU's` column) has no listed hardware to substantiate
it, and the `Provisioned Power (W)` column — the nameplate power of the
storage system's PSUs — publishes blank for every one of these systems' rows.

| Org | Files | Declared totals |
|---|---|---|
| YanRongTech | 3 | 2 each |
| TuringData | 2 | 2 each |

Everpure, the third and largest organization in this family through the
previous revision, cleared its five files on 2026-08-14 — see *Everpure
storage hardware itemized* among the staff-resolved items above. The
declared totals in the table are themselves in question: review issues
[#172](https://github.com/mlcommons/submissions_storage_v3.0/issues/172)
(YanRongTech) and
[#173](https://github.com/mlcommons/submissions_storage_v3.0/issues/173)
(TuringData) note that both organizations' PDFs describe three storage
nodes, so the declared `2` reads as a per-node figure rather than a
system total — itemizing the hardware will settle it either way.

Earlier revisions reported this same gap indirectly, as a rack-unit
arithmetic mismatch (`total_rack_units (43) does not match the sum … = 0`);
the schema now reports the root cause. Systems whose storage lives inside
the client nodes are exempt — client power is excluded from the sum by
design — as are cloud deployments, which carry no power data at all.

**To clear:** add a `product_nodes` entry per homogeneous group of storage
nodes (and a `product_switches` entry for any switch that is part of the
solution), each carrying `rack_units`, `quantity`, and a `chassis.power`
block (`min_psus_active`, plus `psus_configured` entries with `unit_count`,
`inlet_voltage`, `nameplate_power_watts` and `efficiency`). The itemized
rack units must sum to the declared `total_rack_units` — correct the total
if it is wrong. Only the system under test counts; client nodes are
excluded.

### Custom hardware the schema cannot describe — 40 errors, Everpure

Everpure's new `product_nodes` itemizations declare `cpu_model`,
`cpu_qty`, `cpu_cores` and `memory_capacity` as null on two of the three
node groups in each of its five systems: the XFM-8400 fabric module and
the CH-FB-II blade enclosure. Both are custom-designed hardware — neither
is an industry-standard server, and the facts the schema requires (a CPU
model, a socket count, a memory capacity) do not exist for them. The
schema has no way to say so, so every null raises `Input should be a
valid string`/`integer` under `2.1.7`: four fields × two node groups ×
five files = 40 error lines.

The review chairs have ruled these errors a test-design limitation, not a
submission defect (2026-08-14; the ruling is recorded in comments beside
the fields in the YAMLs themselves). The data the published columns
actually consume — rack units and PSU power — is complete on all three
node groups, and the third group, the Supermicro data nodes, fills every
field.

**To clear:** nothing is owed by the submitter. The fix is schema
vocabulary for marking a node group as custom hardware, which is a v4.0
schema question, not a v3.0 review item.

### NVIDIA supporting documents in `systems/` — 2 errors

`AIStore_Disclosure.pdf` and `AIStore_Scaling.pdf` sit in
`closed/NVIDIA/systems/` with no matching `.yaml`. `2.1.7` requires every
`.pdf` in a `systems/` directory to pair with a system description of the same
name, so each raises `has no matching <name>.yaml in systems/`.

Both are supplementary documents rather than system descriptions — they
describe AIStore's disclosure position and scaling behaviour across NVIDIA's
17 systems, and no single system owns them. NVIDIA's 17 real system
descriptions are all present, all paired, and all backfilled. A third
supporting file in the same directory, `CACHE_CLEARING.md`, raises nothing,
because the check pairs only `.pdf` against `.yaml`.

Nothing about the measurements is in question here; this is a packaging
question about where cross-system documentation belongs.

**To clear:** move the two PDFs somewhere other than `systems/` — the
submission's `code-<hash>/` image or a top-level document directory — or, if
the WG would rather they stay, `2.1.7` needs to allow unpaired supplementary
documents. Staff has no mechanism to permit them today.

### Everpure code-pool layout — 2 errors

`CHECK-04 poolLegacyCheck` ×1 and `2.1.5 requiredSubdirectoriesClosed` ×1:
`closed/Everpure/code` is a legacy code tree in a location the layout does not
allow — only `results` and `systems` may sit under a division's organization
directory. Everpure's actual code images are already in the pool at
`Everpure/code-<hash>/` and its published rows link to them correctly; this is
the leftover directory beside them.

The two `CHECK-01 poolPointerResolution` errors reported here in previous
revisions are gone: they belonged to the `…file_59…` kv_cache leaves, which
have been withdrawn.

**To clear:** delete `closed/Everpure/code`, or move anything it still holds
into the `Everpure/code-<hash>/` pool image it belongs to.

### HPE kvcache rerun code image missing — 1 error

HPE replaced its `K3000-kvcache` llama3.1-8b kvcache measurement with a
rerun (run `20260807_155647`, merged 2026-08-11), and the rerun's
`.mlps-code-image` pointer records code image `64104f04`. No
`HPE/code-64104f04/` exists in the pool — HPE's pool holds five other
images, so the rerun was made with a code tree that was never uploaded.
`CHECK-01 poolPointerResolution` flags the leaf.

The row (`v3.0-0149`) publishes the rerun's measurements, but its Code and
Logs links point at the recorded image and are dead until it lands. The
previous revision of the tables linked the row to `HPE/code-69d7248b/`,
which resolves but is not the code that produced the published numbers.

**To clear:** upload the code tree the rerun was executed from as
`HPE/code-64104f04/`. No rerun is needed — only the code image is missing.

## System-description schema fields

The v3.0 results table carries a shared System-Under-Test block —
`Type`, `Access Protocol`, `Availability`, `Usable Capacity (TiB)`,
`Integrated Client Storage (TiB)`, `Provisioned Power (W)` and `Public ID`.
These were previously blank placeholders filled in by hand after report
generation. They are now generated, which required the system description to
actually carry the underlying facts:

| Field | Required | Feeds |
|---|---|---|
| `solution.usable_capacity_tib` | yes | `Usable Capacity (TiB)` |
| `solution.availability` | yes | `Availability` (`available` / `preview` / `RDI`) |
| `solution.int_client_store_tib` | no | `Integrated Client Storage (TiB)` |
| `product_nodes[].chassis.power`, `product_switches[].power` | onprem with external storage | `Provisioned Power (W)` |

`usable_capacity_tib` and `int_client_store_tib` accept fractional values —
report the figure as measured rather than rounding it to a whole number of
TiB. The lower bound is 1 TiB. `int_client_store_tib` is optional and expected
to go unused in v3.0 — the column exists for v2.0 parity — so it should be
omitted unless the solution genuinely has integrated client storage; 21 rows
carry one.

`Type` and `Access Protocol` need no new fields — they are derived from
the `architecture` and `capabilities` blocks that every completed system YAML
already has.

**All 99 system YAMLs now carry both required fields**, across all 19
organizations, so `Availability` and `Usable Capacity (TiB)` are published for
every one of the 150 rows. Nothing further is owed on those two.

`Provisioned Power (W)` is new in this revision: the total nameplate rated
power of the storage system's PSUs — `nameplate_power_watts × unit_count`
summed over every PSU on the product nodes (× node quantity) and product
switches (× switch count). Client nodes and `rack_power_supplies` are
excluded, the same scoping as the rack-unit sum, and redundancy is not
netted out. It publishes for 62 of the 150 rows (26 systems across 8
organizations, 3.6–130.8 kW). Blank is the correct value for the 62 cloud
systems and for systems whose storage lives inside the client nodes; the
only rows *owing* a value are the five files in *Storage hardware not
itemized* above.

## Remaining warnings, by family

119 of the 143 warnings are rule-keyed. The other 24 come from the result
loader and are described in the two subsections at the end, as they are the
most consequential.

### 4.3.1 checkpointDataSizeRatio — 54 warnings, 17 orgs

Checkpoint data size below the 3× client-host-memory bound. Advisory per the
rules — flagged for reviewer awareness, not a compliance failure by itself.
Seven of the previous 61 left with the withdrawn subset rows.

### 5.4.2 / 4.4.2 / 3.4.2 — missing `fs_separation.json` — 25 warnings

VDB runs (NewFW 5, Suzhou_Zishan_Longlin 5, TTA 5), checkpointing runs
(ZettaLane 4) and training runs (ZettaLane 6, all RetinaNet) lack the
filesystem-separation artifact. These were made with older tool builds that
did not yet write it; warn-and-review-manually is the designed behavior.

### 3.3.1 trainingRunDataMatchesDatasize — 14 warnings, 7 orgs

Training runs whose dataset is smaller than the corresponding `datasize`
calculation requires (YanRongTech 6, ZettaLane 3, and one each for TTA,
Suzhou_Zishan_Longlin, HolmesAI, HPE, NVIDIA). Needs per-case
reviewer judgment.

### 4.7.4 checkpointSimultaneousRwSupport — 2 warnings, NewFW

Checkpointing runs where simultaneous read/write support could not be
confirmed from the recorded system data. ZettaLane's two cases, reported here
previously, are **resolved**: its refreshed system descriptions declare
`simultaneous_write: true` and `multi_host: true`, matching what its
completed checkpointing runs imply. Six of NewFW's previous eight sat on the
withdrawn subset leaves; the two that remain are on its llama3-8b runs.

**To clear:** correct the `capabilities` block if the declaration is wrong, or
confirm for the record that it is right.

### 2.1.12 trainingPhases — 8 warnings, 6 orgs

`datasize/` phase directories genuinely absent from the submitted training
trees (ZettaLane 3, and one each for Suzhou_Zishan_Longlin, TTA,
HolmesAI, HPE, NVIDIA).

**To clear:** include the `datasize/` phase output for each affected workload.

### 2.1.24 checkpointingTimestampGap — 1 warning, Everpure

A single closed-division checkpointing invocation-to-invocation timestamp gap
outside the expected bound.

### 5.4.1 vdbPathArgs — 5 warnings, SAMSUNG

VDB runs with `storage_root` unset in the recorded arguments — the storage
target must be inferred manually for review.

### 5.3.5 vdbGroundTruthIntegrity — 5 warnings, TTA

VDB runs with no `result_verdict.json` (older tool build; recall is present
via other artifacts, verdict file absent).

### 3.3.3 trainingSingleHostSimulatedAccelerators — 4 warnings, 3 orgs

Single-host submissions with a low simulated-accelerator count (NewFW 2,
Alluxio 1, ZettaLane 1). Advisory.

### 4.7.1 checkpointCacheFlushValidation — 1 warning, HPE

**HPE `e2000` llama3-70b.** The write-phase-to-read-phase gap could not be
shown to satisfy the 30-second cache-flush bound because the gap is
*negative*: the recorded write-host and read-host clocks or timezones
disagree. The measurement is not impugned, the timestamps are.

**To clear:** resupply the two invocations' metadata with the clocks
reconciled, or provide a note explaining the offset for the record.

### Missing `*_metadata.json` — 2 warnings, FarmGPU

`Could not find metadata file at …`: the two `open/FarmGPU` kv_cache runs
`potato8-qlc-np6-open-tnf-u400` and `-70b`.

On a kv_cache run this file is not cosmetic: it is the only thing that
identifies the run to the loader, so without it the whole run directory is
dropped and its metrics reach no table. (On training and checkpointing runs
the loader recovers the benchmark type from the Hydra configs, and the file's
absence costs nothing.)

**To clear:** restore `kv_cache_<timestamp>_metadata.json` in each affected run
leaf from your own run archives.

### Missing run-level `summary.json` — 22 warnings, 5 orgs

`Could not load Summary log from …`: SAMSUNG 7, NewFW 6,
Suzhou_Zishan_Longlin 6, FarmGPU 2 (open), ZettaLane 1. By workload:
vector_database 19, kv_cache 3. The run-level aggregation step never wrote
its output for these runs. OpenLake's 13, reported here previously, left with
its withdrawn vector_database tree.

**To clear:** re-run the aggregation step for each affected run leaf. The 19 VDB
cases cost nothing in the tables — the report generator recovers those metrics
from the native statistics files — so the priority is the 3 kv_cache cases,
where a missing `summary.json` costs the row. One of those three only needs a
rename; see ZettaLane under *Report-generator observations*.

## Report-generator observations

Running `mlpstorage reports reportgen` over the tree produces a 150-row
global table covering all 19 organizations — 64 checkpointing, 59 training,
23 kv_cache and 4 vector_database rows. **Every published row carries
measurements.** One kv_cache workload that measured nothing is withheld from
the tables rather than published as an all-blank row; one kv_cache row is
built from one of two runs in its workload; and one published row aggregates
a run that lost most of its ranks. Those are the findings below.

`Public ID` is **pinned**: a row keeps its number permanently, so the IDs cited
here stay valid across regenerations. The published rows run `v3.0-0007` …
`v3.0-0181`. The registry holds 179 assignments, of which 150 publish and
**29 are retired** — the nine ANL numbers, Everpure's `v3.0-0020` …
`v3.0-0023` and `v3.0-0177`, Suzhou_Zishan_Longlin's `v3.0-0091`,
`v3.0-0097` and `v3.0-0103`, Nutanix's `v3.0-0180`, TTA's `v3.0-0108`,
OpenLake's `v3.0-0076`, and the ten large-model subset rows the review
chairs withdrew: Nebius's `v3.0-0055`/`0057`/`0059`, NewFW's
`v3.0-0062`–`0064` and `v3.0-0068`–`0070`, and SAMSUNG's `v3.0-0077`.
Two further numbers,
`v3.0-0006` and `v3.0-0138`, were never issued at all: both belong to rows
that have never published, so no assignment was ever recorded for them. This
regeneration minted no new IDs and moved none. The same row carries the same
ID in its per-model table, its per-org rollup and the global table. Only
measurement (`run`) rows are numbered; `datagen` / `datasize` leaf rows are
deliberately left blank.

`Type` and `Access Protocol` now populate for **all 150 rows** — the one
exception in the previous revision was Nutanix, which has withdrawn:

| Type | Rows | Access Protocol |
|---|---|---|
| Shared remote file | 83 | POSIX |
| Shared remote object | 25 | S3 |
| Shared remote and local file | 21 | POSIX |
| Failover local block | 8 | POSIX |
| Shared local file | 10 | POSIX |
| Failover remote block | 2 | POSIX |
| Shared remote and local object | 1 | S3 |

`Availability` and `Usable Capacity (TiB)` populate for **all 150 rows**,
`Integrated Client Storage (TiB)` for 21, `RU's` for 80, and
`Provisioned Power (W)` for 62. Eight of the 80 rack-unit figures are ones
their system YAMLs cannot substantiate — the rows of the five files whose
missing hardware itemization leaves their power cells blank; see
*Storage hardware not itemized* above.

These are the findings that affect published results:

- **ZettaLane `mayascale-gcp_c4hc144_n2hc64_1c_2s` kv_cache — row withheld.**
  The run leaf at `kv_cache/llama3.1-8b/run/20260627_194318` has three option
  directories and nine per-rank result files, but its aggregated summary is
  written under the older name `kvcache_run_summary_20260627_194318.json`,
  which the report generator does not read. Every KVCache cell came out blank,
  so the row is withheld rather than published empty.

  **To clear:** rename `kvcache_run_summary_20260627_194318.json` to
  `summary.json` in that run leaf. No rerun is needed — the measurements are
  there. Note that the row has never published, so it holds no Public ID: when
  it publishes it will be issued the next number, not `v3.0-0138`.

- **One kv_cache workload holds two measured runs, and only one row can
  publish.** A kv_cache row is keyed on
  `(division, organization, system, model, performance profile)`, so two runs
  placed under one system directory reduce to a single published row. The
  generator publishes the **latest error-free** run in the group; a run is not
  error-free if its `summary.json` records `partial_failure` or a non-zero mpirun
  trial exit, or if it has no `summary.json` at all:

  | Workload | Runs | Published | Dropped |
  |---|---|---|---|
  | Everpure `…51hosts_20…` (`v3.0-0019`) | 2 | `20260721_223359` | `20260716_165917` |

  The two other workloads in this table in the previous revision — Everpure's
  `…51hosts_30…` and Nutanix's `wsclient01` — have both been withdrawn. The
  rule is deterministic, but it carries no claim to being the submitter's
  intent, and the row emits a warning naming the published run and the dropped
  one.

  **To clear:** confirm which run represents your submission, or repackage so
  each run has its own system directory and system description.

- **One published row aggregates a run that lost most of its ranks
  (`v3.0-0178`).**
  `open/FarmGPU/…/potato8-qlc-np6-open-tnf-70b/kv_cache/llama3.1-70b-instruct/run/20260709_215001`
  records `partial_failure: true` with 45 missing per-rank result files, so its
  metrics are a mean over the surviving ranks. Its layout is canonical and it
  groups cleanly, so the row looks like any other; it is flagged with the
  missing-file and failed-trial counts.

  **To clear:** re-run it, or leave it pending the WG's ruling on question 5.

- **Three VDB runs without `summary.json`** (NewFW, SAMSUNG,
  Suzhou_Zishan_Longlin — one run each; OpenLake's, reported here
  previously, left with its withdrawal). The report generator recovers the
  metrics from the native statistics files, so these rows are populated and
  nothing is missing from the tables. No action needed for publication.

## Informational lines

The 205 `[INFO]` lines are informational only. They record what was checked
and observed, and call for no action.

## Open policy questions for the Working Group

1. **Per-rank `output.json` requirement (2.1.19)** — DLIO writes per-rank
   output files, but nearly every submitter pruned them for upload. Should
   Rules.md continue to require them in the submission package?
2. **CLOSED-division local code modifications** — 8 code images contain
   small harness workarounds, dependency pins, a package-mirror
   substitution, or tunable-parameter changes, detailed in
   [`CodeAnalysis.md`](CodeAnalysis.md). Staff assessment is that none affect
   measurement integrity; formal WG disposition may still be wanted. (The
   ninth, ANL's HPC launcher portability fix, left with that organization's
   withdrawal. `CodeAnalysis.md` still describes the tree as it stood at 78
   code images; there are now 72 — OpenLake's two vector_database images,
   which carried only benign deployment configuration, left with its
   withdrawal.)
3. **Runs with no aggregated `summary.json`** — 22 warnings, and the sole
   remaining reason one kv_cache workload publishes no row at all. Is an
   unaggregated run a valid submission, or should the submitter re-run the
   aggregation step? Related: the report generator **withholds** a row whose
   workload block is entirely blank rather than publishing it empty, since the
   fixed schema has no column in which to qualify it. The WG may wish to confirm
   that withholding is the right disposition, versus publishing the row with an
   explicit marker.
4. **Which run is the submission, when a workload contains several?** One
   kv_cache workload still contains two measured runs under a single system
   directory and therefore reduces to one published row (table above).
   Selection is deterministic — the latest error-free run — but the tool
   cannot know a submitter's intent. Should Rules.md require exactly one
   measured run per kv_cache workload directory, or should a workload with
   several publish a row per run? The latter needs a row key that
   distinguishes them, which today it has not.
5. **Should a partially-failed run be publishable?** The kv_cache benchmark
   records `partial_failure` and `trial_failures` in `summary.json` when
   ranks lose their result files or mpirun trials exit non-zero. One run
   in this tree carries the flag and it is published. Its metrics are a
   mean over the surviving ranks. The report generator flags such rows;
   the WG should decide whether they are admissible, and if so above what
   surviving-rank threshold.
6. **Supplementary documents in `systems/`** — `2.1.7` requires every `.pdf`
   in a `systems/` directory to pair with a same-named `.yaml`, which leaves
   nowhere to put documentation that describes a submission as a whole rather
   than one system. NVIDIA has two such files. Should Rules.md name a location
   for them, or relax the pairing check?

## Conclusion

The tree is in reasonable shape, and no finding suggests an invalid
measurement. The schema backfill that made up the bulk of the error count
through the last three revisions is finished, and with it the last reason the
`Availability` and `Usable Capacity (TiB)` columns were incomplete. Both now
publish for all 150 rows.

The items that genuinely need action before publication are narrow, and each has
a named owner and a specific fix in the section above it: the five systems
whose storage hardware is not itemized — leaving their rack-unit totals
unsubstantiated and their `Provisioned Power (W)` cells blank — across
YanRongTech and TuringData; Everpure's leftover `closed/Everpure/code` directory; the code
image HPE's kvcache rerun was executed from, which needs uploading;
ZettaLane's `mayascale` — the one workload that publishes no row at all;
FarmGPU's two kv_cache runs whose metadata files were pruned at upload; and
the one workload whose intended run needs confirming by its submitter. Together those account
for the only measurements currently missing from or misreported in the results
tables. ZettaLane's is a one-file rename; the rest need submitter data.

The row built from one of two runs is the item on that list that is not merely
a gap. A workload with no readable measurement publishes nothing, which a
reviewer will notice when the system is absent; a workload containing several
runs publishes a *populated* row that looks complete, which a reviewer will
not. That row carries a warning naming what was dropped, but a warning is a
disclosure, not a fix — only the submitter can say which run was intended.
