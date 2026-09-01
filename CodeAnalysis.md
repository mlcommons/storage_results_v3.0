# Code Image Analysis — MLPerf Storage v3.0 Submissions

*Prepared by MLPerf Storage review staff, 2026-07-28.*

## Summary

Every one of the 78 code images in this tree fails the `CHECK-02
poolImageSelfConsistency` re-hash check. This document explains why, and what
a full byte-level audit of all 78 images found.

**Conclusion up front: there is no evidence that any submitter tampered with
benchmark code.** The universal hash failure is a mechanical artifact of
upload preparation: a single file (`CLAUDE.md`, a coding-agent configuration
file with no effect on benchmark execution) was removed from every code image
before the tree was pushed to GitHub. Of the 69 images whose recorded git SHA
exists in `mlcommons/storage`, 60 are byte-identical to their upstream release
in every remaining file, and the other 9 contain a small number of local
modifications — all of which are enumerated below and are harness
bug-workarounds, HPC portability fixes, dependency-pin changes, a
package-mirror substitution, or performance tuning of a submitter-tunable
parameter. None touch measurement, timing, or reporting logic in a way that
could inflate results.

This is a re-run of the audit over the fuller tree: ANL and OpenLake have
since been added, and Everpure's submission was extended, bringing the pool
from 65 images to 78.

## Background: code images and CHECK-02

Each submission run records the exact benchmark tree it executed from. The
tree is copied into a content-addressed pool directory
(`<org>/code-<hash8>/`), together with a `.code-hash.json` file recording:

- `hash` — an MD5 digest (`md5-tree-v2`) over the sorted list of
  (relative path, file content) pairs, excluding VCS/IDE/agent runtime
  directories, caches, and test directories;
- `git_sha` — the upstream `mlcommons/storage` commit the tree was based on;
- `mlpstorage_version`, `captured_at`.

`CHECK-02` verifies (1) the directory name matches the recorded hash and
(2) the directory contents re-hash to the recorded digest. It is a
*self-consistency* check: it proves the uploaded image is exactly what was
captured on the submitter's machine — including any local modifications the
submitter had made, which are legitimate to capture and are surfaced for
review precisely this way.

## Why every image fails: the stripped `CLAUDE.md`

During preparation of this consolidated tree for GitHub, `CLAUDE.md` was
removed from the code images. `CLAUDE.md` is tracked in `mlcommons/storage`
at every recorded `git_sha` and is **not** in the hash-exclusion list, so it
was part of every capture-time hash. Removing it after capture guarantees the
re-hash fails.

The audit confirmed this is the *only* file missing from the tracked file set
in every comparable image (69 of 69), and that **0 of the 78 images** still
contain a `CLAUDE.md`.

## Audit method

For each of the 78 images:

1. **File-set comparison** — walk the image with the exact `md5-tree-v2`
   predicates and diff the surviving file list against `git ls-tree -r
   <git_sha>` of `mlcommons/storage`, filtered by the same predicates.
2. **Repair test** — recompute the tree hash with the missing files' content
   taken from git at the recorded SHA, merged into the sorted walk. If the
   repaired hash equals the recorded hash **bit-for-bit**, the stripped file
   fully explains the failure and every other byte of the image is proven
   pristine.
3. **Per-file content comparison** — for every surviving file, compare its
   git-blob SHA1 against the upstream blob at the recorded SHA, naming any
   file whose content differs from the upstream release.

## Findings

### Integrity of the upload (vs. each image's own recorded hash)

| Category | Count | Meaning |
|---|---|---|
| Verified intact | 29 | Restoring the upstream `CLAUDE.md` at the recorded SHA reproduces the recorded MD5 **bit-for-bit**. Everything the submitter captured survived upload unchanged. |
| Intact except `CLAUDE.md` | 40 | Every surviving file verified byte-identical to the upstream release (or enumerated under *Local modifications*); the repair test fails only because the capture-time `CLAUDE.md` had been locally customized, and that content was lost when the file was stripped. |
| Not comparable | 9 | The recorded `git_sha` does not exist in `mlcommons/storage` (fork or local commits), so no upstream reference is available. These images also lack `CLAUDE.md`. |

Note that the two axes are independent: *Verified intact* means the upload
preserved exactly what the submitter captured, which for a locally-modified
image includes the modification. Three images carry both a "verified intact"
verdict and a local-modification note.

### Content vs. the upstream release (did submitters modify the benchmark?)

