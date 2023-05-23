package main

import "fmt"

type Node struct {
	element int
	next    *Node
}

type Singly struct {
	head *Node
	tail *Node
	size int
}

func (s *Singly) len() int {
	return s.size
}

func (s *Singly) isempty() bool {
	return s.size == 0
}

func (s *Singly) addlast(e int) {
	n := &Node{e, nil}
	if s.head == nil {
		s.head = n
	} else {
		s.tail.next = n
	}
	s.tail = n
	s.size++
}

func (s *Singly) Display() {
	p := s.head
	for p != nil {
		fmt.Print(p.element, "-->")
		p = p.next
	}
}

func main() {
	O := &Singly{}
	O.addlast(25)
	O.addlast(26)
	O.addlast(27)
	O.addlast(28)
	O.addlast(29)
	O.Display()
}
