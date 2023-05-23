package main

import "fmt"

type Node struct {
	data int
	next *Node
}

type CircularLinkedList struct {
	head *Node
	tail *Node
	size int
}

func (cl *CircularLinkedList) len() int {
	return cl.size
}

func (cl *CircularLinkedList) isempty() bool {
	return cl.size == 0
}

func (cl *CircularLinkedList) search(v int) int {
	p := cl.head
	i := 0
	for i < cl.len() {
		if p.data == v {
			return i
		}
		p = p.next
		i++
	}
	return -1
}

func (cl *CircularLinkedList) addlast(n int) {
	new := &Node{n, nil}
	if cl.isempty() {
		new.next = new
		cl.head = new
	} else {
		new.next = cl.head
		// new.next = cl.tail.next
		cl.tail.next = new
	}
	cl.tail = new
	cl.size++
}

func (cl *CircularLinkedList) addany(n int, index int) {
	if index == 0 {
		cl.addfirst(n)
	} else if index > (cl.len())-1 {
		cl.addlast(n)
	} else {
		new := &Node{n, nil}
		p := cl.head
		i := 1
		for i < index {
			p = p.next
			i++
		}
		new.next = p.next
		p.next = new
		cl.size++
	}
}

func (cl *CircularLinkedList) addfirst(n int) {
	new := &Node{n, nil}
	if cl.isempty() {
		new.next = new
		cl.tail = new
	} else {
		new.next = cl.head
	}
	cl.head = new
	cl.size++
}

func (cl *CircularLinkedList) removefirst() {
	if cl.isempty() {
		fmt.Println("Circular Linked LIst is empty")
	} else {
		cl.head = cl.head.next
		cl.tail.next = cl.head
		cl.size--
	}
	if cl.isempty() {
		cl.head = nil
		cl.tail = nil
	}
}

func (cl *CircularLinkedList) removelast() {
	if cl.isempty() {
		fmt.Println("Circular Linked lis is empty")
	} else {
		p := cl.head
		i := 1
		for i < (cl.len() - 1) {
			p = p.next
			i++
		}
		p.next = cl.tail.next
		cl.tail = p
		cl.size--
	}
	if cl.isempty() {
		cl.head = nil
		cl.tail = nil
	}
}

func (cl *CircularLinkedList) removeany(index int) {
	if index > (cl.len())-1 {
		fmt.Println("Index out of range")
	} else if index == (cl.len())-1 {
		cl.removelast()
	} else if index == 0 {
		cl.removefirst()
	} else {
		p := cl.head
		i := 1
		for i < index {
			p = p.next
			i++
		}
		p.next = p.next.next
		cl.size--
	}
	if cl.isempty() {
		cl.head = nil
		cl.tail = nil
	}
}

func (cl *CircularLinkedList) display() {
	p := cl.head
	i := 0
	for i < cl.len() {
		fmt.Print(p.data, "-->")
		p = p.next
		i++
	}
	fmt.Println()
}

func main() {
	cll := CircularLinkedList{}
	cll.addlast(10)
	cll.addlast(20)
	cll.addlast(30)
	cll.addfirst(40)
	cll.addfirst(50)
	cll.addfirst(60)
	cll.addany(10, 2)
	cll.addlast(25)
	cll.display()
	fmt.Println(cll.search(100))
	fmt.Println(cll.len())
	cll.removefirst()
	cll.removelast()
	cll.removeany(cll.len())
	cll.removeany(2)
	cll.display()
	fmt.Println(cll.len())

}
