# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    n = len(data)
    for i in range(n//2-1, -1, -1):
        largest = i
        while True:
            _largest = largest
            left = 2 * largest + 1
            right = 2 * largest + 2
            if left < n and data[_largest] > data[left]:
                _largest = left
            if right < n and data[_largest] > data[right]:
                _largest = right
            if _largest != largest:
                data[largest], data[_largest] = data[_largest], data[largest]
                swaps.append((largest, _largest))
                largest = _largest
            else:
                break

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
