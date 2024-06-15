
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
    pos = a//2, a//2
    d = dirs()
    for n in range(num):
        x, y = pos
        m[x][y] = n
        dx, dy = next(d)
        pos = x+dx, y+dy

    w = len(str(num))
    for r in m:
        print(*(str(n).ljust(w) for n in r))


if __name__ == '__main__':
    main()
