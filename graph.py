class Graph:
	def __init__(self, n: int):
		#Degree of a vertex is 2((n**2)-1)+(n**2)-2n+1
		self.size = n
		self.vertices = [0]*(self.size**4)
		self.edges = []
		for i in range(self.size**4):
			self.edges.append(set())
		
		for v in range(self.size**4):
			y = int(v/self.size**2)
			x = v-(y*self.size**2)

			x_block = int(x/self.size)
			y_block = int(y/self.size)

			#add edges to cells in the same block
			for x_prime in range(self.size):
				for y_prime in range(self.size):
					u = y_block*(self.size**3)+y_prime*(self.size**2) + x_block*(self.size)+x_prime
					if v != u:
						self.edges[v].add(u)
			
			for x_prime in range(self.size**2):
				u = (y*(self.size**2)) + x_prime
				if v != u:
					self.edges[v].add(u)

			for y_prime in range(self.size**2):
				u = (y_prime*(self.size**2)) + x
				if v != u:
					self.edges[v].add(u)

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

	def initial_assignment(self, file_name):
		f = open(file_name)
		lines = f.read().split()
		if len(lines) != (self.size**4):
			raise Exception('The given file does not contain the correct number of arguments.')
		else:
			for c in range(len(lines)):
				if int(lines[c]) >= 0 and int(lines[c]) <= (self.size**2):
					self.vertices[c] = int(lines[c])
				else:
					raise Exception('The given file contains invalid arguments.')
	
	def cell_color_valid(self, vertex):
		for u in self.edges[vertex]:
			if self.vertices[vertex] == self.vertices[u]:
				return False
		return True
