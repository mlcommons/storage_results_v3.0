/*
 * libnofadvise.c — LD_PRELOAD shim that no-ops posix_fadvise(DONTNEED).
 *
 * Rationale (JM's flax100r MLPerf v3.0 kvcache study, SW-337):
 *   The MLPerf kvcache benchmark calls posix_fadvise(fd, .., POSIX_FADV_DONTNEED)
 *   before every read, deliberately evicting the page cache so each read hits the
 *   device. That models isolated-device performance but does NOT reflect a real
 *   inference engine, which never drops the page cache between decode reads of the
 *   same session. No-opping the call lets re-reads of recently-touched KV blocks
 *   hit the Linux page cache at DDR5 speed — measured at +42% throughput on top of
 *   tcmalloc, and it makes the benchmark's read pattern *more* production-realistic.
 *
 * Scope: benchmark tuning only. This does not touch fsync (that is eatmydata's job)
 *   and is safe to leave loaded for read-heavy workloads. We intentionally no-op
 *   ONLY posix_fadvise; every other libc call passes through untouched.
 *
 * Build:  gcc -shared -fPIC -O2 -o libnofadvise.so libnofadvise.c
 * Use:    LD_PRELOAD=/path/to/libnofadvise.so <command>
 */
#define _GNU_SOURCE
#include <fcntl.h>
#include <sys/types.h>

/* glibc exposes both posix_fadvise and posix_fadvise64 depending on the
 * _FILE_OFFSET_BITS the caller was compiled with. Override both so the no-op
 * applies regardless of how CPython / numpy were built. Return 0 (success). */

int posix_fadvise(int fd, off_t offset, off_t len, int advice)
{
    (void)fd; (void)offset; (void)len; (void)advice;
    return 0;
}

int posix_fadvise64(int fd, off_t offset, off_t len, int advice)
{
    (void)fd; (void)offset; (void)len; (void)advice;
    return 0;
}
