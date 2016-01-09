__author__ = 'bilge'

from itertools import permutations
import numpy as np

def total_distance(way, coordinates):
    """
     Returns the length of the path passing throught
    all the points in the given order.
    :param way:
    :param coordinates:
    :return:
    """
    total_path = np.float64(0.0)
    for i in range(len(way)):
        for j in range(len(way[i])-1):
                total_path += np.sqrt(np.power((coordinates[way[i][j]][0] - coordinates[way[i][j+1]][0]), 2)
                                      + np.power((coordinates[way[i][j]][1] - coordinates[way[i][j+1]][1]), 2))
    return np.around(total_path,decimals=1)


def distance(point1, point2):
    """
    Returns the Euclidean distance of two points in the Cartesian Plane.

    distance([3,4],[0,0])
    5.0
    distance([3,6],[10,6])
    7.0
    """
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

"""
def total_distance(points):

    Returns the length of the path passing throught
    all the points in the given order.

    total_distance([[1,2],[4,6]])
    5.0
    total_distance([[3,6],[7,6],[12,6]])
    9.0

    return np.around(sum([distance(point, points[index + 1]) for index, point in enumerate(points[:-1])]), decimals=1)
"""
def optimized_way(points, start=None):
    """
    As solving the problem in the brute force way is too slow,
    this function implements a simple heuristic: always
    go to the nearest city.

    Even if this algoritmh is extremely simple, it works pretty well
    giving a solution only about 25% longer than the optimal one (cit. Wikipedia),
    and runs very fast in O(N^2) time complexity.

    optimized_travelling_salesman([[i,j] for i in range(5) for j in range(5)])
    [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 4], [1, 3], [1, 2], [1, 1], [1, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 4], [3, 3], [3, 2], [3, 1], [3, 0], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
    optimized_travelling_salesman([[0,0],[10,0],[6,0]])
    [[0, 0], [6, 0], [10, 0]]
    """
    if start is None:
        start = points[0]
    must_visit = points
    path = [start]
    must_visit.remove(start)
    while must_visit:
        nearest = min(must_visit, key=lambda x: distance(path[-1], x)) #key lambda ?
        path.append(nearest)
        must_visit.remove(nearest)
    return path


def find_path_for_vehicles(capacities, indexes, max_capacity):
    """

    :param capacities:
    :param indexes:
    :param max_capacity:
    :return:result

    find result array in terms of maximum capacity
    """
    total_capacity = 0
    j = 0
    result = []
    for i in range(len(indexes)):
        if (total_capacity + capacities[indexes[i]]) <= max_capacity:
            total_capacity += capacities[indexes[i]]
            result.append(indexes[i])
        else:
            print(total_capacity)
            total_capacity = 0
            result.append(-1)
            total_capacity = capacities[indexes[i]]
            result.append(indexes[i])
    return result

def optimalMi():
    print(" ", 0, end='\n')


def find_index(points, nearest_path):
    """
    for nearest way,
    aimed to find its index number to check capacity values
    """
    indexes = []
    for i in range(len(nearest_path)):
        for j in range (len(points)):
            if points[j] == nearest_path[i]:
                indexes.append(j)
                break
    return indexes

def find_max_column(result):
    """
    :param result
    :return:maxColumn
    define column number i have to learn from result array in terms of -1.
    """
    counter=0
    maxColumn = 0
    for i in range(len(result)):
        if result[i] != -1:
            counter +=1
        elif result[i] == -1 and maxColumn < counter :
            maxColumn = counter
            counter=0
        else:
            counter = 0
    return maxColumn

def convert_solution(result):
    max_column = find_max_column(result) + 2 #reason: add 0 at the beginning and end
    normalized_result = np.zeros((vehicle_num,max_column), dtype=np.uint32)
    normalized_result.shape
    k=0
    i=1 #problem yaratabilir kontrol et mutlaka
    while k < vehicle_num:
        for j in range(1,max_column):
            if i < len(result):
                if result[i] != -1:
                    normalized_result[k][j] = result[i]
                    i += 1
                else:
                    i += 1
                    break
            else:
                return normalized_result
        k += 1
    return normalized_result

def print_solution(converted_result):
    j=0
    for i in range(len(converted_result)):
        counter=0
        j=0
        while(j<len(converted_result[i])):
            if(converted_result[i][j] == 0):
                counter += 1
            if(counter <= 2):
                print(converted_result[i][j], end=" ")
            j += 1
        print(end="\n")

with open("data/vrp_26_8_1") as f:
    counter = np.uint16
    vehicle_num = np.uint8
    max_capacity = np.uint16
    #### take main parameters
    temp = f.readline()
    temp = temp.split(" ")
    counter = int(temp[0])
    vehicle_num = int(temp[1]) #4
    max_capacity = int(temp[2]) #10
    capacities = []
    coordinates = []
    j = 0
    ### get rest of them as a float
    data = [list(map(float, line.split())) for line in f]
    #kapasite ve koordinatları ayri degerlendirmek icin
    for i in range(counter):
        if (i < counter):
            capacities.append(data[i][0])
            coordinates.append([])
            coordinates[i].append(data[i][1])
            coordinates[i].append(data[i][2])

    #find total path
    total_path = np.float64(0)
    normalized_result = np.ndarray
    temp = tuple(coordinates)
    path = optimized_way(coordinates)
    #total_path = total_distance(path)
    indexes = find_index(temp,path)
    result = find_path_for_vehicles(capacities,indexes,max_capacity)
    normalized_result = convert_solution(result)
    total_path = total_distance(normalized_result, temp)
    print(total_path, 0, sep=" ",end="\n")
    print(indexes)
    print_solution(normalized_result)