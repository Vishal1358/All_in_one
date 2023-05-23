package main

import "fmt"

func LS(a []int, key int) int {
	index := 0
	for index < len(a) {
		if key == a[index] {
			return index
		}
		index = index + 1
	}
	return -1
}

func main() {
	a := []int{22, 33, 44, 55, 66, 77, 88, 99}
	fmt.Println("result:", LS(a, 77))
}
