# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def heapify(free_time, workers, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and free_time[smallest] > free_time[left]:
        smallest = left
    if right < n and free_time[smallest] > free_time[right]:
        smallest = right
    if left < n and free_time[smallest] == free_time[left] and workers[smallest] > workers[left]:
        smallest = left
    if right < n and free_time[smallest] == free_time[right] and workers[smallest] > workers[right]:
        smallest = right
    if smallest != i:
        # swap
        free_time[i], free_time[smallest] = free_time[smallest], free_time[i]
        workers[i], workers[smallest] = workers[smallest], workers[i]
        heapify(free_time, workers, n, smallest)


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    workers = [x for x in range(n_workers)]
    next_free_time = [0] * n_workers
    for job in jobs:
        result.append(AssignedJob(workers[0], next_free_time[0]))
        next_free_time[0] += job
        heapify(next_free_time, workers, n_workers, 0)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
