// 2.WAP to display  prime numbers from 1 to 100

package main

import (
	"fmt"
	"math"
)

func prime(start, end int) {
	if start < 2 || end < 2 {
		fmt.Println("Numbers must be greater than 2.")
		return
	}
	for start <= end {
		isPrime := true
		for i := 2; i <= int(math.Sqrt(float64(start))); i++ {
			if start%i == 0 {
				isPrime = false
				break
			}
		}
		if isPrime {
			fmt.Printf("%d ", start)
		}
		start++
	}
	fmt.Println()
}

func main() {
	prime(2, 100)
}
