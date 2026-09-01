# Assigned Reviewers — MLPerf Storage v3.0

*Generated from `results.csv` — 171 published result rows, 107 systems, 20
submitting organizations. Public IDs are **pinned**: a row keeps its number
permanently, so an ID cited here or in an issue stays valid.*

---

> ## ANL has withdrawn — nvidia now has one reviewer, not two
>
> ANL's submission trees have been removed from the repository at its request,
> taking 8 rows and 9 systems out of the field. **ANL has been removed from this
> document without rebalancing anything else**: every other organization reviews
> exactly what it reviewed before.
>
> Two consequences to be aware of:
>
> - **nvidia is now reviewed by Alluxio alone.** ANL was its first reviewer.
>   nvidia is the largest submission in the field at 37 points, and it is the one
>   organization currently below the two-reviewer standard described under *How
>   this works*.
> - **TTA and TuringData each lost their largest assignment** and now sit at
>   6 points, well under a fair share. TTA reviews TuringData; TuringData reviews
>   Nutanix and OpenLake.
>
> Nobody needs to do anything differently unless the review chairs assign a
> second reviewer to nvidia.

> ## Nutanix joined the field after the first assignment
>
> Nutanix submits one kv_cache row (`v3.0-0180`). Adding it as a reviewer changed
> four assignments at the time. If your assignment moved then, it is one of
> these four:
>
> | Submission | Was reviewed by | Now reviewed by |
> |---|---|---|
> | farmgpu | ZettaLane | **Nutanix** |
> | YanRongTech | TTA | **Nutanix** |
> | UBIX | HPE | **ZettaLane** |
> | SAMSUNG | TuringData | **HPE** |
>
> Everyone else reviews exactly what they reviewed before.

> ## One row is no longer published
>
> It was withheld because it carried **no measurements at all** — every metric
> cell was blank, which in a table with no issues column is indistinguishable
> from a system that genuinely measured zero. Its Public ID is **retired**: held
> for this row, never reissued to anything else.
>
> | Public ID | Organization | System | Benchmark | Why |
> |---|---|---|---|---|
> | `v3.0-0138` | ZettaLane | `mayascale-gcp_c4hc144_n2hc64_1c_2s` | kv_cache | The run's summary is named `kvcache_run_summary_20260627_194318.json`; reportgen reads `summary.json`, so every pass-through metric was blank. |
>
> ZettaLane's withheld row is offset by a new RetinaNet row on the same system
> (`v3.0-0181`), so ZettaLane stands at **6 rows across 5 systems**. The gap is
> recoverable by the submitter: rename the summary file, and the row comes back
> under the same ID.
>
> Nine further numbers — `v3.0-0001` … `v3.0-0006` and `v3.0-0174` …
> `v3.0-0176` — are retired to the ANL withdrawal. Published IDs therefore run
> `v3.0-0007` … `v3.0-0181`.

> ## Two submissions' published numbers need a second look
>
> **Nutanix (`v3.0-0180`)** — the system directory holds two complete kv_cache
> runs. Reportgen publishes the *latest error-free* one (`20260723_235425`), but
> the `results.csv` Nutanix uploaded reported the earlier run
> (`20260723_213946`). The two differ by roughly 1%% on throughput. **If you are
> reviewing Nutanix, the published row will not match the numbers the submitter
> prepared** — that is expected, and which run is intended is an open question
> for the submitter.
>
> **Everpure (`v3.0-0019`, `v3.0-0021`)** — both publish different measurements
> than they did earlier in the review, for the same reason: reportgen selects the
> latest error-free run, and both systems submitted two clean kv_cache runs.
> Checking either row against an earlier copy of the table will not reconcile.
> The rule is "latest error-free", not "best": `51hosts_30` improved on
> throughput and bandwidth but its P95 latencies rose, and both are published as
> measured.

---

## How this works

**Every organization's submission is reviewed by two other organizations**, and
no organization reviews itself. One exception stands at present: nvidia is
reviewed by Alluxio alone, because its other reviewer was ANL, which has
withdrawn. See the callout at the top.

**The unit of assignment is a whole organization, never part of one.** If you are
assigned an organization, you review *all* of its rows and *all* of its systems.
You read its `systems/` descriptions and its `code-*/` directory once, then apply
that context to every row it submitted. There is no need to coordinate with your
co-reviewer about who covers which half — you each cover the whole thing,
independently.

**Load is equalized by varying how many organizations you review — not by
splitting them.** Assignments range from one organization to three. Whoever draws
a large submitter draws only that one; whoever draws small submitters draws
several. Nobody is assigned more than three.

### Review leads

Each organization names **one review lead** — the person accountable for that
organization's assigned reviews getting done, and the first point of contact when
someone has a question about that organization's own submission. The lead does not
have to do all the work personally; they own the outcome.

Issue labels still notify each organization's full contact list from
`.github/issue-notify-roster.json`, so naming a lead does not cut anyone out of the
traffic.

### The effort metric

Review effort is counted in **points**:

```
points = (number of result rows) + (number of distinct systems)
```

Each row needs its numbers checked; each system needs its description and
configuration read. Both halves matter, because submissions come in opposite
shapes — `Suzhou_Zishan_Longlin` has 24 rows across just 4 systems, while `nvidia`
has 20 rows across 17 systems. Counting only rows would understate the second;
counting only systems would understate the first.

The field totals **278 points** (171 rows + 107 systems). Reviewed twice over,
that would be 556 points spread across 20 organizations — a fair share of
**27.8 points** each. Most organizations land between 79% and 133% of that;
TTA and TuringData sit at 22% because their largest assignment, ANL, withdrew
and the assignment has deliberately not been rebalanced around it.

### No mutual review

The assignment contains **no reciprocal pairs** — there is no case where
organization A reviews B while B also reviews A.

---

## Your assignment

Find your organization below. Everything listed under it is yours to review.

### Alluxio

**Review lead:** @Stephen-Pu

