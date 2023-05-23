package main

import "fmt"

func isValid(s string) bool {
	l := len(s)

	if l == 1 {
		return false
	}

	stack := make([]byte, 0, l/2)

	brackets := make(map[byte]byte, 3)
	brackets['('] = ')'
	brackets['['] = ']'
	brackets['{'] = '}'

	for i := range s {
		if r, f := brackets[s[i]]; f {
			stack = append(stack, r)
		} else if len(stack) > 0 && stack[len(stack)-1] == s[i] {
			stack = stack[:len(stack)-1]
		} else {
			return false
		}
	}

	return len(stack) == 0
}

func main() {
	fmt.Println(isValid("(){}"))
	fmt.Println(isValid("({})"))
	fmt.Println(isValid("({}[])"))
	fmt.Println(isValid("({}{]})"))
	fmt.Println(isValid("()"))
	fmt.Println(isValid("{}"))
	fmt.Println(isValid("[]"))
}
