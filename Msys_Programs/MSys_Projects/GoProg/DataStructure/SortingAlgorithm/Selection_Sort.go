package main

import "fmt"

func SelectionSort(items []int) {
	for i := 0; i < len(items)-1; i++ { // it will iterator 0 index to n -1
		min := i                              // i am storing index value in min variable this means i will take i is minimum value
		for j := i + 1; j < len(items); j++ { // it will iterator 1st index becose it will compaire 1st index to 2nd index
			if items[min] > items[j] { // it will check condition i > j if its true swap it otherwise increment j value
				min = j
			}
		} // after j iterator complete
		if min != i { // it will check min != i its true it will swap becose we alredy define min = i

			items[i], items[min] = items[min], items[i] // i value and min value swap

		}
	}
}

func main() {
	items := []int{25, -2, 660, 8, -1, 0, 8.00}
	fmt.Println(items)
	SelectionSort(items)
	fmt.Println(items)
}
