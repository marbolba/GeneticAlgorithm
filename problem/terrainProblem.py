import numpy as np

from problem.abstractProblem import Problem
from tools.terrainHandler import TerrainHandler
import matplotlib.pyplot as plt
from scipy.spatial import distance


class TerrainProblem(Problem):
    TerrainHandler.setName("ctype2")

    def goalFunction(self, values):
        points = []
        for i in range(0,len(values),2):
            points.append([values[i],values[i+1]])
        return points

    def adaptationFunction(self, values):
        # settings
        distanceMax = 150
        costMax = 1200
        # składowa dystansu
        point1, point2 = (values[2][0], values[2][1]), (140, 60)
        distanceElement = TerrainHandler.distance(point1, point2)

        # toughness

        cost = 0
        # cost of travel
        for i in range(0,len(values)-1):
            cost = cost + TerrainHandler.travelCost(values[i], values[i+1])
        # print("distanceElement:",distanceElement,", cost of travel: ", cost,"adaptation",1000*(distanceMax - distanceElement)/distanceMax + 1000*(costMax-cost)/costMax)
        return 1000*(distanceMax - distanceElement)/distanceMax + 3000*(costMax-cost)/costMax
