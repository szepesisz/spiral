
def dirs():
    d = 1j
    i = 0
    while i := i + 1:
        d *= -1j
        yield from ((int(d.imag), int(d.real)) for _ in range(i//2))


def main():
    num = 25

    assert (a := num ** 0.5).is_integer()
    a = int(a)

    m = [[0 for _ in range(a)] for _ in range(a)]
    x = y = a//2
    for n, (dx, dy) in zip(range(num), dirs()):
        m[x][y] = n
        x += dx
        y += dy

    w = len(str(num))
    for r in m:
        print(*(str(n).ljust(w) for n in r))


if __name__ == '__main__':
    main()
