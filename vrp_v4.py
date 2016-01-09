__author__ = 'bilge'
import numpy as np
import sys

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

def sort_capacities(capacities):
    """
    bubble sort
    :param capacities:
    :return: indexes
    """
    indexes = [i for i in range(counter)]
    for i in range(len(capacities)):
        for j in range(len(capacities)-1-i):
            if capacities[j] < capacities[j+1]:
                capacities[j], capacities[j+1] = capacities[j+1], capacities[j]
                indexes[j],indexes[j+1] = indexes[j+1], indexes[j]

    return capacities,indexes


def optimized_solution(capacities, indexes, max_capacities):
    """
    find solution array
    :param capacities:
    :param indexes:
    :param max_capacities:
    :return: result
    """
    result = []
    total_capacity = []
    i = 0
    j=0
    while i < vehicle_num:
        result.append([])
        result[i].append(0)
        total_capacity.append(0)
        i += 1
    i = 0
    while i < (len(indexes)-1):
        if (j < vehicle_num) and ((total_capacity[j] + capacities[i]) <= max_capacity):
            total_capacity[j] = capacities[i] + total_capacity[j]
            result[j].append(indexes[i])
            j += 1
            i += 1
        elif j >= vehicle_num:
            j = 0
        else:
            j += 1
    i = 0
    while i < vehicle_num:
        result[i].append(0)
        i += 1
    return result

def print_solution(path):
    for i in range(len(path)):
        for j in range(len(path[i])):
            print(path[i][j], end=" ")
        print(end="\n")

with open(sys.argv[1]) as f:
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
    capacities, indexes = sort_capacities(capacities)
    path = optimized_solution(capacities,indexes,max_capacity)
    total_dist = total_distance(path, coordinates)
    print(total_dist,end="\n")
    print_solution(path)