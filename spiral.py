
def c_tup(z):
    return int(z.imag), int(z.real)


def dirs():
    i = 0
    while i := i+1:
        yield from i//2 * (c_tup(1j**i), )


def spiral(a):
    m = [[0 for _ in range(a)] for _ in range(a)]
    x = y = a//2
    for n, (dx, dy) in zip(range(num := a**2), dirs()):
        m[x][y] = n
        x, y = x+dx, y+dy

    w = len(str(num))
    print(*(' '.join(str(n).ljust(w) for n in r) for r in m), sep='\n')


def main():
    spiral(5)
    spiral(4)


if __name__ == '__main__':
    main()

