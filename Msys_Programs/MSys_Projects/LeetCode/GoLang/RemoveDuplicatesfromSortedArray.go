package main

import "fmt"

func removeDuplicates(nums []int) {
	i := 1
	for i < len(nums) {
		if nums[i] == nums[i-1] {
			nums = append(nums[:i], nums[i+1:]...)
		} else {
			i++
		}
	}
	fmt.Println(i)
}

func main() {
	O := []int{2, 2, 3, 3, 4, 4, 5, 5, 6}
	removeDuplicates(O)
}
