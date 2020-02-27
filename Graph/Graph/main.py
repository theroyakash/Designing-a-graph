from graph import Graph
import numpy as np
from BellmanFord import bellmanford_path

graph1 = Graph(vertices=20,is_directed=True)

while graph1.number_of_edges<100:
	random_start = np.random.randint(low=0,high=graph1.vertices)
	random_end = np.random.randint(low=0,high=graph1.vertices)

	random_weight = np.random.randint(-7,20)
	if random_weight !=0 and graph1.show_graph()[random_start][random_end]==0:
		graph1.add_edge_between(start=random_start, end=random_end, weight=random_weight)
		graph1.add_edge_between(start=random_start,end=random_end,weight=random_weight)
	else:
		pass

print(graph1.number_of_edges)
print(graph1.vertices)
print(graph1.show_graph())

a = bellmanford_path(graph=graph1)

print(a)