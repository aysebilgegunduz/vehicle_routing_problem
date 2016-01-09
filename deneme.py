__author__ = 'bilge'
def distance(point1, point2):
    """
    Returns the Euclidean distance of two points in the Cartesian Plane.

    distance([3,4],[0,0])
    5.0
    distance([3,6],[10,6])
    7.0
    """
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5


data = [[0,1],[2,3],[4,5]]
data2 = data
while data2:
    print(min(data2, key=lambda x: distance(data[-1], x)))