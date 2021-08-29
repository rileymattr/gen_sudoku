from graph import Graph
import queue

def checker(graph):
	for i in range(len(graph.edges)):
		y = int(i/(graph.size**2))
		x = i - (y*(graph.size**2))
		color = graph.vertices[((graph.size**2)*y)+x]
		for j in range(len(graph.edges[i])):
			u = graph.edges[i][j]
			if color == graph.vertices[u]:
				return False
	return True

def backtracking_solver(graph):
	to_color = queue.PriorityQueue()
	colored = queue.LifoQueue()

	for v in range(len(graph.vertices)):
		if graph.vertices[v] != 0:
			pass
		else:
			to_color.put((v,v))

	while not to_color.empty():
		v = to_color.get()[1]
		if graph.vertices[v] == 1+graph.size**2:
			raise Exception('No valid value for cell (' + str(v - (graph.size**2*(int((v/(graph.size**2)))))) + ',' + str(int(v/(graph.size**2))) + ')')
		for c in range(graph.vertices[v] + 1, 1+graph.size**2):
			graph.vertices[v] = c
			if graph.cell_color_valid(v):
				break
			elif c == graph.size**2:
				graph.vertices[v] = 0
				u = colored.get()
				to_color.put((u,u))
				to_color.put((v,v))
		
		colored.put(v)