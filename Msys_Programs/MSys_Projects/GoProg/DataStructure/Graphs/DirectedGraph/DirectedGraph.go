package main

import "fmt"

type Graph struct {
	vertices int
	adjMat   [][]int
}

func cunstructor(vertices int) *Graph {
	G := &Graph{}
	G.vertices = vertices
	for i := 0; i < G.vertices; i++ {
		G.adjMat = append(G.adjMat, make([]int, G.vertices))
	}
	return G
}

func (g *Graph) insert_edge(u, v, x int) {
	if x == 0 {
		x = 1
	}
	g.adjMat[u][v] = x
}

func (g *Graph) remove_edge(u, v int) {
	g.adjMat[u][v] = 0
}

func (g *Graph) exist_edge(u, v int) bool {
	return g.adjMat[u][v] != 0
}

func (g *Graph) vertex_count() int {
	return g.vertices
}

func (g *Graph) edge_count() int {
	count := 0
	for i := 0; i < g.vertices; i++ {
		for j := 0; j < g.vertices; j++ {
			if g.adjMat[i][j] != 0 {
				count++
			}
		}
	}
	return count
}

func (g *Graph) vertice() {
	for i := 0; i < g.vertices; i++ {
		fmt.Printf("%d ", i)
	}
	fmt.Println()
}

func (g *Graph) edges() {
	for i := 0; i < g.vertices; i++ {
		for j := 0; j < g.vertices; j++ {
			if g.adjMat[i][j] != 0 {
				fmt.Printf("%d -- %d\n", i, j)
			}
		}
	}
}

func (g *Graph) outdgree(v int) int {
	count := 0
	for i := 0; i < g.vertices; i++ {
		if g.adjMat[v][i] != 0 {
			count++
		}
	}
	return count
}

func (g *Graph) indegree(v int) int {
	count := 0
	for i := 0; i < g.vertices; i++ {
		if g.adjMat[i][v] != 0 {
			count++
		}
	}
	return count
}

func (g *Graph) display_adjMat() {
	fmt.Println(g.adjMat)
}

func main() {
	G := cunstructor(4)
	G.display_adjMat()
	fmt.Printf("%d\n", G.vertex_count())
	fmt.Printf("%d\n", G.edge_count())
	G.insert_edge(0, 1, 0)
	G.insert_edge(0, 2, 0)
	G.insert_edge(1, 2, 0)
	G.insert_edge(2, 3, 0)
	G.display_adjMat()
	fmt.Printf("%d\n", G.vertex_count())
	fmt.Printf("%d\n", G.edge_count())
	G.vertice()
	G.edges()
	fmt.Printf("Indegree of %d : %d\n", 2, G.indegree(2))
	fmt.Printf("%t\n", G.exist_edge(1, 2))
	G.remove_edge(1, 2)
	fmt.Printf("%t\n", G.exist_edge(1, 2))
	fmt.Printf("Indegree of %d : %d\n", 2, G.indegree(2))

}
