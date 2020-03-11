import numpy as np

from problem.abstractProblem import Problem
from tools.terrainHandler import TerrainHandler
import matplotlib.pyplot as plt
from scipy.spatial import distance


class TerrainProblem(Problem):

    def goalFunction(self, values):
        points = []
        for i in range(0,len(values),2):
            points.append([values[i],values[i+1]])
        return points

    def adaptationFunction(self, values:[]):
        # settings
        distanceMax = 150
        costMax = 1200
        startPoint = [0,0]
        endPoint = [140, 60]

        # składowa dystansu
        distanceElement = TerrainHandler.distance((values[3][0], values[3][1]), endPoint)

        # skladowa kosztu podróży
        cost = 0
        values.insert(0,[0,0])
        for i in range(0,len(values)-1):
            cost = cost + TerrainHandler.travelCost(values[i], values[i+1])

        # print("distanceElement:",distanceElement,", cost of travel: ", cost,"adaptation",1000*(distanceMax - distanceElement)/distanceMax + 1000*(costMax-cost)/costMax)
        return 4000*(distanceMax - distanceElement)/distanceMax + 3000*(costMax-cost)/costMax
