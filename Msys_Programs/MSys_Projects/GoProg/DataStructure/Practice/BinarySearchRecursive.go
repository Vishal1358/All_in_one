package main

import "fmt"

func BSR(a []int, key, l, r int) int {
	if l > r {
		return -1
	} else {
		mid := (l + r) / 2
		if key == a[mid] {
			return mid
		} else if key < a[mid] {
			return BSR(a, key, l, mid-1)
		} else if key > a[mid] {
			return BSR(a, key, mid+1, r)
		}
	}
	return 0
}
func main() {
	a := []int{25, 36, 45, 56, 67, 78, 79, 88, 99, 111, 222}
	l := len(a)
	f := BSR(a, 220, 0, l)
	fmt.Println("result :", f)
}
