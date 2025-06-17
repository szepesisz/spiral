
def c_tup(z):
    return int(z.imag), int(z.real)


def dirs(a):
    yield from sum(((i//2 * (c_tup(1j**i), )) for i in range(1, 2*a+1)), start=())


def spiral(a):
    m = [[0 for _ in range(a)] for _ in range(a)]
    x = y = a//2
    for n, (dx, dy) in enumerate(dirs(a)):
        m[x][y] = n
        x, y = x+dx, y+dy

    w = len(str(a**2))
    print(*(' '.join(str(n).ljust(w) for n in r) for r in m), sep='\n')


def main():
    spiral(5)
    spiral(4)


if __name__ == '__main__':
    main()

