package main

import "fmt"

type Heap struct {
	maxsize int
	data    []int
	csize   int
}

func constructor() *Heap {
	h := new(Heap)
	h.maxsize = 10
	h.data = make([]int, h.maxsize)
	h.csize = 0
	return h
}

func (pqh *Heap) len() int {
	return len(pqh.data)
}

func (pqh *Heap) isempty() bool {
	return pqh.csize == 0
}

func (pqh *Heap) insert(e int) {
	if pqh.csize == pqh.maxsize {
		fmt.Println("No Space!...")
		return
	}
	pqh.csize += 1
	hi := pqh.csize
	for hi > 1 && e > pqh.data[hi/2] {
		pqh.data[hi] = pqh.data[hi/2]
		hi = hi / 2
	}
	pqh.data[hi] = e
}

func (pqh *Heap) max() int {
	if pqh.isempty() {
		fmt.Println("Heap is empty!...")
		return -1
	}
	return pqh.data[1]
}

func (pqh *Heap) deleteMax() int {
	if pqh.isempty() {
		fmt.Println("Heap is empty!...")
		return -1
	}
	e := pqh.data[1]
	pqh.data[1] = pqh.data[pqh.csize]
	pqh.data[pqh.csize] = 0
	pqh.csize -= 1
	i := 1
	j := i * 2
	for j <= pqh.csize {
		if pqh.data[j] < pqh.data[j+1] {
			j = j + 1
		}
		if pqh.data[i] < pqh.data[j] {
			temp := pqh.data[i]
			pqh.data[i] = pqh.data[j]
			pqh.data[j] = temp
			i = j
			j = i * 2
		} else {
			break
		}
	}
	return e
}

func heapSort(A []int) {
	heap := constructor()
	n := len(A)
	for i := 0; i < n; i++ {
		heap.insert(A[i])
	}

	k := n - 1
	for j := 0; j < n; j++ {
		A[k] = heap.deleteMax()
		k--
	}

}

func main() {
	H := constructor()
	H.insert(20)
	H.insert(14)
	H.insert(2)
	H.insert(15)
	H.insert(10)
	H.insert(21)
	fmt.Printf("%#v\n", H.data)
	fmt.Printf("%d\n", H.max())
	fmt.Printf("%d\n", H.deleteMax())
	fmt.Printf("%#v\n", H.data)

	A := []int{20, 14, 2, 15, 10, 21}
	fmt.Printf("Original Array : %#v\n", A)
	heapSort(A)
	fmt.Printf("Sorted Array : %#v\n", A)

}
