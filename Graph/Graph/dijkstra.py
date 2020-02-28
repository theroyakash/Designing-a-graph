import numpy as np
from PriorityQueue import PriorityQueue

def dijsktra_path(graph, start_from=0):

    number_of_vertices = graph.vertices
    
    distances = [160] * number_of_vertices
    distances[start_from] = 0

    visited = [False] * number_of_vertices
    visited[0] = True



    return []