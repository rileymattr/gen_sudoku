class Graph:
	def __init__(self, n: int):
		#Degree of a vertex is 2((n**2)-1)+(n**2)-2n+1
		self.size = n
		self.vertices = [0]*(self.size**4)
		self.edges = []
		for i in range(self.size**4):
			self.edges.append([])
		
		#This will be used to dynamically track the saturation degree of each vertex, by tracking the size of the set of colors a vertex is adjacent to.
		self.sat_degree = []
		for i in range(self.size**4):
			self.sat_degree.append(set())

		for y in range(self.size**2):
			for x in range(self.size**2):
				edges = self.edges[((n**2)*y) + x]
				x_region = int(x/self.size)
				y_region = int(y/self.size)
				
				#This adds edges to cells in the same region.
				for x_prime in range(0,self.size):
					for y_prime in range(0,self.size):
						if (x_region*self.size) + x_prime != x or (y_region*self.size) + y_prime != y:
							edges.append((self.size)*(y_region+y_prime)+(x_region+x_prime))

				#This adds edges to cells in the same column, outside the same region. 		
				for row in range(n**2):
					if int(row/self.size) != x_region:
						edges.append((self.size*y)+row)

				#This adds edges to the cells in the sme row, outside the same region.
				for col in range(n**2):
					if int(col/self.size) != y_region:
						edges.append((self.size*col)+x)

	def __str__(self):
		board = ''

		for y in range(self.size**2):
			row = ''
			for x in range(self.size**2):
				if self.vertices[((self.size**2)*y)+x] == 0:
					row +=' #'
				else:
					row += ' '+str(self.vertices[((self.size**2)*y)+x])
				if (x+1)%self.size == 0:
					row += '  '
			
			board += row+'\n'
		
			if (y+1)%self.size == 0:
				board += '\n'
			
		return board

	def update_sat_degree(self, vertex, color):
		if color == 0:
			raise Exception('Invalid argument')
		else:
			for neighbor in self.edges[vertex]:
				self.sat_degree[neighbor].add(color)

	def initial_assignment(self, file_name):
		f = open(file_name)
		lines = f.read().split()
		if len(lines) != (self.size**4):
			raise Exception('The given file does not contain the correct number of arguments.')
		else:
			for c in range(len(lines)):
				if int(lines[c]) >= 0 and int(lines[c]) <= (self.size**2):
					self.vertices[c] = int(lines[c])
					if int(lines[c]) != 0:
						self.update_sat_degree(c,int(lines[c]))

				else:
					raise Exception('The given file contains invalid arguments.')
	
	def check_cell_color(self, vertex):
		for neighbor in range(len(self.edges[vertex])):
			if self.vertices[vertex] == self.vertices[neighbor] and neighbor != vertex:
				return False
		return True