Of the 69 comparable images: **60 match the upstream release exactly** in
every surviving file; **9 contain local modifications**, detailed in the next
section. For the 9 non-comparable images no statement can be made either way.

### Per-image results

| Org | Image | Tool ver. | Verdict |
|---|---|---|---|
| Alluxio | code-4a3ce79d | 3.0.37 | Intact except CLAUDE.md |
| Alluxio | code-5d45230a | 3.0.28 | Verified intact |
| Alluxio | code-b64876ed | 3.0.37 | Verified intact |
| Alluxio | code-d2006d80 | 3.0.42 | Verified intact |
| Alluxio | code-eca34694 | 3.0.37 | Verified intact |
| ANL | code-ba731d56 | 3.0.46 | Verified intact; locally modified (§ANL) |
| ANL | code-fe4d097a | 3.0.46 | Verified intact |
| Everpure | code-206c50e8 | 3.0.46 | Verified intact |
| Everpure | code-3f76af5d | 3.0.42 | Verified intact |
| Everpure | code-4023b6bc | 3.0.42 | Verified intact |
| Everpure | code-5d4e9e92 | 3.0.43 | Verified intact |
| Everpure | code-7c647a56 | 3.0.42 | Verified intact |
| Everpure | code-87df32cb | 3.0.43 | Intact except CLAUDE.md |
| Everpure | code-a7ada398 | 3.0.44 | Verified intact |
| Everpure | code-f263abdd | 3.0.42 | Intact except CLAUDE.md |
| Everpure | code-fd7d946d | 3.0.46 | Verified intact |
| farmgpu | code-37ce6a8b | 3.0.46 | Not comparable (SHA not upstream) |
| farmgpu | code-da417e70 | 3.0.46 | Not comparable (SHA not upstream) |
| farmgpu | code-e5ee7070 | 3.0.46 | Not comparable (SHA not upstream) |
| farmgpu | code-eb95104a | 3.0.46 | Not comparable (SHA not upstream) |
| farmgpu | code-f1b36da9 | 3.0.37 | Intact except CLAUDE.md |
| holmesai_limited | code-56d13410 | 3.0.37 | Intact except CLAUDE.md; locally modified (§holmesai) |
| holmesai_limited | code-d8b126b5 | 3.0.42 | Intact except CLAUDE.md; locally modified (§holmesai) |
| HPE | code-1c717832 | 3.0.46 | Intact except CLAUDE.md; locally modified (§HPE) |
| HPE | code-69d7248b | 3.0.46 | Intact except CLAUDE.md; locally modified (§HPE) |
| HPE | code-73abf5ff | 3.0.38 | Intact except CLAUDE.md |
| HPE | code-c7eb110c | 3.0.38 | Not comparable (SHA not upstream) |
| HPE | code-e5d01e30 | 3.0.46 | Intact except CLAUDE.md |
| InspurData | code-fe4d097a | 3.0.46 | Not comparable (SHA not upstream) |
| Microsoft | code-4023b6bc | 3.0.42 | Verified intact |
| Nebius | code-46ae7904 | 3.0.46 | Intact except CLAUDE.md |
| Nebius | code-5d4e9e92 | 3.0.43 | Verified intact |
| Nebius | code-d4484ca8 | 3.0.42 | Intact except CLAUDE.md |
| Nebius | code-e1dc9e2c | 3.0.45 | Verified intact |
| Nebius | code-fe4d097a | 3.0.46 | Verified intact |
| NewFW | code-036406a0 | 3.0.44 | Intact except CLAUDE.md |
| NewFW | code-19613128 | 3.0.42 | Intact except CLAUDE.md |
| nvidia | code-092bc506 | 3.0.46 | Intact except CLAUDE.md |
| nvidia | code-1312df84 | 3.0.36 | Intact except CLAUDE.md |
| nvidia | code-3528112e | 3.0.40 | Intact except CLAUDE.md |
| nvidia | code-3a9a7bf3 | 3.0.46 | Intact except CLAUDE.md |
| nvidia | code-4578162a | 3.0.46 | Intact except CLAUDE.md |
| nvidia | code-48676b4f | 3.0.40 | Intact except CLAUDE.md |
| nvidia | code-666dead1 | 3.0.40 | Intact except CLAUDE.md |
| nvidia | code-673d4726 | 3.0.44 | Intact except CLAUDE.md |
| nvidia | code-684dafcb | 3.0.46 | Intact except CLAUDE.md |
| nvidia | code-7eb38695 | 3.0.40 | Intact except CLAUDE.md; locally modified (§NVIDIA) |
| nvidia | code-960b6dbc | 3.0.40 | Intact except CLAUDE.md |
| nvidia | code-98929eb5 | 3.0.40 | Intact except CLAUDE.md |
| nvidia | code-d9ad28df | 3.0.40 | Intact except CLAUDE.md |
| nvidia | code-f9327d87 | 3.0.46 | Intact except CLAUDE.md |
| OpenLake | code-05a915c8 | 3.0.46 | Verified intact |
| OpenLake | code-206c50e8 | 3.0.46 | Verified intact |
| OpenLake | code-ea355a28 | 3.0.46 | Intact except CLAUDE.md |
| SAMSUNG | code-08dbf816 | 3.0.42 | Intact except CLAUDE.md; locally modified (§SAMSUNG) |
| Suzhou_Zishan_Longlin | code-3f76af5d | 3.0.42 | Verified intact |
| Suzhou_Zishan_Longlin | code-66eac40f | 3.0.40 | Verified intact |
| Suzhou_Zishan_Longlin | code-703c0c17 | 3.0.41 | Verified intact |
| Suzhou_Zishan_Longlin | code-959c6bc5 | 3.0.43 | Verified intact |
| Suzhou_Zishan_Longlin | code-d2006d80 | 3.0.42 | Verified intact |
| Suzhou_Zishan_Longlin | code-df323474 | 3.0.46 | Intact except CLAUDE.md |
| Suzhou_Zishan_Longlin | code-eca34694 | 3.0.38 | Verified intact |
| Suzhou_Zishan_Longlin | code-fb66ae73 | 3.0.46 | Intact except CLAUDE.md |
| Suzhou_Zishan_Longlin | code-fe4d097a | 3.0.46 | Verified intact |
| TTA | code-1bc6c941 | 3.0.38 | Intact except CLAUDE.md |
| TTA | code-7c1ce38a | 3.0.45 | Intact except CLAUDE.md |
| TTA | code-9c126335 | 3.0.45 | Intact except CLAUDE.md |
| TTA | code-9cacf3b9 | 3.0.45 | Intact except CLAUDE.md |
| TuringData | code-73ec291b | 3.0.46 | Intact except CLAUDE.md |
| UBIX | code-fe4d097a | 3.0.46 | Verified intact |
| XSKY | code-4e4e4e66 | 3.0.46 | Not comparable (SHA not upstream) |
| XSKY | code-fc90a592 | 3.0.46 | Not comparable (SHA not upstream) |
| YanRongTech | code-73ec291b | 3.0.46 | Intact except CLAUDE.md |
| ZettaLane | code-10e15398 | 3.0.35 | Intact except CLAUDE.md; locally modified (§ZettaLane) |
| ZettaLane | code-6b0262ba | 3.0.23 | Verified intact; locally modified (§ZettaLane) |
| ZettaLane | code-ca5fe47d | 3.0.24 | Intact except CLAUDE.md |
| ZettaLane | code-d1142bf2 | 3.0.31 | Verified intact |
| ZettaLane | code-e0482096 | 3.0.2 | Not comparable (SHA not upstream) |

