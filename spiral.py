
def dirs():
    d = 1j
    i = 0
    while i := i + 1:
        d *= -1j
        yield from ((int(d.imag), int(d.real)), ) * (i//2)


def main():
    a = 5
    m = [[0 for _ in range(a)] for _ in range(a)]
    x = y = a//2
    for n, (dx, dy) in zip(range(num := a**2), dirs()):
        m[x][y] = n
        x, y = x+dx, y+dy

    w = len(str(num))
    print(*(' '.join((str(n).ljust(w) for n in r)) for r in m), sep='\n')


if __name__ == '__main__':
    main()
