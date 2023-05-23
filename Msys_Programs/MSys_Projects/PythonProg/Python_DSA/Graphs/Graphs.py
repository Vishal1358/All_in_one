import numpy as np

# Graph ADT(Abstract Data Type)
class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjMat = np.zeros((vertices, vertices))

    def insert_edge(self, u, v, x=1):
        self._adjMat[u][v]=x
    
    def remove_edge(self, u, v):
        self._adjMat[u][v]=0
    
    def exist_edge(self, u, v):
        return self._adjMat[u][v] != 0
    
    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count = count + 1
        return count

    def Vertices(self):
        for i in range(self._vertices):
            print(i,end=" ")
        print()

    def Edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i,"--",j)
    
    def outdegree(self, v):
        count = 0
        for j in range(self._vertices):
            if self._adjMat[v][j] != 0:
                count = count + 1
        return count

    def indegree(self, v):
        count = 0 
        for i in range(self._vertices):
            if self._adjMat[i][v] != 0:
                count = count + 1
        return count

    def display_adjMat(self):
        print(self._adjMat)

G = Graph(4)
# G.display_adjMat()
# print("Vertices:",G.vertex_count())
# print("Edges:",G.edge_count())
# Undirected Graph-------------------------------
# G.insert_edge(0,1)
# G.insert_edge(0,2)
# G.insert_edge(1,0)
# G.insert_edge(1,2)
# G.insert_edge(2,0)
# G.insert_edge(2,1)
# G.insert_edge(2,3)
# G.insert_edge(3,2)
# G.display_adjMat()
# print("Edges:",G.edge_count())
# G.Edges()
# print("edge between 1-3",G.exist_edge(1, 3))
# print("edge between 1-2",G.exist_edge(1, 2))
# print("Degree",G.indegree(2))
# G.remove_edge(1, 2)
# print("edge between 1-2",G.exist_edge(1, 2))
# Weighted Undirected Graph--------------------------------------
# G.insert_edge(0,1,26)
# G.insert_edge(0,2,16)
# G.insert_edge(1,0,26)
# G.insert_edge(1,2,12)
# G.insert_edge(2,0,16)
# G.insert_edge(2,1,12)
# G.insert_edge(2,3,8)
# G.insert_edge(3,2,8)
# G.display_adjMat()
# print("Edges:",G.edge_count())
# G.Edges()
# print("edge between 1-3",G.exist_edge(1, 3))
# print("edge between 1-2",G.exist_edge(1, 2))
# print("Degree",G.indegree(2))
# G.remove_edge(1, 2)
# print("edge between 1-2",G.exist_edge(1, 2))

# Directed Graph--------------------------------------
# G.display_adjMat()
# print("Vertices:",G.vertex_count())
# G.insert_edge(0, 1)
# G.insert_edge(0, 2)
# G.insert_edge(1, 2)
# G.insert_edge(2, 3)
# G.display_adjMat()
# print("Edges:", G.edge_count())
# G.Edges()
# print("edge between 1-3",G.exist_edge(1, 3))
# print("edge between 1-2",G.exist_edge(1, 2))
# print("Indegree 2", G.indegree(2))
# print("Outdegree 2", G.outdegree(2))
# G.remove_edge(1, 2)
# print("edge between 1-2",G.exist_edge(1, 2))

# Weighted Directed Graph---------------------------------
G.display_adjMat()
print("Vertices:",G.vertex_count())
G.insert_edge(0, 1, 26)
G.insert_edge(0, 2, 16)
G.insert_edge(1, 2, 12)
G.insert_edge(2, 3, 8)
G.display_adjMat()
print("Edges:", G.edge_count())
G.Edges()
print("edge between 1-3",G.exist_edge(1, 3))
print("edge between 1-2",G.exist_edge(1, 2))
print("Indegree 2", G.indegree(2))
print("Outdegree 2", G.outdegree(2))
G.remove_edge(1, 2)
print("edge between 1-2",G.exist_edge(1, 2))