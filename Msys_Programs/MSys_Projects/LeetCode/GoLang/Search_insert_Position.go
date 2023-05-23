package main

import "fmt"

func searchInsert(nums []int, target int) int {
	if nums[len(nums)-1] < target {
		return len(nums)
	}
	for i := 0; i < len(nums); i++ {
		if nums[i] == target {
			return i
		}
		if nums[i] > target {
			return i
		}
	}
	return -1
}

func main() {
	O := []int{1, 3, 5, 6}
	t := 2
	fmt.Println(searchInsert(O, t))
}
