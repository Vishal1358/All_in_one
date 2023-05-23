package main

import "fmt"

type Graph struct {
	vertices int
	adjMat   [][]int
	visited  []int
}

func cunstructor(vertices int) *Graph {
	G := &Graph{}
	G.vertices = vertices
	G.visited = make([]int, G.vertices)
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

func (g *Graph) BFS(s int) {
	i := s
	q := []int{}
	visited := make([]int, g.vertices)
	fmt.Print(i, " ")
	visited[i] = 1
	q = append(q, i)
	for len(q) != 0 {
		i = q[0]
		q = q[1:]
		for j := 0; j < g.vertices; j++ {
			if g.adjMat[i][j] != 0 && visited[j] == 0 {
				fmt.Print(j, " ")
				visited[j] = 1
				q = append(q, j)
			}
		}
	}
	fmt.Println()
}

func (g *Graph) DFS(s int) {
	if g.visited[s] == 0 {
		fmt.Print(s, " ")
		g.visited[s] = 1
		for j := 0; j < g.vertices; j++ {
			if g.adjMat[s][j] != 0 && g.visited[j] == 0 {
				g.DFS(j)
			}
		}
	}
}

func main() {
	G := cunstructor(7)
	G.display_adjMat()
	fmt.Printf("%d\n", G.vertex_count())
	fmt.Printf("%d\n", G.edge_count())
	G.insert_edge(0, 1, 0)
	G.insert_edge(0, 5, 0)
	G.insert_edge(0, 6, 0)
	G.insert_edge(1, 0, 0)
	G.insert_edge(1, 6, 0)
	G.insert_edge(1, 5, 0)
	G.insert_edge(1, 2, 0)
	G.insert_edge(2, 6, 0)
	G.insert_edge(2, 3, 0)
	G.insert_edge(3, 4, 0)
	G.insert_edge(4, 5, 0)
	G.insert_edge(5, 2, 0)
	G.insert_edge(5, 3, 0)
	G.insert_edge(6, 3, 0)
	G.display_adjMat()
	fmt.Printf("%d\n", G.vertex_count())
	fmt.Printf("%d\n", G.edge_count())
	fmt.Println("BFS :")
	G.BFS(0)
	fmt.Println("DFS :")
	G.DFS(0)

}