**Reviews 1 organization — 37 points (133% of a fair share).**

#### → nvidia — 20 rows, 17 systems, 37 points

- **Public IDs:** v3.0-0154 – v3.0-0173
- **Benchmarks:** Checkpointing 12, Training 8
- **Submission tree:** `closed/nvidia/`
- **Ask questions of:** @gaikwadabhishek (nvidia review lead)

<details><summary>All 17 systems</summary>

- `closed/nvidia/systems/aistore-12n-oci-bm-denseio-e5-128-16client.yaml` — 2 rows
- `closed/nvidia/systems/aistore-12n-oci-bm-denseio-e5-128-1client.yaml` — 1 row
- `closed/nvidia/systems/aistore-12n-oci-bm-denseio-e5-128-20client-unet3d.yaml` — 1 row
- `closed/nvidia/systems/aistore-12n-oci-bm-denseio-e5-128-8client.yaml` — 1 row
- `closed/nvidia/systems/aistore-3n-aws-i8ge-150g-4client-m8gn24xl-unet3d.yaml` — 1 row
- `closed/nvidia/systems/aistore-3n-aws-i8ge-150g-5client-m8gn24xl.yaml` — 1 row
- `closed/nvidia/systems/aistore-3n-gcp-z3-200g-8client-n2d96.yaml` — 1 row
- `closed/nvidia/systems/aistore-3n-oci-bm-denseio-e5-128-1client.yaml` — 1 row
- `closed/nvidia/systems/aistore-3n-oci-bm-denseio-e5-128-5client-retinanet.yaml` — 1 row
- `closed/nvidia/systems/aistore-3n-oci-bm-denseio-e5-128-5client-unet3d.yaml` — 1 row
- `closed/nvidia/systems/aistore-3n-oci-bm-denseio-e5-128-8client-405b-1t.yaml` — 2 rows
- `closed/nvidia/systems/aistore-3n-oci-bm-denseio-e5-128-8client.yaml` — 1 row
- `closed/nvidia/systems/aistore-6n-oci-bm-denseio-e5-128-10client-retinanet.yaml` — 1 row
- `closed/nvidia/systems/aistore-6n-oci-bm-denseio-e5-128-10client-unet3d.yaml` — 1 row
- `closed/nvidia/systems/aistore-6n-oci-bm-denseio-e5-128-1client.yaml` — 1 row
- `closed/nvidia/systems/aistore-6n-oci-bm-denseio-e5-128-8client-405b-1t.yaml` — 2 rows
- `closed/nvidia/systems/aistore-6n-oci-bm-denseio-e5-128-8client.yaml` — 1 row

</details>


### Everpure

**Review lead:** @lou-lydiksen-purestorage

**Reviews 1 organization — 33 points (119% of a fair share).**

#### → Microsoft — 17 rows, 16 systems, 33 points

- **Public IDs:** v3.0-0031 – v3.0-0047
- **Benchmarks:** Training 13, Checkpointing 4
- **Submission tree:** `closed/Microsoft/`
- **Ask questions of:** @wolfgang-desalvador (Microsoft review lead)

<details><summary>All 16 systems</summary>

- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-1280TiB-16-Standard_E192is_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-160TiB-2-Standard_E192is_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-160TiB-3-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-2400TiB-46-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-4096TiB-128-Standard_E104is_v5.yaml` — 2 rows
- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-4096TiB-70-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-800TiB-16-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-20-25632TiB-70-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-20-4800TiB-16-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-20-960TiB-3-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-250-400TiB-16-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-250-80TiB-3-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-40-2400TiB-16-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-40-480TiB-3-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-500-200TiB-16-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-500-40TiB-3-Standard_D192ds_v6.yaml` — 1 row

</details>


### InspurData

**Review lead:** @Dandy-yin

**Reviews 1 organization — 33 points (119% of a fair share).**

#### → Microsoft — 17 rows, 16 systems, 33 points

- **Public IDs:** v3.0-0031 – v3.0-0047
- **Benchmarks:** Training 13, Checkpointing 4
- **Submission tree:** `closed/Microsoft/`
- **Ask questions of:** @wolfgang-desalvador (Microsoft review lead)

<details><summary>All 16 systems</summary>

- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-1280TiB-16-Standard_E192is_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-160TiB-2-Standard_E192is_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-160TiB-3-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-2400TiB-46-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-4096TiB-128-Standard_E104is_v5.yaml` — 2 rows
- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-4096TiB-70-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-125-800TiB-16-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-20-25632TiB-70-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-20-4800TiB-16-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-20-960TiB-3-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-250-400TiB-16-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-250-80TiB-3-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-40-2400TiB-16-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-40-480TiB-3-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-500-200TiB-16-Standard_D192ds_v6.yaml` — 1 row
- `closed/Microsoft/systems/AMLFS-Durable-Premium-500-40TiB-3-Standard_D192ds_v6.yaml` — 1 row

</details>


### Microsoft

**Review lead:** @wolfgang-desalvador

**Reviews 2 organizations — 31 points (112% of a fair share).**

#### → Nebius — 14 rows, 14 systems, 28 points

- **Public IDs:** v3.0-0048 – v3.0-0061
- **Benchmarks:** Checkpointing 10, Training 3, KVCache 1
- **Submission tree:** `closed/Nebius/`
- **Ask questions of:** @oralzb (Nebius review lead)

<details><summary>All 14 systems</summary>

- `closed/Nebius/systems/nebius-kvcache-b300.yaml` — 1 row
- `closed/Nebius/systems/nebius-s3-ckpt-llama3-405b.yaml` — 1 row
- `closed/Nebius/systems/nebius-s3-ckpt-llama3-70b.yaml` — 1 row
- `closed/Nebius/systems/nebius-s3-ckpt-llama3-8b.yaml` — 1 row
- `closed/Nebius/systems/nebius-s3-retinanet-32nx24-cm64.yaml` — 1 row
- `closed/Nebius/systems/nebius-s3-unet3d-21n.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-1t-default.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-1t-subset.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-405b-default.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-405b-subset.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-70b-default.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-70b-subset.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-8b-default.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-retinanet-256.yaml` — 1 row

