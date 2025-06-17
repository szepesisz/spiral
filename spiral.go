package main

import (
	"fmt"
	"math/cmplx"
	"strconv"
	"strings"
)

func dirs(a int) [][2]int {
	dirs := make([][2]int, a*a)
	c := 0
	z := complex(0, 0)
	d := [2]int{}
	for i := 1; i < 2*a+1; i++ {
		z = cmplx.Pow(1i, complex(float64(i), 0))
		d = [2]int{int(imag(z)), int(real(z))}
		for range i / 2 {
			dirs[c] = d
			c++
		}
	}
	return dirs
}

func spiral(a int) {
	b := make([][]int, a)
	for r := range a {
		b[r] = make([]int, a)
	}

	x, y := a/2, a/2
	for n, d := range dirs(a) {
		b[y][x] = n
		x += d[0]
		y += d[1]
	}
	wl := strconv.Itoa(len(strconv.Itoa(a*a)))
	for _, r := range b {
		s := make([]string, a)
		for i, v := range r {
			s[i] = fmt.Sprintf("%" + wl + "d", v)
		}
		fmt.Println(strings.Join(s, " "))
	}
}

func main() {
	spiral(5)
	spiral(4)
}