## Local modifications in detail

Nine images differ from their upstream release in files other than
`CLAUDE.md`. In every case the image is self-consistent with its own
recorded hash (the modifications were present at capture time and hashed —
exactly what the code-image mechanism is designed to record). Categorized:

### ANL — HPC launcher and CPU-affinity portability (1 of 2 images)

`code-ba731d56` modifies `mlpstorage_py/checkpointing/streaming_checkpoint.py`
in two places, both concerned with sizing the dgen worker pool correctly on
ALCF machines:

- adds `PALS_LOCAL_SIZE` and `PMI_LOCAL_SIZE` to the list of environment
  variables consulted for ranks-per-node. Upstream recognizes only the
  OpenMPI / MPICH / MVAPICH2 variables; ALCF Aurora and Sunspot launch via
  HPE PALS / Cray PMI, where none of those are set and the count silently
  falls back to a default.
- clamps the thread count to `os.sched_getaffinity(0)` in addition to
  `total_cpus // local_ranks`, so a rank launched under `--cpu-bind
  list/depth` does not spawn more generator threads than the cores it is
  pinned to.

Both are resource-sizing fixes for the job launcher; neither alters what is
generated, measured or timed. The image also carries a
`streaming_checkpoint.py.bak.20260723_025516` backup file, which the audit
confirmed is **byte-identical to the upstream original** — it was captured
alongside the edit, and is not a separate discrepancy.

