// 1.WAP to toggle the case in a string
// Input: “HellO WorLd”
// Output: “hELLo wORlD”
package main

import (
	"fmt"
	"strings"
)

func toggleCase(s string) string {

	var result strings.Builder
	for _, ch := range s {
		if ch >= 'A' && ch <= 'Z' {
			result.WriteRune(ch + 32)
		} else if ch >= 'a' && ch <= 'z' {
			result.WriteRune(ch - 32)
		} else {
			result.WriteRune(ch)
		}
	}

	return result.String()
}

func main() {
	inputStr := "HellO WorLd"
	outputStr := toggleCase(inputStr)
	fmt.Println(outputStr) // prints "hELLo wORlD"
}
