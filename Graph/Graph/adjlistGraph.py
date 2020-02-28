import numpy as np
import sys
from PriorityQueue import PriorityQueue

class GraphList:
    def __init__(self, num):
        self.adjList = {}  # To store graph: u -> (v,w)
        self.num_nodes = num  # Number of nodes in graph
        # To store the distance from source vertex
        self.dist = [0] * self.num_nodes
        self.par = [-1] * self.num_nodes  # To store the path

    def add_edge(self, u, v, w):
        #  Edge going from node u to v and v to u with weight w
        # u (w)-> v, v (w) -> u
        # Check if u already in graph
        if u in self.adjList.keys():
            self.adjList[u].append((v, w))
        else:
            self.adjList[u] = [(v, w)]

        # Assuming undirected graph
        if v in self.adjList.keys():
            self.adjList[v].append((u, w))
        else:
            self.adjList[v] = [(u, w)]

    def show_graph(self):
        # u -> v(w)
        for u in self.adjList:
            print(u, "->", " -> ".join(str(f"{v}({w})") for v, w in self.adjList[u]))

    def dijkstra(self, src):
        # Flush old junk values in par[]
        self.par = [-1] * self.num_nodes
        # src is the source node
        self.dist[src] = 0
        Q = PriorityQueue()
        Q.insert((0, src))  # (dist from src, node)
        for u in self.adjList.keys():
            if u != src:
                self.dist[u] = sys.maxsize  # Infinity
                self.par[u] = -1

        while not Q.isEmpty():
            u = Q.extract_min()  # Returns node with the min dist from source
            # Update the distance of all the neighbours of u and
            # if their prev dist was INFINITY then push them in Q
            for v, w in self.adjList[u]:
                new_dist = self.dist[u] + w
                if self.dist[v] > new_dist:
                    if self.dist[v] == sys.maxsize:
                        Q.insert((new_dist, v))
                    else:
                        Q.decrease_key((self.dist[v], v), new_dist)
                    self.dist[v] = new_dist
                    self.par[v] = u

        # Show the shortest distances from src
        self.show_distances(src)

    def show_distances(self, src):
        print(f"Distance from node: {src}")
        for u in range(self.num_nodes):
            print(f"Node {u} has distance: {self.dist[u]}")

    def show_path(self, src, dest):
        # To show the shortest path from src to dest
        # WARNING: Use it *after* calling dijkstra
        path = []
        cost = 0
        temp = dest
        # Backtracking from dest to src
        while self.par[temp] != -1:
            path.append(temp)
            if temp != src:
                for v, w in self.adjList[temp]:
                    if v == self.par[temp]:
                        cost += w
                        break
            temp = self.par[temp]
        path.append(src)
        path.reverse()

        print(f"----Path to reach {dest} from {src}----")
        for u in path:
            print(f"{u}", end=" ")
            if u != dest:
                print("-> ", end="")

        print("\nTotal cost of path: ", cost)