package main

import (
	"fmt"
)

type Node struct {
	_element int
	_left    *Node
	_right   *Node
}

type BinaryTree struct {
	_root *Node
}

func (b *BinaryTree) maketree(e int, left, right *BinaryTree) {
	b._root = &Node{e, left._root, right._root}
}

func (b *BinaryTree) inorder(troot *Node) {
	if troot != nil {
		b.inorder(troot._left)
		fmt.Printf("%d ", troot._element)
		b.inorder(troot._right)
	}

}
func (b *BinaryTree) preorder(troot *Node) {
	if troot != nil {
		fmt.Printf("%d ", troot._element)
		b.postorder(troot._left)
		b.postorder(troot._right)
	}
}

func (b *BinaryTree) postorder(troot *Node) {
	if troot != nil {
		b.postorder(troot._left)
		b.postorder(troot._right)
		fmt.Printf("%d ", troot._element)
	}
}

func (b *BinaryTree) levelorder(troot *Node) {
	Q := []*Node{}
	t := troot
	fmt.Println(troot._element, " ")
	Q = append(Q, t)
	for len(Q) > 0 {
		t = Q[0]
		Q = Q[1:]
		if t._left != nil {
			fmt.Println(t._left._element, " ")
			Q = append(Q, t._left)
		}
		if t._right != nil {
			fmt.Println(t._right._element, " ")
			Q = append(Q, t._right)
		}
	}
}

func (b *BinaryTree) count(troot *Node) int {
	if troot != nil {
		x := b.count(troot._left)
		y := b.count(troot._right)
		return x + y + 1
	}
	return 0
}

func (b *BinaryTree) height(troot *Node) int {
	if troot != nil {
		x := b.height(troot._left)
		y := b.height(troot._right)
		if x > y {
			return x + 1
		} else {
			return y + 1
		}
	}
	return 0
}

func main() {
	x := &BinaryTree{}
	y := &BinaryTree{}
	z := &BinaryTree{}
	r := &BinaryTree{}
	s := &BinaryTree{}
	t := &BinaryTree{}
	a := &BinaryTree{}
	x.maketree(40, a, a)
	y.maketree(60, a, a)
	z.maketree(20, x, a)
	r.maketree(50, a, y)
	s.maketree(30, r, a)
	t.maketree(10, z, s)
	fmt.Println("Inorder Traversal")
	t.inorder(t._root)
	fmt.Println()
	fmt.Println("Preorder Traversal")
	t.preorder(t._root)
	fmt.Println()
	fmt.Println("Postorder Traversal")
	t.postorder(t._root)
	fmt.Println()
	fmt.Println("Levelorder Traversal")
	t.levelorder(t._root)
	// fmt.Println()
	fmt.Println("Number of Nodes :", t.count(t._root))
	fmt.Println()
	fmt.Println("Number of Height :", t.height(t._root))

}
