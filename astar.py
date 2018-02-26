import math
import copy

from graph import *
import heapq


# Read graph data and coordinates data (to be implemented)
coordinates = readCoordinates('./data/USA-road-d.NY.co')
print 'Coordinates read: DONE'

###########################################
########## A* implementation ##############
###########################################

# Priority queue definition
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def find(self, id):
        for element in self.elements:
            if (id == element[1]):
                return True
        return False


# Heuristic function (to be implemented)
def h(pos1, pos2):
    return math.sqrt(math.pow(coordinates[pos1][0]-coordinates[pos2][0],2) + math.pow(coordinates[pos1][1]-coordinates[pos2][1],2))

def h2(pos1,pos2):
  return math.fabs((coordinates[pos1][0]-coordinates[pos2][0])+(coordinates[pos1][1]-coordinates[pos2][1]))

def a_star_search(graph, start, goal):
    closed = [None]*graph.num_vertices # initialize the closed array
    cameFrom = [None]*graph.num_vertices # initialize the cameFrom array;
                                         # for each node, which node it can most efficiently be reached from
    g = [999999999]*graph.num_vertices # map g with default value of infinite
    f = [99999999]*graph.num_vertices # map f with default value of infinite
    open = PriorityQueue() # initialize open with a priority queue
    open.put(start, 0) # put the start node in open array
    cameFrom[start] = None # set the father of the start node to None
    g[start]=0 # set the cost so far of the start node equals to 0
    f[start] = h2(start, goal) # calculate the f for the start node
    while not open.empty(): # check if i have node to be expanded
        current = open.get()  # remove and return the index Vertex with lowest f value
        if (current == goal): # check if i've reach the goal node
            return cameFrom, f # return the solution
        closed.append(current) # put the current node in the closed array

        for neighbor in graph.getVertex(current).getNeighbors():
            if neighbor in closed: # skip node already in closed array
                continue
            tentative_g_score = g[current] + graph.getVertex(current).getWeight(neighbor)
            if not open.find(neighbor): # discover a new node
                open.put(neighbor, tentative_g_score) # put the discovered node in the priority queue
            elif tentative_g_score >= g[neighbor]:
                continue # this is not a better path

            # this path is the best until now, so i record all the useful data
            cameFrom[neighbor] = current
            g[neighbor] = tentative_g_score
            f[neighbor] = g[neighbor] + h2(neighbor, goal)

    return None #return the failure of searching the path