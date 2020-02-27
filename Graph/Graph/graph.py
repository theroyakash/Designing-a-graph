import numpy as np
from collections import defaultdict

class Graph:

    number_of_edges = 0

    def __init__(self, vertices, is_directed=False):
        self.vertices = vertices
        self.graph = np.zeros((vertices,vertices), dtype=int)
        self.is_directed = is_directed

    def add_edge_between(self, start, end, weight):
        if not self.is_directed and self.graph[start][end]==0 and self.graph[end][start]== 0:
            self.graph[start][end] = weight
            self.graph[end][start] = weight
            self.number_of_edges+=1

        elif self.is_directed and self.graph[start][end]==0:
            self.graph[start][end] = weight
            self.number_of_edges+=1

        else:
            pass


    def show_graph(self):
        return self.graph