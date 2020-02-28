import numpy as np

def dijsktra_path(graph, start_from=0):
    
    distances = [160] * graph.vertices
    distances[start_from] = 0
    return []