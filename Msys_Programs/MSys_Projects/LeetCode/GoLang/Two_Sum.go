package main

import "fmt"

func twoSum(nums []int, target int) []int {
	for i, right := range nums {
		for j, left := range nums {
			if right+left == target && i != j {
				return []int{i, j}
			}
		}
	}
	return nil
}

func main() {
	B := []int{2, 7, 11, 15}
	Target := 9
	T := twoSum(B, Target)
	fmt.Println(T)
}
