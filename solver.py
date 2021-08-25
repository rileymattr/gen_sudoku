from graph import Graph

def checker(graph):
	for i in range(len(graph.edges)):
		y = int(i/(graph.size**2))
		x = i - (y*(graph.size**2))
		color = graph.vertices[y][x]
		for j in range(len(graph.edges[i])):
			u = graph.edges[i][j]
			if color == graph.vertices[u[1]][u[0]]:
				return False
	return True
