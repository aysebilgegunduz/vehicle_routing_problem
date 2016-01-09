__author__ = 'bilge'
"""
http://web.mit.edu/urban_or_book/www/book/chapter6/6.4.12.html
https://github.com/razvanilin/clark-wright-vrp/blob/master/src/com/nightingale/main/VRSolution.java
http://www.mafy.lut.fi/study/DiscreteOpt/CH6.pdf
"""
import numpy as np
from collections import namedtuple
import networkx as nx
import itertools
import copy

Route = nx.Graph()

Item = namedtuple("Item", ['index', 'x', 'y', 'capacity','used'])
Savings = namedtuple("Savings", ['i','j','value'])

def in_route(i,j,tour):
    counter = 0
    for t in range(0,len(tour)):
        for k in range (0,len(tour[t])):
            if(tour[t][k] == i):
                counter += 1
                index = i
            if(tour[t][k] == j):
                counter += 1
                index = j
            if(counter == 2):
                break
            elif(counter == 1):
                return index
    return counter

def has_edge(G, edge):
    for u in G.nodes(data=True):
        if Route.has_edge(u[0],edge):
            return True
    return False

def checkObjectives(orderedSavings, items, vehicle_count, vehicle_capacity):
    vehicle_tours = []
    tempItems = set(items)
    used = set()
    for v in range(0,vehicle_count):
        vehicle_tours.append([])
        capacity_remaining = vehicle_capacity
        counter = len(tempItems)
        if(counter != 1):
            for k in range(0,len(orderedSavings)):
                #check if any of them in route
                temp1 = capacity_remaining - (items[orderedSavings[k].i].capacity + items[orderedSavings[k].j].capacity)
                temp2 = capacity_remaining - items[orderedSavings[k].i].capacity
                temp3 = capacity_remaining - items[orderedSavings[k].j].capacity
                if (Route.__len__() == 0 and \
                        (has_edge(Route, orderedSavings[k].i) == False and has_edge(Route, orderedSavings[k].j) == False )) \
                        and (temp1 >= 0) and items[orderedSavings[k].i].used == False and items[orderedSavings[k].j].used == False:

                    Route.add_edge(items[0].index, orderedSavings[k].i)
                    Route.add_edge(orderedSavings[k].i,orderedSavings[k].j)
                    Route.add_edge(orderedSavings[k].j, items[0].index)
                    capacity_remaining -= items[orderedSavings[k].i].capacity + items[orderedSavings[k].j].capacity
                    tempItems.remove(items[orderedSavings[k].i])
                    tempItems.remove(items[orderedSavings[k].j])
                    items[orderedSavings[k].i] = items[orderedSavings[k].i]._replace(used = True)
                    items[orderedSavings[k].j] = items[orderedSavings[k].j]._replace(used = True)
                elif has_edge(Route, orderedSavings[k].i) ^ has_edge(Route, orderedSavings[k].j):
                    if Route.has_edge(items[0].index, orderedSavings[k].i) and temp3>=0 and items[orderedSavings[k].j].used == False:
                        Route.add_edge(items[0].index, orderedSavings[k].j)
                        Route.add_edge(orderedSavings[k].j, orderedSavings[k].i)
                        Route.remove_edge(items[0].index,orderedSavings[k].i)
                        capacity_remaining -= items[orderedSavings[k].j].capacity
                        tempItems.remove(items[orderedSavings[k].j])
                        items[orderedSavings[k].j] = items[orderedSavings[k].j]._replace(used = True)
                    elif Route.has_edge(items[0].index, orderedSavings[k].j) and temp2>=0 and  items[orderedSavings[k].i].used == False:
                        Route.add_edge(items[0].index, orderedSavings[k].i)
                        Route.add_edge(orderedSavings[k].i, orderedSavings[k].j)
                        Route.remove_edge(items[0].index,orderedSavings[k].j)
                        capacity_remaining -= items[orderedSavings[k].i].capacity
                        tempItems.remove(items[orderedSavings[k].i])
                        items[orderedSavings[k].i] = items[orderedSavings[k].i]._replace(used = True)
                elif (Route.__len__() == 0 and \
                        (has_edge(Route, orderedSavings[k].i) == False and has_edge(Route, orderedSavings[k].j) == False )) \
                        and (temp1 >= 0) and (items[orderedSavings[k].i].used ^ items[orderedSavings[k].j].used):

                    if items[orderedSavings[k].i].used == False:
                        Route.add_edge(items[0].index, orderedSavings[k].i)
                        Route.add_edge(orderedSavings[k].i, items[0].index)
                        capacity_remaining -= items[orderedSavings[k].i].capacity
                        tempItems.remove(items[orderedSavings[k].i])
                        items[orderedSavings[k].i] = items[orderedSavings[k].i]._replace(used = True)
                    elif items[orderedSavings[k].j].used == False:
                        Route.add_edge(items[0].index, orderedSavings[k].j)
                        Route.add_edge(orderedSavings[k].j, items[0].index)
                        capacity_remaining -= items[orderedSavings[k].j].capacity
                        tempItems.remove(items[orderedSavings[k].j])
                        items[orderedSavings[k].j] = items[orderedSavings[k].j]._replace(used = True)
        elif counter <= 1:
            Route.add_edge(items[0].index,items[0].index)
        if Route.__len__() != 0:
            vehicle_tours[v].append(Route)
            print(Route.edges())
            print(Route.nodes())
            used.add(capacity_remaining)
            print(capacity_remaining)
            Route.clear()

def normalize_Route(G):
    for e,v in G.edges_iter():


def calculate_distance(i,j):
    """
    calculate the distance between two customer
    :param i:
    :param j:
    :return: distance_value
    """
    distance = np.sqrt(np.power((i.x-j.x),2) + np.power((i.y-j.y),2))
    return distance

def calculate_savings(depot, i,j):
    """
    :param depot: where to start
    :param i: from
    :param j: to or vice versa
    :return:savingValue
    """
    savingValue = calculate_distance(i,depot) + calculate_distance(j,depot) - calculate_distance(i,j)
    return savingValue

def determinePath(input_data):
    # parse the input
    lines = input_data.split('\n')

    item_count, vehicle_num, max_cap = map(float, lines[0].split())
    item_count = int(item_count)
    vehicle_num = int(vehicle_num)

    items = []
    for i in range(1, item_count+1):
        cap,x,y = map(float, lines[i].split())
        items.append(Item(i-1, x, y, cap, False))
    savings = []
    depot = items[0]
    #calculate savings
    for i in range(1,item_count):
        for j in range(i+1,item_count):
            savings.append(Savings(items[i].index,items[j].index,calculate_savings(depot,items[i],items[j])))
    #sort savings descending order
    savings_sorted = sorted(savings, key = lambda i: i.value, reverse = True)
    return checkObjectives(savings_sorted,items,vehicle_num,max_cap)
with open("data/vrp_26_8_1") as f:
    input_data = ''.join(f.readlines())
    determinePath(input_data)