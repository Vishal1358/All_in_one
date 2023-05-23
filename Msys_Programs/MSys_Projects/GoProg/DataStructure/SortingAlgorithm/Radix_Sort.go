package main

import (
	"fmt"
	"math"
	"strconv"
)

func radixSort(A []int) {
	n := len(A)
	maxnum := A[0]
	for _, v := range A {
		if v > maxnum {
			maxnum = v
		}
	}

	digits := len(strconv.Itoa(maxnum))
	bins := make([][]int, 10)

	for i := 0; i < digits; i++ {
		for j := 0; j < n; j++ {
			e := (A[j] / int(math.Pow(10, float64(i))) % 10)
			bins[e] = append(bins[e], A[j])
		}

		k := 0

		for x := 0; x < 10; x++ {
			if len(bins[x]) > 0 {
				for len(bins[x]) > 0 {
					A[k] = bins[x][0]
					bins[x] = bins[x][1:]
					k++
				}
			}
		}
	}

}

func main() {
	// A := []int{63, 250, 835, 947, 651, 28}
	A := []int{3, 5, 8, 9, 6, 2, 3, 5, 5}
	fmt.Println("Original Array:", A)
	radixSort(A)
	fmt.Println("Sorted Array:", A)
}
