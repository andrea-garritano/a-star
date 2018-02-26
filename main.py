from astar import *


def main():
    graph = readGraph('./data/USA-road-d.NY.gr')
    print 'Graph read: DONE'
    import random
    random.seed(50)
    N = graph.num_vertices
    start = random.randint(0, N-1)
    goal = random.randint(0, N-1)
    print 'start '+str(start)
    print 'goal '+str(goal)
    (cameFrom, f) = a_star_search(graph, start, goal)
    i = goal
    k = 1
    while cameFrom[i] != None:
        print cameFrom[i]
        i = cameFrom[i]
        k=k+1
    print 'n: '+str(k)
    print f[goal]
    #a_star_search(graph, 1, 12)
if  __name__ =='__main__':main()
