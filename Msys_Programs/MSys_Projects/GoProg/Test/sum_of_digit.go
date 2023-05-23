// WAP to find the sum of digits of a number, using recursion
package main

import (
	"fmt"
)

func sum_fo_digit(n int) int {
	if n == 0 {
		return 0
	}
	return (n%10 + sum_fo_digit(int(n/10)))
}

func main() {
	n := sum_fo_digit(2536)
	fmt.Println(n)
}

// def sum_of_digit( n ):
//     if n == 0:
//         return 0
//     return (n % 10 + sum_of_digit(int(n / 10)))
