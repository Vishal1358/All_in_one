package main

import "fmt"

func main() {
	var s int
	fmt.Scan(&s)

	if s%2 == 0 {
		fmt.Print("Even")
	} else {
		fmt.Print("Odd")
	}

}