</details>

#### → holmesai_limited — 2 rows, 1 system, 3 points

- **Public IDs:** v3.0-0147 – v3.0-0148
- **Benchmarks:** Training 2
- **Submission tree:** `closed/holmesai_limited/`
- **Ask questions of:** @kenzeng-China (holmesai_limited review lead)

<details><summary>All 1 system</summary>

- `closed/holmesai_limited/systems/StorMeshAI.yaml` — 2 rows

</details>


### Nebius

**Review lead:** @oralzb

**Reviews 1 organization — 28 points (101% of a fair share).**

#### → Suzhou_Zishan_Longlin — 24 rows, 4 systems, 28 points

- **Public IDs:** v3.0-0083 – v3.0-0106
- **Benchmarks:** Checkpointing 11, Training 8, KVCache 4, VectorDB 1
- **Submission tree:** `closed/Suzhou_Zishan_Longlin/`
- **Ask questions of:** @daddypig88 (Suzhou_Zishan_Longlin review lead)

<details><summary>All 4 systems</summary>

- `closed/Suzhou_Zishan_Longlin/systems/GalaxSphere-1Tier0.yaml` — 6 rows
- `closed/Suzhou_Zishan_Longlin/systems/GalaxSphere-2Tier0.yaml` — 6 rows
- `closed/Suzhou_Zishan_Longlin/systems/GalaxSphere-3Tier0.yaml` — 6 rows
- `closed/Suzhou_Zishan_Longlin/systems/GalaxSphere-4Tier0.yaml` — 6 rows

</details>


### NewFW

**Review lead:** @AjanZhong

**Reviews 1 organization — 28 points (101% of a fair share).**

#### → Nebius — 14 rows, 14 systems, 28 points

- **Public IDs:** v3.0-0048 – v3.0-0061
- **Benchmarks:** Checkpointing 10, Training 3, KVCache 1
- **Submission tree:** `closed/Nebius/`
- **Ask questions of:** @oralzb (Nebius review lead)

<details><summary>All 14 systems</summary>

- `closed/Nebius/systems/nebius-kvcache-b300.yaml` — 1 row
- `closed/Nebius/systems/nebius-s3-ckpt-llama3-405b.yaml` — 1 row
- `closed/Nebius/systems/nebius-s3-ckpt-llama3-70b.yaml` — 1 row
- `closed/Nebius/systems/nebius-s3-ckpt-llama3-8b.yaml` — 1 row
- `closed/Nebius/systems/nebius-s3-retinanet-32nx24-cm64.yaml` — 1 row
- `closed/Nebius/systems/nebius-s3-unet3d-21n.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-1t-default.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-1t-subset.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-405b-default.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-405b-subset.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-70b-default.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-70b-subset.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-ckpt-llama3-8b-default.yaml` — 1 row
- `closed/Nebius/systems/nebius-sfs-retinanet-256.yaml` — 1 row

</details>


### Nutanix

**Review lead:** @willo7734

**Reviews 2 organizations — 22 points (79% of a fair share).**

#### → farmgpu — 9 rows, 6 systems, 15 points

- **Public IDs:** v3.0-0140 – v3.0-0146, v3.0-0178 – v3.0-0179
- **Benchmarks:** KVCache 6, Checkpointing 2, Training 1
- **Submission tree:** `closed/farmgpu/`, `open/farmgpu/`
- **Ask questions of:** @mrf512 (farmgpu review lead)

<details><summary>All 6 systems</summary>

- `closed/farmgpu/systems/hickory.yaml` — 4 rows
- `closed/farmgpu/systems/potato1-qlc-closed-tcm.yaml` — 1 row
- `closed/farmgpu/systems/potato8-qlc-closed-tcm.yaml` — 1 row
- `closed/farmgpu/systems/potato8-qlc-np2-closed-tcm.yaml` — 1 row
- `open/farmgpu/systems/potato8-qlc-np6-open-tnf-70b.yaml` — 1 row
- `open/farmgpu/systems/potato8-qlc-np6-open-tnf-u400.yaml` — 1 row

</details>

#### → YanRongTech — 4 rows, 3 systems, 7 points

- **Public IDs:** v3.0-0130 – v3.0-0133
- **Benchmarks:** Checkpointing 2, KVCache 1, Training 1
- **Submission tree:** `closed/YanRongTech/`
- **Ask questions of:** @limengran-yr (YanRongTech review lead)

<details><summary>All 3 systems</summary>

- `closed/YanRongTech/systems/YanRongTech_F9000X_2_Clients.yaml` — 1 row
- `closed/YanRongTech/systems/YanRongTech_F9000X_8_Clients.yaml` — 1 row
- `closed/YanRongTech/systems/YanRongTech_F9000X_9_Clients.yaml` — 2 rows

</details>


### OpenLake

**Review lead:** @arnavbalyan

**Reviews 1 organization — 28 points (101% of a fair share).**

#### → Suzhou_Zishan_Longlin — 24 rows, 4 systems, 28 points

- **Public IDs:** v3.0-0083 – v3.0-0106
- **Benchmarks:** Checkpointing 11, Training 8, KVCache 4, VectorDB 1
- **Submission tree:** `closed/Suzhou_Zishan_Longlin/`
- **Ask questions of:** @daddypig88 (Suzhou_Zishan_Longlin review lead)

<details><summary>All 4 systems</summary>

- `closed/Suzhou_Zishan_Longlin/systems/GalaxSphere-1Tier0.yaml` — 6 rows
- `closed/Suzhou_Zishan_Longlin/systems/GalaxSphere-2Tier0.yaml` — 6 rows
- `closed/Suzhou_Zishan_Longlin/systems/GalaxSphere-3Tier0.yaml` — 6 rows
- `closed/Suzhou_Zishan_Longlin/systems/GalaxSphere-4Tier0.yaml` — 6 rows