### SAMSUNG — workload-parameter tuning (1 image)

`code-08dbf816` modifies two DLIO workload templates, changing only
`reader.read_threads`:

- `configs/dlio/workload/unet3d_b200.yaml`: `read_threads: 4` → `32`
- `configs/dlio/workload/retinanet_b200.yaml`: `read_threads: 8` → `4`

`read_threads` is a host-tunable I/O parallelism knob. The change was made by
editing the shipped template rather than via CLI override; the effective
value is also recorded in each run's metadata, where the rules checks
evaluate it.

### NVIDIA — object-store portability fixes (1 of 14 images)

`code-7eb38695` modifies two harness files:

- `mlpstorage_py/benchmarks/dlio.py`: adds a `_dataset_root_location()`
  helper so `--data-dir` resolves to the real object-store URI
  (`s3://`/`direct://` etc.) when `storage.storage_type` is not `local`, and
  writes run metadata before an in-run datagen leaf check that would
  otherwise fail (upstream writes it only after the run returns).
- `mlpstorage_py/rules/datagen_hierarchy.py`: wraps three dataset parameters
  in `int(...)` to tolerate string-typed values.

Both are portability/bug workarounds for object-storage submissions
(AIStore). NVIDIA's other 13 images match upstream exactly.

### ZettaLane — MPI launcher and kv-cache harness fixes (2 images)

- `code-10e15398` / `code-6b0262ba`, `mlpstorage_py/utils.py`: drops or
  conditions the `--npernode` flag in the generated `mpirun` prefix — on
  OpenMPI 5.x it auto-translates to `--map-by ppr:N:node`, which conflicts
  with the explicit `--map-by socket` the harness also emits. The rank
  layout is already fully specified by `-n N -host host:N`.
- `code-6b0262ba`, `kv_cache_benchmark/kv_cache/benchmark.py`: hoists a
  `cache_stats` assignment out of a block that an upstream commit had
  accidentally swallowed into a docstring, restoring the summary print
  statements. (Fixes a genuine upstream defect in that release.)

### HPE — dependency pin (2 images)

`code-1c717832` / `code-69d7248b`: `pyproject.toml` moves the
`dlio-benchmark` git pin to a newer `DLIO_local_changes` revision
(`edaf4bb3` → `86945a7a`), with the matching `uv.lock` regeneration. A stray
editor backup (`pyproject.toml.bak`) is also present — it is untracked
upstream and was captured with the image, which is why it appears; it is not
a discrepancy.

### holmesai_limited — package-mirror substitution (2 images)

`code-56d13410` / `code-d8b126b5`: `uv.lock` only. Every package URL is
rewritten from `pypi.org` / `files.pythonhosted.org` to the Tsinghua
University PyPI mirror (`pypi.tuna.tsinghua.edu.cn`). **The package
`sha256` hashes are unchanged**, so the installed artifacts are identical —
this is a network-locality change, not a dependency change.

## Files present in images but not upstream

Three images carry a file that has no upstream counterpart. None modifies
tracked benchmark code; all were present at capture time and are part of the
recorded hash.

- **OpenLake** `code-05a915c8` and `code-ea355a28` —
  `vdb_benchmark/stacks/milvus/standalone/s3/docker-compose.override.yml`,
  a Docker Compose overlay binding the etcd and Milvus data volumes to
  `/mnt/vdb/...` (the storage under test) and, in `code-ea355a28`, raising
  the `nofile` ulimit for both services. This is deployment configuration
  pointing the vector database at the system being benchmarked, which is
  what a VDB submission is expected to supply. The two overlays differ from
  each other, consistent with two distinct system configurations.
- **ANL** `code-ba731d56` and **HPE** `code-1c717832` / `code-69d7248b` —
  editor backup files, described in their sections above.

## Conclusion

- The universal `CHECK-02` failure is fully explained by the removal of
  `CLAUDE.md` during upload preparation. For 29 images this is proven
  bit-for-bit; for the remaining comparable images, every surviving file was
  independently verified against the upstream release.
- The 9 locally-modified images contain harness bug-workarounds, HPC
  launcher and CPU-affinity portability fixes, dependency pins, a
  package-mirror substitution, and one tunable-parameter change.
  Nothing observed alters measurement, timing, or result reporting.
- No action is required from submitters. The `CHECK-02` errors in
  `mlpstorage validate` output for this tree can be read with this document
  as context.
