package main

import "fmt"

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	t := x
	r := 0
	for x > 0 {
		r = r*10 + x%10
		x /= 10
	}
	return t == r
}

func main() {
	fmt.Println(isPalindrome(101))
	fmt.Println(isPalindrome(121))
	fmt.Println(isPalindrome(102))
}
