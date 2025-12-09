def ok(a, r, c):
    for i in range(r):
        if a[i] == c or abs(a[i] - c) == abs(i - r):
            return False
    return True


def solve(r, a):
    if r == 8:
        print(a)
        return

    for c in range(8):
        if ok(a, r, c):
            a[r] = c
            solve(r + 1, a)


a = [0] * 8
solve(0, a)