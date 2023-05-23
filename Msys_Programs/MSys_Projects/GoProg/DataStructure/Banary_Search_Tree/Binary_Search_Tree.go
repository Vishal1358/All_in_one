package main

import "fmt"

type Node struct {
	element int
	left    *Node
	right   *Node
}

type BinarySearchTree struct {
	root *Node
}

// Iterative Insert
func (bst *BinarySearchTree) insert(troot *Node, e int) {
	var temp *Node
	for troot != nil {
		temp = troot
		if e == troot.element {
			return
		} else if e < troot.element {
			troot = troot.left
		} else if e > troot.element {
			troot = troot.right
		}
	}

	n := &Node{e, nil, nil}
	if bst.root != nil {
		if e < temp.element {
			temp.left = n
		} else {
			temp.right = n
		}
	} else {
		bst.root = n
	}

}

// Recursive Insert
func (bst *BinarySearchTree) rinsert(troot *Node, e int) *Node {
	if troot != nil {
		if e < troot.element {
			troot.left = bst.rinsert(troot.left, e)
		} else if e > troot.element {
			troot.right = bst.rinsert(troot.right, e)
		}
	} else {
		n := &Node{e, nil, nil}
		troot = n
	}
	return troot
}

// Iterative Search
func (bts *BinarySearchTree) search(key int) bool {
	troot := bts.root
	for troot != nil {
		if key == troot.element {
			return true
		} else if key < troot.element {
			troot = troot.left
		} else if key > troot.element {
			troot = troot.right
		}
	}
	return false
}

// Recursive Search
func (bts *BinarySearchTree) rsearch(troot *Node, key int) bool {
	if troot != nil {
		if key == troot.element {
			return true
		} else if key < troot.element {
			return bts.rsearch(troot.left, key)
		} else if key > troot.element {
			return bts.rsearch(troot.right, key)
		}
	}
	return false
}

func (bts *BinarySearchTree) delete(e int) {
	p := bts.root
	var pp *Node
	for p != nil && p.element != e {
		pp = p
		if e < p.element {
			p = p.left
		} else {
			p = p.right
		}
	}
	if p != p {
		return
	}
	if p.left != nil && p.right != nil {
		s := p.left
		ps := p
		for s.right != nil {
			ps = s
			s = s.right
		}
		p.element = s.element
		p = s
		pp = ps
	}
	var c *Node
	if p.left != nil {
		c = p.left
	} else {
		c = p.right
	}
	if p == bts.root {
		bts.root = nil
	} else {
		if p == pp.left {
			pp.left = c
		} else {
			pp.right = c
		}
	}
}

// Inorder Traversal
func (bst *BinarySearchTree) inorder(troot *Node) {
	if troot != nil {
		bst.inorder(troot.left)
		fmt.Print(troot.element, " ")
		bst.inorder(troot.right)
	}
}

// Preorder Traversal
func (bst *BinarySearchTree) preorder(troot *Node) {
	if troot != nil {
		fmt.Print(troot.element, " ")
		bst.preorder(troot.left)
		bst.preorder(troot.right)
	}
}

// Postorder Traversal
func (bst *BinarySearchTree) postorder(troot *Node) {
	if troot != nil {
		bst.postorder(troot.left)
		bst.postorder(troot.right)
		fmt.Print(troot.element, " ")
	}
}

func main() {
	B := BinarySearchTree{}
	// B.insert(B.root, 50)
	// B.insert(B.root, 30)
	// B.insert(B.root, 80)
	// B.insert(B.root, 10)
	// B.insert(B.root, 40)
	// B.insert(B.root, 60)
	// B.insert(B.root, 90)
	B.root = B.rinsert(B.root, 50)
	B.rinsert(B.root, 30)
	B.rinsert(B.root, 80)
	B.rinsert(B.root, 10)
	B.rinsert(B.root, 40)
	B.rinsert(B.root, 60)
	B.rinsert(B.root, 90)
	fmt.Println("Inorder Traversal")
	B.inorder(B.root)
	fmt.Println()
	fmt.Println("Preorder Traversal")
	B.preorder(B.root)
	fmt.Println()
	fmt.Println("postorder Traversal")
	B.postorder(B.root)
	fmt.Println()
	// fmt.Println(B.search(90))
	// fmt.Println(B.search(91))
	fmt.Println(B.rsearch(B.root, 90))
	fmt.Println(B.rsearch(B.root, 99))
	B.delete(55)
	B.inorder(B.root)
}
