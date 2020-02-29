import numpy as np

from problem.abstractProblem import Problem
from tools.terrainHandler import TerrainHandler
import matplotlib.pyplot as plt
from scipy.spatial import distance


class TerrainProblem(Problem):
    TerrainHandler.setName("ctype")

    def goalFunction(self, values):
        points = []
        for i in range(0,len(values),2):
            points.append([values[i],values[i+1]])
        return points

    def adaptationFunction(self, values):
        # składowa dystansu
        point1, point2 = (values[2][0], values[2][1]), (140, 10)
        distanceElement = 1500 - TerrainHandler.distance(point1, point2)

        # toughness

        cost = 0
        # cost of travel
        for i in range(0,len(values)-1):
            a, b = TerrainHandler.slope(values[i], values[i+1])
            for x in range(min(values[i][0], values[i+1][0]), max(values[i][0], values[i+1][0])):
                y = int(round(a * x + b))
                cost = cost + TerrainHandler.getTerrainToughness(x, y)

        # print("cost of travel: ", cost)
        values = [[0,0]] + values + [[140,10]]

        return distanceElement + 3000-2*cost
