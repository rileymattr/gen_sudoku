class Graph:
	def __init__(self, n: int):
		self.size = n
		self.vertices = []
		for i in range(self.size**2):
			self.vertices.append([0]*(self.size**2))
		self.edges = []
		for i in range(self.size**4):
			self.edges.append([])

		for y in range(self.size**2):
			for x in range(self.size**2):
				edges = self.edges[((n**2)*y) + x]
				x_region = int(x/self.size)
				y_region = int(y/self.size)
				
				#This adds edges to cells in the same region.
				for x_prime in range(0,self.size):
					for y_prime in range(0,self.size):
						if (x_region*self.size) + x_prime != x or (y_region*self.size) + y_prime != y:
							edges.append(((x_region*self.size) + x_prime, (y_region*self.size) + y_prime))

				#This adds edges to cells in the same column, outside the same region. 		
				for row in range(n**2):
					if int(row/self.size) != x_region:
						edges.append((row,y))

				#This adds edges to the cells in the sme row, outside the same region.
				for col in range(n**2):
					if int(col/self.size) != y_region:
						edges.append((x,col))

	def __str__(self):
		board = ''
		horizontal_edge = ''
		for i in range((self.size**2)+(self.size-1)+2):
			horizontal_edge += '-'
		board += horizontal_edge+'\n'

		for y in range(self.size**2):
			row = '|'
			for x in range(self.size**2):
				if self.vertices[y][x] == 0:
					row +=' '
				else:
					row += str(self.vertices[y][x])
				if (x+1)%self.size == 0:
					row += '|'
			
			board += row+'\n'
		
			if (y+1)%self.size == 0:
				board += horizontal_edge+'\n'
			
		return board

	def initial_assignment(self, file_name):
		f = open(file_name)
		lines = f.read().split()
		if len(lines) != (self.size**4):
			raise Exception('The given file does not contain the correct number of arguments.')
		else:
			for c in range(len(lines)):
				if int(lines[c]) >= 0 and int(lines[c]) <= (self.size**2):
					y = int(c/(self.size**2))
					x = c - (y*(self.size**2))
					self.vertices[y][x] = int(lines[c])
				else:
					raise Exception('The given file contains invalid arguments.')