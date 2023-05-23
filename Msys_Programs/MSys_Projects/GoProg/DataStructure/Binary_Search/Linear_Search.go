package main

import "fmt"

func linearsearch(A []int, key int) int {
	index := 0
	for index < len(A) {
		if A[index] == key {
			return index
		}
		index += 1
	}
	return -1
}

func main() {
	A := []int{25, 36, 65, 96, 88}
	key := 36
	fmt.Println("Original list and key:", A)
	fmt.Println("Original key:", key)

	fmt.Println("Index No:", linearsearch(A, key))

}
