# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    segments.sort()
    points = []
    # write your code here
    cur_seg = segments[0]
    for s in segments[1:]:
        if cur_seg.end >= s.start:
            start = s.start
            end = min(s.end, cur_seg.end)
            cur_seg = Segment(start, end)
        else:
            points.append(cur_seg.start)
            cur_seg = s
    points.append(cur_seg.start)
    return points


if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        a, b = map(int, input().split())
        segments.append(Segment(a, b))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
