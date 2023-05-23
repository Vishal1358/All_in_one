// 4.WAP to check whether the given two strings are anagram or not:
// Explanation: two string are said to be anagram, if the letters from one string can be rearranged to form the other string
// Input 1:
//         String1: “coal”
//         String2: “caol”
// Output 1 : “ both the string are anagram”

// Input2:
//
//	String1: “hello”
//	String2: “heelo”
//
// Output2: “both strings are not anagram”
package main

import "fmt"

func isAnagram(s, t string) string {

	lenS := len(s)
	lenT := len(t)

	if lenS != lenT {
		return "both string length is not equal"
	}

	anagram := make(map[string]int)

	for i := 0; i < lenS; i++ {
		anagram[string(s[i])]++
	}

	for i := 0; i < lenT; i++ {
		anagram[string(t[i])]--
	}

	for i := 0; i < lenS; i++ {
		if anagram[string(s[i])] != 0 {
			return "both strings are not anagram"
		}
	}

	return "both the string are anagram"
}

func main() {
	output := isAnagram("abc", "bac")
	fmt.Println(output)

	op := isAnagram("man", "MAN")
	fmt.Println(op)
}
