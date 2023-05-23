package main

import "fmt"

func BSI(a []int, key int) int {
	l := 0
	r := len(a)
	for l <= r {
		m := (l + r) / 2
		if key == a[m] {
			return m
		} else if key < a[m] {
			r = m - 1
		} else if key > a[m] {
			l = l + 1
		}
	}
	return -1
}

func main() {
	a := []int{25, 36, 45, 56, 67, 78, 89, 99}
	fmt.Println("result", BSI(a, 20))
}
