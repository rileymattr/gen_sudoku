class Graph:
	def __init__(self, n: int):
		self.vertices = [[0]*(n**2)]*(n**2)
		self.edges = []
		for i in range(n**4):
			self.edges.append([])

		for y in range(n**2):
			for x in range(n**2):
				edges = self.edges[((n**2)*y) + x]
				x_region = int(x/n)
				y_region = int(y/n)
				
				#This adds edges to cells in the same region.
				for x_prime in range(0,n):
					for y_prime in range(0,n):
						if (x_region*n) + x_prime != x or (y_region*n) + y_prime != y:
							edges.append(((x_region*n) + x_prime, (y_region*n) + y_prime))

				#This adds edges to cells in the same column, outside the same region. 		
				for row in range(n**2):
					if int(row/n) != x_region:
						edges.append((row,y))

				#This adds edges to the cells in the sme row, outside the same region.
				for col in range(n**2):
					if int(col/n) != y_region:
						edges.append((x,col))

g = Graph(2)
print(g.vertices)
print(g.edges)