</details>


### SAMSUNG

**Review lead:** @dhoon-4890

**Reviews 2 organizations — 26 points (94% of a fair share).**

#### → Everpure — 11 rows, 8 systems, 19 points

- **Public IDs:** v3.0-0014 – v3.0-0023, v3.0-0177
- **Benchmarks:** Checkpointing 6, KVCache 3, Training 2
- **Submission tree:** `closed/Everpure/`, `open/Everpure/`
- **Ask questions of:** @lou-lydiksen-purestorage (Everpure review lead)

<details><summary>All 8 systems</summary>

- `closed/Everpure/systems/Everpure_FBEXA_file_32hosts_10-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 1 row
- `closed/Everpure/systems/Everpure_FBEXA_file_32hosts_15-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 1 row
- `closed/Everpure/systems/Everpure_FBEXA_file_32hosts_20-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 1 row
- `closed/Everpure/systems/Everpure_FBEXA_file_32hosts_30-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 3 rows
- `closed/Everpure/systems/Everpure_FBEXA_file_51hosts_20-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 2 rows
- `closed/Everpure/systems/Everpure_FBEXA_file_51hosts_30-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 2 rows
- `closed/Everpure/systems/Everpure_FBEXA_file_59-DN-DNOS-1.1.0-4845253c3899_50-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 1 row
- `open/Everpure/systems/Everpure_FBEXA_file_32hosts_30-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 3 rows

</details>

#### → YanRongTech — 4 rows, 3 systems, 7 points

- **Public IDs:** v3.0-0130 – v3.0-0133
- **Benchmarks:** Checkpointing 2, KVCache 1, Training 1
- **Submission tree:** `closed/YanRongTech/`
- **Ask questions of:** @limengran-yr (YanRongTech review lead)

<details><summary>All 3 systems</summary>

- `closed/YanRongTech/systems/YanRongTech_F9000X_2_Clients.yaml` — 1 row
- `closed/YanRongTech/systems/YanRongTech_F9000X_8_Clients.yaml` — 1 row
- `closed/YanRongTech/systems/YanRongTech_F9000X_9_Clients.yaml` — 2 rows

</details>


### Suzhou_Zishan_Longlin

**Review lead:** @daddypig88

**Reviews 2 organizations — 25 points (90% of a fair share).**

#### → Alluxio — 7 rows, 7 systems, 14 points

- **Public IDs:** v3.0-0007 – v3.0-0013
- **Benchmarks:** Training 4, Checkpointing 3
- **Submission tree:** `closed/Alluxio/`
- **Ask questions of:** @Stephen-Pu (Alluxio review lead)

<details><summary>All 7 systems</summary>

- `closed/Alluxio/systems/aws_c5n18xlarge_i3en24xlarge_8c_10s_8a.yaml` — 1 row
- `closed/Alluxio/systems/aws_c7i48xlarge_i3en12xlarge_1c_1s_32a.yaml` — 1 row
- `closed/Alluxio/systems/aws_c7i48xlarge_i3en12xlarge_1c_1s_8a.yaml` — 1 row
- `closed/Alluxio/systems/aws_m7i48xlarge_i3en12xlarge_32c_32s_512p.yaml` — 1 row
- `closed/Alluxio/systems/aws_r5n24xlarge_i3en12xlarge_1c_1s_8h.yaml` — 1 row
- `closed/Alluxio/systems/aws_r5n24xlarge_i3en12xlarge_4c_10s_64p.yaml` — 1 row
- `closed/Alluxio/systems/rigA_c5n18xl.yaml` — 1 row

</details>

#### → ZettaLane — 6 rows, 5 systems, 11 points

- **Public IDs:** v3.0-0134 – v3.0-0137, v3.0-0139, v3.0-0181
- **Benchmarks:** Training 3, Checkpointing 2, KVCache 1
- **Submission tree:** `closed/ZettaLane/`
- **Ask questions of:** @crossmeta (ZettaLane review lead)

<details><summary>All 5 systems</summary>

- `closed/ZettaLane/systems/mayanas-lustre-gcp_c3hc176_c3d90_1c_4s.yaml` — 1 row
- `closed/ZettaLane/systems/mayanas-lustre-gcp_c4hc144_c3d90_1c_2s.yaml` — 2 rows
- `closed/ZettaLane/systems/mayanas-lustre-gcp_c4hc144_c3d90_2c_4s.yaml` — 1 row
- `closed/ZettaLane/systems/mayascale-gcp_c4hc144_n2hc64_1c_2s.yaml` — 1 row
- `closed/ZettaLane/systems/mayascale-gcp_c4hc192_n2hc64_1c_4s.yaml` — 1 row

</details>


### TTA

**Review lead:** @ByoungjunSeo

**Reviews 1 organization — 6 points (22% of a fair share).**

#### → TuringData — 4 rows, 2 systems, 6 points

- **Public IDs:** v3.0-0112 – v3.0-0115
- **Benchmarks:** Checkpointing 2, KVCache 1, Training 1
- **Submission tree:** `closed/TuringData/`
- **Ask questions of:** @xanturing (TuringData review lead)

<details><summary>All 2 systems</summary>

- `closed/TuringData/systems/TuringData_F9200_2_Clients.yaml` — 1 row
- `closed/TuringData/systems/TuringData_F9200_8_Clients.yaml` — 3 rows

</details>


### TuringData

**Review lead:** @xanturing

**Reviews 2 organizations — 6 points (22% of a fair share).**

#### → OpenLake — 2 rows, 2 systems, 4 points

- **Public IDs:** v3.0-0075 – v3.0-0076
- **Benchmarks:** Checkpointing 1, VectorDB 1
- **Submission tree:** `closed/OpenLake/`
- **Ask questions of:** @arnavbalyan (OpenLake review lead)

<details><summary>All 2 systems</summary>

