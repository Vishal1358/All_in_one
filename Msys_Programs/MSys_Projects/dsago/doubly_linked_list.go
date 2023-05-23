package main

import "fmt"

type node struct {
	data int
	next *node
	prev *node
}

type linked struct {
	head *node
	tail *node
	size int
}

// func (l *linked) len(num int) int {
// 	return l.size
// }

func (l *linked) addlast(e int) {
	b := node{e, nil, nil}
	new := &b
	if l.head == nil && l.tail == nil {
		l.head = new
		l.tail = new
	} else {
		l.tail.next = new
		new.prev = l.tail
		l.tail = new
	}
	l.size++
	return
}

func (l *linked) addfirst(e int) {
	b := node{e, nil, nil}
	new := &b
	if l.head == nil && l.tail == nil {
		l.head = new
		l.tail = new
	} else {
		new.next = l.head
		l.head.prev = new
		l.head = new
	}
	l.size++

}

func (l *linked) addany(e int, position int) {
	b := node{e, nil, nil}
	new := &b
	p := l.head
	i := 1
	for i < position-1 {
		p = p.next
		i++
	}
	new.next = p.next
	p.next.prev = new
	p.next = new
	new.prev = p
	l.size++
}

func (l *linked) removefirst() {
	if l.head == nil && l.tail == nil {
		fmt.Println("List is empty")
		return
	}
	e := l.head.data
	l.head = l.head.next
	l.head.prev = nil
	l.size -= 1
	if l.head == nil && l.tail == nil {
		l.tail = nil
	}
	// return e
	_ = e
}

func (l *linked) removelast() {
	if l.head == nil && l.tail == nil {
		fmt.Println("list is empty")
		return
	}
	e := l.tail.data
	l.tail = l.tail.prev
	l.tail.next = nil
	l.size -= 1
	_ = e
}

func (l *linked) removeany(position int) {
	p := l.head
	i := 1
	if i < position-1 {
		p = p.next
		i++
	}
	e := p.next.data
	p.next = p.next.next
	p.next.prev = p
	l.size -= 1
	_ = e
}

func (l *linked) display() {
	p := l.head
	for p != nil {
		fmt.Print(p.data, "-->")
		p = p.next
	}
	fmt.Println()
}

func (l *linked) displayrev() {
	p := l.tail
	for p != nil {
		fmt.Println(p.data, "-->")
		p = p.prev
	}
	fmt.Println()
}

func main() {
	L := linked{}
	L.addlast(2)
	L.addlast(3)
	L.addlast(4)
	L.addlast(5)
	L.addlast(7)
	L.addlast(9)
	// L.display()
	// fmt.Println("revers order")
	// L.displayrev()
	L.addfirst(20)
	// L.display()
	// fmt.Println("revers order")
	// L.displayrev()
	L.addany(26, 4)
	// L.display()
	// fmt.Println("revers order")
	// L.displayrev()
	// L.removefirst()
	// L.display()
	// fmt.Println("revers order")
	// L.displayrev()
	// L.removelast()
	// L.display()
	// fmt.Println("revers order")
	// L.displayrev()
	L.removeany(3)
	L.display()
	fmt.Println("revers order")
	L.displayrev()
}
