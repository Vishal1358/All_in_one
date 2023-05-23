package main

import "fmt"

type node struct {
	data int
	next *node
}

type linked struct {
	head *node
	tail *node
	size int
}

func (l *linked) len() int {
	return l.size
}

// func (l *linked) isempty() bool {
// 	return l.head.data == 0
// }

func (l *linked) addlast(e int) {
	b := node{e, nil}
	new := &b
	if l.head == nil {
		l.head = new
	} else {
		l.tail.next = new
	}
	l.tail = new

}

func (l *linked) addfirst(e int) {
	newest := node{e, nil}
	b := &newest
	if l.head == nil {
		l.head = b
		l.tail = b
	} else {
		b.next = l.head
		l.head = b
	}
}

func (l *linked) addany(e, position int) {
	newest := node{e, nil}
	b := &newest
	p := l.head
	i := 1
	for i < position-1 {
		p = p.next
		i++
	}
	b.next = p.next
	p.next = b

}

func (l *linked) removefirst() {
	p := l.head
	for p == nil {
		fmt.Println("List is empty")
		return
	}
	e := l.head.data
	l.head = l.head.next
	if p == nil {
		l.tail = nil
	}
	_ = e

}

func (l *linked) removeany(position int) {

	p := l.head
	i := 1
	for i < position-1 {
		p = p.next
		i++
	}

	e := p.next.data
	p.next = p.next.next
	// return e
	_ = e

}

func (l *linked) removelast() {
	p := l.head
	for p != nil {
		fmt.Println("List is empty")
		return
	}
	p = l.head
	i := 1
	if i < l.len()-1 {
		p = p.next
		i++
	}
	l.tail = p
	p = p.next
	e := p.data
	l.tail.next = nil
	l.size -= 1
	return
	_ = e
}

func (l *linked) search(key int) int {
	p := l.head
	index := 0
	for p != nil {
		if p.data == key {
			return index
		}
		p = p.next
		index++
	}
	return -1
}

func (l *linked) display() {
	p := l.head
	for p != nil {
		fmt.Print(p.data, "-->")
		p = p.next
	}
}

func main() {

	a := linked{}
	a.addlast(10)
	a.addlast(11)
	a.addlast(12)
	a.addlast(13)
	// a.display()

	// fmt.Println(a.search(12))
	// a.addfirst(15)

	// a.addany(35, 3)
	// a.display()
	// a.removefirst()
	// a.removelast()
	// a.removeany(3)
	a.removelast()
	a.display()
	// fmt.Printf("%T\n", a)

}