- `closed/OpenLake/systems/openlake-hbv4-1c1s-final.yaml` — 1 row
- `closed/OpenLake/systems/openlake_hc44_1c1s.yaml` — 1 row

</details>

#### → Nutanix — 1 row, 1 system, 2 points

- **Public IDs:** v3.0-0180
- **Benchmarks:** KVCache 1
- **Submission tree:** `closed/Nutanix/`
- **Ask questions of:** @willo7734 (Nutanix review lead)

<details><summary>All 1 system</summary>

- `closed/Nutanix/systems/wsclient01.yaml` — 1 row

</details>


### UBIX

**Review lead:** @xutao00090

**Reviews 3 organizations — 28 points (101% of a fair share).**

#### → NewFW — 13 rows, 2 systems, 15 points

- **Public IDs:** v3.0-0062 – v3.0-0074
- **Benchmarks:** Checkpointing 8, KVCache 2, Training 2, VectorDB 1
- **Submission tree:** `closed/NewFW/`
- **Ask questions of:** @AjanZhong (NewFW review lead)

<details><summary>All 2 systems</summary>

- `closed/NewFW/systems/Solidigm_D5-P5336_61TB_Gen4_NVMe_QLC.yaml` — 6 rows
- `closed/NewFW/systems/Solidigm_D7-PS1010_7TB_Gen5_NVMe_TLC.yaml` — 7 rows

</details>

#### → SAMSUNG — 6 rows, 1 system, 7 points

- **Public IDs:** v3.0-0077 – v3.0-0082
- **Benchmarks:** Checkpointing 2, Training 2, KVCache 1, VectorDB 1
- **Submission tree:** `closed/SAMSUNG/`
- **Ask questions of:** @dhoon-4890 (SAMSUNG review lead)

<details><summary>All 1 system</summary>

- `closed/SAMSUNG/systems/MEMORY_AE.yaml` — 6 rows

</details>

#### → TuringData — 4 rows, 2 systems, 6 points

- **Public IDs:** v3.0-0112 – v3.0-0115
- **Benchmarks:** Checkpointing 2, KVCache 1, Training 1
- **Submission tree:** `closed/TuringData/`
- **Ask questions of:** @xanturing (TuringData review lead)

<details><summary>All 2 systems</summary>

- `closed/TuringData/systems/TuringData_F9200_2_Clients.yaml` — 1 row
- `closed/TuringData/systems/TuringData_F9200_8_Clients.yaml` — 3 rows

</details>


### XSKY

**Review lead:** @boyin-xsky

**Reviews 3 organizations — 29 points (104% of a fair share).**

#### → NewFW — 13 rows, 2 systems, 15 points

- **Public IDs:** v3.0-0062 – v3.0-0074
- **Benchmarks:** Checkpointing 8, KVCache 2, Training 2, VectorDB 1
- **Submission tree:** `closed/NewFW/`
- **Ask questions of:** @AjanZhong (NewFW review lead)

<details><summary>All 2 systems</summary>

- `closed/NewFW/systems/Solidigm_D5-P5336_61TB_Gen4_NVMe_QLC.yaml` — 6 rows
- `closed/NewFW/systems/Solidigm_D7-PS1010_7TB_Gen5_NVMe_TLC.yaml` — 7 rows

</details>

#### → HPE — 5 rows, 5 systems, 10 points

- **Public IDs:** v3.0-0149 – v3.0-0153
- **Benchmarks:** Checkpointing 2, Training 2, KVCache 1
- **Submission tree:** `closed/HPE/`
- **Ask questions of:** @leachkr (HPE review lead)

<details><summary>All 5 systems</summary>

- `closed/HPE/systems/K3000-kvcache.yaml` — 1 row
- `closed/HPE/systems/e2000-unet3d.yaml` — 1 row
- `closed/HPE/systems/e2000.yaml` — 1 row
- `closed/HPE/systems/k3000-unet3d.yaml` — 1 row
- `closed/HPE/systems/k3000.yaml` — 1 row

</details>

#### → OpenLake — 2 rows, 2 systems, 4 points

- **Public IDs:** v3.0-0075 – v3.0-0076
- **Benchmarks:** Checkpointing 1, VectorDB 1
- **Submission tree:** `closed/OpenLake/`
- **Ask questions of:** @arnavbalyan (OpenLake review lead)

<details><summary>All 2 systems</summary>

- `closed/OpenLake/systems/openlake-hbv4-1c1s-final.yaml` — 1 row
- `closed/OpenLake/systems/openlake_hc44_1c1s.yaml` — 1 row

</details>


### YanRongTech

**Review lead:** @limengran-yr

**Reviews 3 organizations — 28 points (101% of a fair share).**

#### → farmgpu — 9 rows, 6 systems, 15 points

- **Public IDs:** v3.0-0140 – v3.0-0146, v3.0-0178 – v3.0-0179
- **Benchmarks:** KVCache 6, Checkpointing 2, Training 1
- **Submission tree:** `closed/farmgpu/`, `open/farmgpu/`
- **Ask questions of:** @mrf512 (farmgpu review lead)

<details><summary>All 6 systems</summary>

- `closed/farmgpu/systems/hickory.yaml` — 4 rows
- `closed/farmgpu/systems/potato1-qlc-closed-tcm.yaml` — 1 row
- `closed/farmgpu/systems/potato8-qlc-closed-tcm.yaml` — 1 row
- `closed/farmgpu/systems/potato8-qlc-np2-closed-tcm.yaml` — 1 row
- `open/farmgpu/systems/potato8-qlc-np6-open-tnf-70b.yaml` — 1 row
- `open/farmgpu/systems/potato8-qlc-np6-open-tnf-u400.yaml` — 1 row

</details>

#### → XSKY — 6 rows, 4 systems, 10 points

- **Public IDs:** v3.0-0124 – v3.0-0129
- **Benchmarks:** Checkpointing 3, Training 3
- **Submission tree:** `closed/XSKY/`
- **Ask questions of:** @boyin-xsky (XSKY review lead)

<details><summary>All 4 systems</summary>

