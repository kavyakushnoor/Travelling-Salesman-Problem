import random
import math
import numpy as np
import statistics
import itertools
import matplotlib.pyplot as plt

def cityList():
    #Generate random x,y values for a list of 14 cities on a 1000*1000 plane
    cityList1 = []
    for x in range(1, 15):
        x = random.randint(0, 1001)
        y = random.randint(0, 1001)
        city = x, y
        cityList.append(city)
    return cityList1

cityList = [(541, 826), (334, 640), (736, 769), (350, 258), (173, 956), (779, 392), (164, 461), (941, 218), (884, 795),
            (340, 640), (426, 168), (473, 298), (510, 67), (139, 655)]

def distance(p1, p2):
    #Calculate disance between 2 given points
    if p1 == p2:
        distance = math.inf
    else:
        distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    return round(distance, 2)

def max_distance():
    #13 times the diagnol representing maximum value
    return round(distance((0, 0), (1000, 1000)) * 13, 2)

def total_distance(points):
    #Sum of distances between all points in a given list
    return round(sum([distance(point, points[index + 1]) for index, point in enumerate(points[:-1])]), 2)

def origin_dist(p1):
    # Distance of each point from the origin
    return distance((0, 0), p1)

def cityDict():
    dict = {}
    for x in cityList:
        dict[origin_dist(x)] = x
    return dict

def sortedCity():
    sortedCity1 = []
    dict = cityDict()
    for key in sorted(dict.keys()):
        sortedDict = dict[key]
        sortedCity1.append(sortedDict)
    return sortedCity1

sortedCity = sortedCity()
def eachDistance():
    a = []
    for x in sortedCity:
        for y in sortedCity:
            item = distance(x, y)
            a.append(item)
    return a

#print ('sortedList: ', sortedCity)
print('sorted Total: ', total_distance(sortedCity))

a = eachDistance()
def matrix():
    mat = []
    for z in range(14):
        row = []
        for q in range(14):
            row.append(a.pop())
        mat.append(row)
    return mat

def print_matrix():
    c = np.reshape(a, (14, 14))
    return c

def optimized_travelling_salesman(points, start=None):
    if start is None:
        start = points[0]
    must_visit = points
    path = [start]
    must_visit.remove(start)
    while must_visit:
        nearest = min(must_visit, key=lambda x: distance(path[-1], x))
        path.append(nearest)
        must_visit.remove(nearest)
    return path

mat = matrix()
def opt_path():
    opt_path = [0]
    for z in mat:
        opt_index = z.index(min(z))
        if opt_index not in opt_path:
            opt_path.append(opt_index)
        else:
            pass
    return opt_path

opt_path = opt_path()
def rem_cities():
    rem_cities = []
    for x in range(0, 13):
        if x not in opt_path:
            rem_cities.append(x)
    return rem_cities

rem_cities = rem_cities()
def opt_pathPoints():
    opt_pathPoints = []
    for x in opt_path:
        opt_pathPoints.append(sortedCity[x])
    rem_citiesPoints = []
    for x in rem_cities:
        rem_citiesPoints.append(sortedCity[x])
    rem_citiesPoints.append(opt_pathPoints[-1])
    newRemList = (optimized_travelling_salesman(rem_citiesPoints, opt_pathPoints[-1]))
    opt_pathPoints.pop()
    for x in newRemList:
        opt_pathPoints.append(x)
    return opt_pathPoints

optList = [(350, 258), (426, 168), (510, 67), (473, 298), (779, 392), (941, 218), (884, 795), (736, 769), (541, 826),
           (340, 640), (334, 640), (139, 655), (164, 461), (173, 956)]
myOpt = [(350, 258), (426, 168), (779, 392), (139, 655), (473, 298), (340, 640), (334, 640), (884, 795), (736, 769),
         (541, 826), (173, 956), (164, 461), (510, 67), (941, 218)]

print('Random Total: ', total_distance(cityList))
print('myOptTotal:', total_distance(myOpt))
print('optTotal/ minimum: ', total_distance(optList))
print ("max distance: ", max_distance())

total = 0
count = 0
sos = 0
median =0
distances = []
for p in itertools.permutations(cityList):
    t = total_distance(p)
    sos += t*t
    count +=1
    if count < 31:
        distances.append(t)
    if count == 100000:
        break
    total += t
    average = total/count
    stdev = math.sqrt((sos-((total*total)/count))/count)
distances.sort()
print ('total: ', total)
print ('average:', average)
print ('stdev:', stdev)
print ('median: ', distances[15])
plt.hist(distances, normed=True, bins=5, histtype='bar', stacked=True, color='c',edgecolor='black', linewidth=1.2)
plt.axvline(average, color='b', linestyle='dashed', linewidth=2)
plt.ylabel('Histogram of Sample Distances')
plt.show()
'''
print ('mat: ', mat)
print ('mypathList: ', opt_pathPoints())
print('optList: ', optimized_travelling_salesman(sortedCity))
print('randList: ', cityList)
'''