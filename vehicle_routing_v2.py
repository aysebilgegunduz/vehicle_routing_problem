__author__ = 'bilge'

import numpy as np

class AntVRP:
    #original amount of trail
    c = np.float64(1.0)
    #trail preference
    alpha = np.float64(1)
    #greedy preference
    beta = np.float64(5)
    #trail evaporation coefficient
    evaporation = np.float64(0.5)
    #new trail deposit coefficient
    Q = np.float64(500)
    #number of ants used = numAntFactor*numTowns
    numAntFactor = np.float64(0.8)
    #probability of pure random selection of the next town
    pr = np.float64(0.01)

    maxIteration = np.uint16(2000)
    #towns
    n = np.uint16(0)
    #ants
    m = np.uint16(0)
    graph = np.array(dtype=np.float64)
    trails = np.array(dtype=np.float64)
    probs = np.array(dtype=np.float64)
    bestTour = np.array(dtype=np.int_)
    bestTourLength = np.float64
    currentIndex = np.uint16(0)
    class Ant:
        tour = np.zeros(len(AntVRP.graph))
        visited = np.zeros(len(AntVRP.graph))
        def __init__(self, tour, visited):
            self.tour = tour
            self.visited = visited

        def clear(self):
            for i in range(AntVRP.n):
                self.visited[i] = 1

        def tourLength(self):
            length = AntVRP.graph[AntVRP.tour[AntVRP.n - 1]][AntVRP.tour[0]]
            for i in range(AntVRP.n-1):
                length = length + AntVRP.graph[AntVRP.tour[i]][AntVRP.tour[i + 1]]
            return(length)

        def visited_(i):
            return(visited[i])

        def visitTown(town):
            AntVRP.tour[AntVRP.currentIndex + 1] = town
            visited[town] = 0

        ants = Ant()


    """
    private Ant ants[] = null;
    private Random rand = new Random();

    """




with open("data/vrp_5_4_1") as f:
    counter = np.uint16
    vehicle_num = np.uint8
    max_capacity = np.uint16
    #### take main parameters
    temp=f.readline()
    temp = temp.split(" ")
    counter = np.uint16(temp[0])
    vehicle_num = np.uint8(temp[1])
    max_capacity = np.uint16(temp[2])

    ### get rest of them as a float
    data = [list(map(np.float64, line.split())) for line in f]

    for i in range(vehicle_num):
        print(i)