- `closed/XSKY/systems/XSKY_AIMesh_3StorageNode_1Client.yaml` — 1 row
- `closed/XSKY/systems/XSKY_AIMesh_3StorageNode_7Client.yaml` — 1 row
- `closed/XSKY/systems/XSKY_AIMesh_3StorageNode_8Client.yaml` — 3 rows
- `closed/XSKY/systems/XSKY_AIMesh_3StorageNode_9Client.yaml` — 1 row

</details>

#### → holmesai_limited — 2 rows, 1 system, 3 points

- **Public IDs:** v3.0-0147 – v3.0-0148
- **Benchmarks:** Training 2
- **Submission tree:** `closed/holmesai_limited/`
- **Ask questions of:** @kenzeng-China (holmesai_limited review lead)

<details><summary>All 1 system</summary>

- `closed/holmesai_limited/systems/StorMeshAI.yaml` — 2 rows

</details>


### ZettaLane

**Review lead:** @crossmeta

**Reviews 3 organizations — 23 points (83% of a fair share).**

#### → UBIX — 8 rows, 3 systems, 11 points

- **Public IDs:** v3.0-0116 – v3.0-0123
- **Benchmarks:** Checkpointing 4, Training 3, KVCache 1
- **Submission tree:** `closed/UBIX/`
- **Ask questions of:** @xutao00090 (UBIX review lead)

<details><summary>All 3 systems</summary>

- `closed/UBIX/systems/UbiPower18000_16x15.36TB_NVMe_4xNDR400_3xStorageNode_16hosts256GBMem.yaml` — 6 rows
- `closed/UBIX/systems/UbiPower18000_16x15.36TB_NVMe_4xNDR400_3xStorageNode_16hosts256GBMem_MI355.yaml` — 1 row
- `closed/UBIX/systems/UbiPower18000_16x15.36TB_NVMe_4xNDR400_3xStorageNode_1hosts256GBMem.yaml` — 1 row

</details>

#### → HPE — 5 rows, 5 systems, 10 points

- **Public IDs:** v3.0-0149 – v3.0-0153
- **Benchmarks:** Checkpointing 2, Training 2, KVCache 1
- **Submission tree:** `closed/HPE/`
- **Ask questions of:** @leachkr (HPE review lead)

<details><summary>All 5 systems</summary>

- `closed/HPE/systems/K3000-kvcache.yaml` — 1 row
- `closed/HPE/systems/e2000-unet3d.yaml` — 1 row
- `closed/HPE/systems/e2000.yaml` — 1 row
- `closed/HPE/systems/k3000-unet3d.yaml` — 1 row
- `closed/HPE/systems/k3000.yaml` — 1 row

</details>

#### → Nutanix — 1 row, 1 system, 2 points

- **Public IDs:** v3.0-0180
- **Benchmarks:** KVCache 1
- **Submission tree:** `closed/Nutanix/`
- **Ask questions of:** @willo7734 (Nutanix review lead)

<details><summary>All 1 system</summary>

- `closed/Nutanix/systems/wsclient01.yaml` — 1 row

</details>


### farmgpu

**Review lead:** @mrf512

**Reviews 2 organizations — 29 points (104% of a fair share).**

#### → Everpure — 11 rows, 8 systems, 19 points

- **Public IDs:** v3.0-0014 – v3.0-0023, v3.0-0177
- **Benchmarks:** Checkpointing 6, KVCache 3, Training 2
- **Submission tree:** `closed/Everpure/`, `open/Everpure/`
- **Ask questions of:** @lou-lydiksen-purestorage (Everpure review lead)

<details><summary>All 8 systems</summary>

