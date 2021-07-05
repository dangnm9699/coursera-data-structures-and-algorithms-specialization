# python3
from collections import deque


def max_sliding_window_naive(sequence, m):
    maximums = []
    deq = deque()
    for i in range(m):
        while deq and sequence[i] >= sequence[deq[-1]]:
            deq.pop()
        deq.append(i)
    for i in range(m, len(sequence)):
        maximums.append(sequence[deq[0]])
        while deq and deq[0] <= i-m:
            deq.popleft()
        while deq and sequence[i] >= sequence[deq[-1]]:
            deq.pop()
        deq.append(i)
    maximums.append(sequence[deq[0]])
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
