__author__ = 'bilge'

import numpy as np

def optimalMi():
    print(" ", 0, end='\n')

def uzaklikHesapla(way, coordinates):
    total_path = np.float64(0.0)
    for i in range(len(way)):
        for j in range(len(way[i])-1):
                total_path += np.sqrt(np.power((coordinates[way[i][j]][0] - coordinates[way[i][j+1]][0]), 2)
                                      + np.power((coordinates[way[i][j]][1] - coordinates[way[i][j+1]][1]), 2))
    return np.around(total_path,decimals=1)

def normalizeEt(result):
    j=0
    for i in range(len(result)):
        counter=0
        j=0
        while(j<len(result[i])):
            if(result[i][j] == 0):
                counter += 1
            if(counter <= 2):
                print(result[i][j], end=" ")
            j += 1
        print(end="\n")

    #return temp

with open("data/vrp_26_8_1") as f:
    counter = np.uint16
    vehicle_num = np.uint8
    max_capacity = np.uint16
    #### take main parameters
    temp = f.readline()
    temp = temp.split(" ")
    counter = np.uint16(temp[0]) #5
    vehicle_num = np.uint8(temp[1]) #4
    max_capacity = np.uint16(temp[2]) #10
    total_capacity = np.int_(0) #toplama icin gecici kapasite
    capacities = np.empty(counter, dtype=np.int_) # tum kapasite degerleri
    coordinates = np.empty((counter, 2), dtype=np.float64) #tum koordinatlar

    capacities.shape
    coordinates.shape
    j = 0
    ### get rest of them as a float
    data = [list(map(np.float64, line.split())) for line in f]
    #kapasite ve koordinatları ayri degerlendirmek icin
    for i in range(counter):
        if (i < counter):
            capacities[i] = data[i][0]
            coordinates[i][0] = data[i][1]
            coordinates[i][1] = data[i][2]
    result = np.zeros((vehicle_num, counter + 1), dtype=np.uint16)
    result.shape
    k = 0
    i = 0
    j = 0
    #sonuc matrisini bulabilmek icin
    while j < counter and i< vehicle_num:
        if (total_capacity + capacities[j]) <= max_capacity:
            total_capacity = total_capacity + capacities[j]
            result[i][k] = j
            k += 1
        else:
            total_capacity =0
            i += 1
            k = 1
            j -= 1
        j += 1
    #toplam yolu bul
    total_path = np.float64(0)
    total_path = uzaklikHesapla(result, coordinates) #dogru hesaplamiyor
    print(total_path, 0, sep=" ",end="\n")
    normalizeEt(result)