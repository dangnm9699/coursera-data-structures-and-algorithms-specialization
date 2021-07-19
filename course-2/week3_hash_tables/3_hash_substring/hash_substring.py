# python3

def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def hash(s, p, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % p
    return ans % p


def precompute_hash(text, len_pattern, p, x):
    H = [0]*(len(text)-len_pattern + 1)
    s = text[len(text)-len_pattern:]
    H[len(text)-len_pattern] = hash(s, p, x)
    y = 1
    for i in range(len_pattern):
        y = (y * x) % p
    for i in range(len(text)-len_pattern - 1, -1, -1):
        H[i] = (x * H[i+1] + ord(text[i]) - y*ord(text[i+len_pattern])) % p
    return H


def get_occurrences(pattern, text):
    p = 10000007
    x = 163
    res = []
    H = precompute_hash(text, len(pattern), p, x)
    p_hash = hash(pattern, p, x)
    for i in range(len(text)-len(pattern) + 1):
        if p_hash != H[i]:
            continue
        if text[i:i+len(pattern)] == pattern:
            res.append(i)
    return res


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
