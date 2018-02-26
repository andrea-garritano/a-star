import fileinput

# Vertex implementation
class Vertex:
	# Initialization of a vertex, given a neighbor and the corresponding weight
	# Each vertex contains a list of neighbors and corresponding weights
	def __init__(self,i,neighbor_index,weight):
		self.index = i
		self.neighbors = [neighbor_index]
		self.weights = [weight]

	# Add a neighbor with corresponding weight to the vertex
	def addNeighbor(self,neighbor_index,weight):
		self.neighbors.append(neighbor_index)
		self.weights.append(weight)

	def getNeighbors(self):
		return self.neighbors

	def getWeight(self, neighbor_index):
		return self.weights[self.neighbors.index(neighbor_index)]

# Graph data structure
class Graph:
	# Initializes a graph with n_vertices nodes
	# The graph contains a list of vertices
	def __init__(self,n_vertices):
		self.vertices = [None]*n_vertices
		self.num_vertices = len(self.vertices)

	# Returns the i'th node
	def getVertex(self, i):
		if ((i >= len(self.vertices)) | (i < 0)):
			return None
		else :
			return self.vertices[i]

	# Adds a new vertex to the graph
	def addVertex(self, vertex_index, neighor_index, distance):
		if (self.vertices[vertex_index] == None):
			# Construct new vertex
			self.vertices[vertex_index] = Vertex(vertex_index, neighor_index, distance)
		else:
			# Vertex already in graph but other neighbor, add extra edge
			self.vertices[vertex_index].addNeighbor(neighor_index, distance)

# Read graph data
def readGraph(filePath):
	n_vertices = 0
	for line in fileinput.input([filePath]):
		words = line.split(" ")
		if (words[0] == "p"):
			n_vertices = int(words[2])
	graph = Graph(n_vertices)
	for line in fileinput.input([filePath]):
		words = line.split(" ")
		if (words[0] == "a"):
			graph.addVertex(int(words[1])-1, int(words[2])-1, float(words[3]))
	return graph

# read coordinates data
def readCoordinates(filepath):
	coordinates = []
	for line in fileinput.input([filepath]):
		words = line.split(" ")
		if (words[0] == "v"):
			coordinates.append([float(words[2]), float(words[3])])
	return coordinates
