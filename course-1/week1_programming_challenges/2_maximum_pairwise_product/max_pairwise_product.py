# python3


def max_pairwise_product(numbers):
    numbers = sorted(numbers)

    return numbers[-1]*numbers[-2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
