package main

import "fmt"

func binaryiteratirve(A []int, key int) int {
	l := 0
	r := len(A)
	for l <= r {
		m := (l + r) / 2
		if key == A[m] {
			return m
		} else if key < A[m] {
			r = m - 1
		} else if key > A[m] {
			l = l + 1
		}
	}
	return -1
}

func main() {
	A := []int{25, 36, 99, 65, 33, 258}
	fmt.Println(binaryiteratirve(A, 258))
}
