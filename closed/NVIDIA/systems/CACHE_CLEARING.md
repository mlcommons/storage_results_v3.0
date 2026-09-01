# NVIDIA AIStore checkpoint cache-clearing disclosure

All checkpoint results in this package that required a client cache flush used
the two-invocation CLOSED workflow from MLPerf Storage Rules section 4.7.1.

For each workload:

1. `mlpstorage` completed a write-only invocation with 10 checkpoint writes and
   zero reads.
2. After the write invocation exited, the following command completed on every
   participating benchmark client:

   `sudo -n sh -c 'sync; echo 3 > /proc/sys/vm/drop_caches'`

3. `mlpstorage` then completed a read-only invocation against the same 10
   checkpoints with zero writes.

No checkpoint write or measured checkpoint read overlapped the client cache
boundary. AIStore remained continuously available with the submitted
configuration throughout each paired invocation. The validator-generated
`results.json` under each workload records the paired invocation structure and
measured inter-phase gap; every included pair is below the 30-second CLOSED
limit.

The included configurations are:

| System | Workload(s) | Clients | Ranks | Placement |
|---|---|---:|---:|---|
| `aistore-3n-oci-bm-denseio-e5-128-1client` | Llama3 8B | 1 | 8 | 8 ranks/client |
| `aistore-3n-oci-bm-denseio-e5-128-8client` | Llama3 70B | 8 | 64 | 8 ranks/client |
| `aistore-3n-oci-bm-denseio-e5-128-8client-405b-1t` | Llama3 405B, 1T | 8 | 512 / 1,024 | 64 / 128 ranks/client |
| `aistore-6n-oci-bm-denseio-e5-128-1client` | Llama3 8B | 1 | 8 | 8 ranks/client |
| `aistore-6n-oci-bm-denseio-e5-128-8client` | Llama3 70B | 8 | 64 | 8 ranks/client |
| `aistore-6n-oci-bm-denseio-e5-128-8client-405b-1t` | Llama3 405B, 1T | 8 | 512 / 1,024 | 64 / 128 ranks/client |
| `aistore-12n-oci-bm-denseio-e5-128-1client` | Llama3 8B | 1 | 8 | 8 ranks/client |
| `aistore-12n-oci-bm-denseio-e5-128-8client` | Llama3 70B | 8 | 64 | 8 ranks/client |
| `aistore-12n-oci-bm-denseio-e5-128-16client` | Llama3 405B, 1T | 16 | 512 / 1,024 | 32 / 64 ranks/client |
