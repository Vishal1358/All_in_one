package main

import (
	"fmt"
	"time"
)

type names []string

func (n names) print() {
	for i, name := range n {
		fmt.Println(i, name)
	}
}

func main() {
	const day = 24 * time.Hour
	fmt.Printf("%T\n", day)

	second := day.Seconds()
	fmt.Printf("%T\n", second)
	fmt.Printf("Seconds in a day: %v\n", second)

	friends := names{"Vinayak", "Vishal"}
	friends.print()

	names.print(friends)

	var n int64 = 93353554
	fmt.Println(n)
	fmt.Println(time.Duration(n))
}
