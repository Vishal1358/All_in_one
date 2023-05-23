package main

import "fmt"

func search(nums []int, target int) int {
	start := 0
	end := len(nums) - 1

	for start <= end {
		mid := (end + start) >> 1
		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			start = mid + 1
		} else {
			end = mid - 1
		}
	}
	return -1
}

func main() {
	O := []int{2, 3, 5, 6, 7, 9}
	fmt.Println(search(O, 5))
	fmt.Println(search(O, 1))
	fmt.Println(search(O, 8))

}
