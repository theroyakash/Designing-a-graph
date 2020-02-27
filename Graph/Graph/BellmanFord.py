import numpy as np
'''
The algorithm goes like this
    1. Set every edge distance to (+)inf
    2. Set d[source] = 0
    3. Relax each edge V - 1 times 

'''
def bellmanford_path(graph,start_from=0):

	number_of_vertices = graph.vertices

	distances = [160] * number_of_vertices
	distances[start_from] = 0

	matrix_of_graph = graph.show_graph()
	prev = np.zeros((number_of_vertices,1), dtype=int)

	for _ in range(number_of_vertices - 1):
		for i in range(number_of_vertices):
			for j in range(number_of_vertices):
				if distances[i] + matrix_of_graph[i][j] < distances[j]:
					distances[j] = distances[i] + matrix_of_graph[i][j]
					prev[j] = i
	
	# Running for another time to detect the negative edge cycle
	for _ in range(graph.vertices - 1):
		for i in range(graph.vertices):
			for j in range(graph.vertices):
				if distances[i] + matrix_of_graph[i][j] < distances[j]:
					distances[j] = - 160
					prev[j] = -1

	return distances