- `closed/Everpure/systems/Everpure_FBEXA_file_32hosts_10-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 1 row
- `closed/Everpure/systems/Everpure_FBEXA_file_32hosts_15-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 1 row
- `closed/Everpure/systems/Everpure_FBEXA_file_32hosts_20-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 1 row
- `closed/Everpure/systems/Everpure_FBEXA_file_32hosts_30-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 3 rows
- `closed/Everpure/systems/Everpure_FBEXA_file_51hosts_20-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 2 rows
- `closed/Everpure/systems/Everpure_FBEXA_file_51hosts_30-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 2 rows
- `closed/Everpure/systems/Everpure_FBEXA_file_59-DN-DNOS-1.1.0-4845253c3899_50-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 1 row
- `open/Everpure/systems/Everpure_FBEXA_file_32hosts_30-DN-DNOS-1.1.0-4845253c3899_30-S500R2-blades-MDN-4.8.3.exa-4845253c.yaml` — 3 rows

</details>

#### → XSKY — 6 rows, 4 systems, 10 points

- **Public IDs:** v3.0-0124 – v3.0-0129
- **Benchmarks:** Checkpointing 3, Training 3
- **Submission tree:** `closed/XSKY/`
- **Ask questions of:** @boyin-xsky (XSKY review lead)

<details><summary>All 4 systems</summary>

- `closed/XSKY/systems/XSKY_AIMesh_3StorageNode_1Client.yaml` — 1 row
- `closed/XSKY/systems/XSKY_AIMesh_3StorageNode_7Client.yaml` — 1 row
- `closed/XSKY/systems/XSKY_AIMesh_3StorageNode_8Client.yaml` — 3 rows
- `closed/XSKY/systems/XSKY_AIMesh_3StorageNode_9Client.yaml` — 1 row

</details>


### holmesai_limited

**Review lead:** @kenzeng-China

**Reviews 2 organizations — 25 points (90% of a fair share).**

#### → Alluxio — 7 rows, 7 systems, 14 points

- **Public IDs:** v3.0-0007 – v3.0-0013
- **Benchmarks:** Training 4, Checkpointing 3
- **Submission tree:** `closed/Alluxio/`
- **Ask questions of:** @Stephen-Pu (Alluxio review lead)

<details><summary>All 7 systems</summary>

- `closed/Alluxio/systems/aws_c5n18xlarge_i3en24xlarge_8c_10s_8a.yaml` — 1 row
- `closed/Alluxio/systems/aws_c7i48xlarge_i3en12xlarge_1c_1s_32a.yaml` — 1 row
- `closed/Alluxio/systems/aws_c7i48xlarge_i3en12xlarge_1c_1s_8a.yaml` — 1 row
- `closed/Alluxio/systems/aws_m7i48xlarge_i3en12xlarge_32c_32s_512p.yaml` — 1 row
- `closed/Alluxio/systems/aws_r5n24xlarge_i3en12xlarge_1c_1s_8h.yaml` — 1 row
- `closed/Alluxio/systems/aws_r5n24xlarge_i3en12xlarge_4c_10s_64p.yaml` — 1 row
- `closed/Alluxio/systems/rigA_c5n18xl.yaml` — 1 row

</details>

#### → ZettaLane — 6 rows, 5 systems, 11 points

- **Public IDs:** v3.0-0134 – v3.0-0137, v3.0-0139, v3.0-0181
- **Benchmarks:** Training 3, Checkpointing 2, KVCache 1
- **Submission tree:** `closed/ZettaLane/`
- **Ask questions of:** @crossmeta (ZettaLane review lead)

<details><summary>All 5 systems</summary>

- `closed/ZettaLane/systems/mayanas-lustre-gcp_c3hc176_c3d90_1c_4s.yaml` — 1 row
- `closed/ZettaLane/systems/mayanas-lustre-gcp_c4hc144_c3d90_1c_2s.yaml` — 2 rows
- `closed/ZettaLane/systems/mayanas-lustre-gcp_c4hc144_c3d90_2c_4s.yaml` — 1 row
- `closed/ZettaLane/systems/mayascale-gcp_c4hc144_n2hc64_1c_2s.yaml` — 1 row
- `closed/ZettaLane/systems/mayascale-gcp_c4hc192_n2hc64_1c_4s.yaml` — 1 row

</details>


### HPE

**Review lead:** @leachkr

**Reviews 3 organizations — 25 points (90% of a fair share).**

#### → InspurData — 7 rows, 5 systems, 12 points

- **Public IDs:** v3.0-0024 – v3.0-0030
- **Benchmarks:** Checkpointing 3, KVCache 2, Training 2
- **Submission tree:** `closed/InspurData/`
- **Ask questions of:** @Dandy-yin (InspurData review lead)

<details><summary>All 5 systems</summary>

- `closed/InspurData/systems/InspurData_InDataOS_AS13000G7_10clients.yaml` — 2 rows
- `closed/InspurData/systems/InspurData_InDataOS_AS13000G7_10clients_checkpointing.yaml` — 1 row
- `closed/InspurData/systems/InspurData_InDataOS_AS13000G7_1client.yaml` — 1 row
- `closed/InspurData/systems/InspurData_InDataOS_AS13000G7_KH-50000_10clients.yaml` — 2 rows
- `closed/InspurData/systems/InspurData_InDataOS_AS13000G7_KH-50000_10clients_Unet3D.yaml` — 1 row

</details>

#### → SAMSUNG — 6 rows, 1 system, 7 points

- **Public IDs:** v3.0-0077 – v3.0-0082
- **Benchmarks:** Checkpointing 2, Training 2, KVCache 1, VectorDB 1
- **Submission tree:** `closed/SAMSUNG/`
- **Ask questions of:** @dhoon-4890 (SAMSUNG review lead)

<details><summary>All 1 system</summary>

- `closed/SAMSUNG/systems/MEMORY_AE.yaml` — 6 rows

</details>

#### → TTA — 5 rows, 1 system, 6 points

- **Public IDs:** v3.0-0107 – v3.0-0111
- **Benchmarks:** Checkpointing 2, KVCache 1, Training 1, VectorDB 1
- **Submission tree:** `closed/TTA/`
- **Ask questions of:** @ByoungjunSeo (TTA review lead)

<details><summary>All 1 system</summary>

- `closed/TTA/systems/seahorse-storage.yaml` — 5 rows

</details>


### nvidia

**Review lead:** @gaikwadabhishek

**Reviews 3 organizations — 29 points (104% of a fair share).**

#### → InspurData — 7 rows, 5 systems, 12 points

- **Public IDs:** v3.0-0024 – v3.0-0030
- **Benchmarks:** Checkpointing 3, KVCache 2, Training 2
- **Submission tree:** `closed/InspurData/`
- **Ask questions of:** @Dandy-yin (InspurData review lead)

<details><summary>All 5 systems</summary>

- `closed/InspurData/systems/InspurData_InDataOS_AS13000G7_10clients.yaml` — 2 rows
- `closed/InspurData/systems/InspurData_InDataOS_AS13000G7_10clients_checkpointing.yaml` — 1 row
- `closed/InspurData/systems/InspurData_InDataOS_AS13000G7_1client.yaml` — 1 row
- `closed/InspurData/systems/InspurData_InDataOS_AS13000G7_KH-50000_10clients.yaml` — 2 rows
- `closed/InspurData/systems/InspurData_InDataOS_AS13000G7_KH-50000_10clients_Unet3D.yaml` — 1 row

</details>

#### → UBIX — 8 rows, 3 systems, 11 points

- **Public IDs:** v3.0-0116 – v3.0-0123
- **Benchmarks:** Checkpointing 4, Training 3, KVCache 1
- **Submission tree:** `closed/UBIX/`
- **Ask questions of:** @xutao00090 (UBIX review lead)

<details><summary>All 3 systems</summary>

- `closed/UBIX/systems/UbiPower18000_16x15.36TB_NVMe_4xNDR400_3xStorageNode_16hosts256GBMem.yaml` — 6 rows
- `closed/UBIX/systems/UbiPower18000_16x15.36TB_NVMe_4xNDR400_3xStorageNode_16hosts256GBMem_MI355.yaml` — 1 row
- `closed/UBIX/systems/UbiPower18000_16x15.36TB_NVMe_4xNDR400_3xStorageNode_1hosts256GBMem.yaml` — 1 row

</details>

#### → TTA — 5 rows, 1 system, 6 points

- **Public IDs:** v3.0-0107 – v3.0-0111
- **Benchmarks:** Checkpointing 2, KVCache 1, Training 1, VectorDB 1
- **Submission tree:** `closed/TTA/`
- **Ask questions of:** @ByoungjunSeo (TTA review lead)

<details><summary>All 1 system</summary>

- `closed/TTA/systems/seahorse-storage.yaml` — 5 rows

</details>

---

## Review leads

| Organization | Review lead |
|---|---|
| Alluxio | @Stephen-Pu |
| Everpure | @lou-lydiksen-purestorage |
| InspurData | @Dandy-yin |
| Microsoft | @wolfgang-desalvador |
| Nebius | @oralzb |
| NewFW | @AjanZhong |
| Nutanix | @willo7734 |
| OpenLake | @arnavbalyan |
| SAMSUNG | @dhoon-4890 |
| Suzhou_Zishan_Longlin | @daddypig88 |
| TTA | @ByoungjunSeo |
| TuringData | @xanturing |
| UBIX | @xutao00090 |
| XSKY | @boyin-xsky |
| YanRongTech | @limengran-yr |
| ZettaLane | @crossmeta |
| farmgpu | @mrf512 |
| holmesai_limited | @kenzeng-China |
| HPE | @leachkr |
| nvidia | @gaikwadabhishek |

For the organizations that list more than one contact in
`.github/issue-notify-roster.json`, the lead above is the first name on that list
and should be **confirmed by the organization**:

- **NewFW** — lead @AjanZhong; also on the roster: @raysmond
- **SAMSUNG** — lead @dhoon-4890; also on the roster: @idevasena
- **UBIX** — lead @xutao00090; also on the roster: @yueyangubix, @bocellibin, @tylerqi007, @litianqi00315
- **farmgpu** — lead @mrf512; also on the roster: @malventano, @ereinha3, @lmacken, @jmhands
- **HPE** — lead @leachkr; also on the roster: @sakib-samar

## Who reviews whom

| Submission | Points | First reviewer | Second reviewer |
|---|---:|---|---|
| **Alluxio** | 14 | Suzhou_Zishan_Longlin | holmesai_limited |
| **Everpure** | 19 | SAMSUNG | farmgpu |
| **InspurData** | 12 | HPE | nvidia |
| **Microsoft** | 33 | Everpure | InspurData |
| **Nebius** | 28 | Microsoft | NewFW |
| **NewFW** | 15 | UBIX | XSKY |
| **Nutanix** | 2 | TuringData | ZettaLane |
| **OpenLake** | 4 | TuringData | XSKY |
| **SAMSUNG** | 7 | UBIX | HPE |
| **Suzhou_Zishan_Longlin** | 28 | Nebius | OpenLake |
| **TTA** | 6 | HPE | nvidia |
| **TuringData** | 6 | TTA | UBIX |
| **UBIX** | 11 | ZettaLane | nvidia |
| **XSKY** | 10 | YanRongTech | farmgpu |
| **YanRongTech** | 7 | Nutanix | SAMSUNG |
| **ZettaLane** | 11 | Suzhou_Zishan_Longlin | holmesai_limited |
| **farmgpu** | 15 | Nutanix | YanRongTech |
| **holmesai_limited** | 3 | Microsoft | YanRongTech |
| **HPE** | 10 | XSKY | ZettaLane |
| **nvidia** | 37 | Alluxio | *(none — ANL withdrew)* |

## Load balance

| Reviewer | Organizations reviewed | Points | %% of fair share |
|---|---|---:|---:|
| Alluxio | nvidia | 37 | 133% |
| Everpure | Microsoft | 33 | 119% |
| InspurData | Microsoft | 33 | 119% |
| Microsoft | Nebius, holmesai_limited | 31 | 112% |
| XSKY | NewFW, OpenLake, HPE | 29 | 104% |
| farmgpu | Everpure, XSKY | 29 | 104% |
| nvidia | InspurData, TTA, UBIX | 29 | 104% |
| Nebius | Suzhou_Zishan_Longlin | 28 | 101% |
| NewFW | Nebius | 28 | 101% |
| OpenLake | Suzhou_Zishan_Longlin | 28 | 101% |
| UBIX | NewFW, SAMSUNG, TuringData | 28 | 101% |
| YanRongTech | XSKY, farmgpu, holmesai_limited | 28 | 101% |
| SAMSUNG | Everpure, YanRongTech | 26 | 94% |
| Suzhou_Zishan_Longlin | Alluxio, ZettaLane | 25 | 90% |
| holmesai_limited | Alluxio, ZettaLane | 25 | 90% |
| HPE | InspurData, SAMSUNG, TTA | 25 | 90% |
| ZettaLane | Nutanix, UBIX, HPE | 23 | 83% |
| Nutanix | YanRongTech, farmgpu | 22 | 79% |
| TTA | TuringData | 6 | 22% |
| TuringData | Nutanix, OpenLake | 6 | 22% |

Alluxio, at the top of the table, reviews `nvidia` and nothing else. `nvidia` is a
single 37-point unit against a 27.8-point fair share, so it cannot be brought under
100% without splitting one organization across two reviewers — which this scheme
deliberately does not do. It had a second reviewer, ANL, until that organization
withdrew; the assignment has not been rebalanced around the withdrawal, which is
also why TTA and TuringData sit at the bottom of the table.

## Filing what you find

Use the issue forms described in [IssueManagement.md](IssueManagement.md):
**Question about a submission** if you need the other organization to clarify
something, **Potential flaw in a submission** if you believe something is wrong.
Set **From** to your organization and **To** to the one you are reviewing; labels
and notifications are applied automatically.

Direct anything about the rules, the tooling, or the review process itself to
**ReviewChairs** rather than to another submitter.
