import numpy as np

from problem.abstractProblem import Problem
from tools.terrainHandler import TerrainHandler
import matplotlib.pyplot as plt
from scipy.spatial import distance


class TerrainProblem(Problem):
    def goalFunction(self, values):
        points = []
        for i in range(0, len(values), 2):
            points.append([values[i], values[i + 1]])
        return points

    def adaptationFunction(self, values: []):
        # settings
        startPoint = [0, 0]
        endPoint = TerrainHandler.getSize()

        distanceMax = TerrainHandler.distance(startPoint, endPoint)
        costMax = 2000

        # składowa dystansu - ostatni element do endpoint
        distanceElement = TerrainHandler.distance((values[len(values) - 1][0], values[len(values) - 1][1]), endPoint)

        # skladowa kosztu podróży
        cost = 0
        values.insert(0, [0, 0])
        for i in range(0, len(values) - 1):
            cost = cost + TerrainHandler.travelCost(values[i], values[i + 1])

        # print("distanceElement:",distanceElement,", cost of travel: ", cost,"adaptation",1000*(distanceMax - distanceElement)/distanceMax + 1000*(costMax-cost)/costMax)
        adaptationVal = 3000 * (distanceMax - distanceElement) / distanceMax + 4000 * (costMax - cost) / costMax
        return adaptationVal if adaptationVal > 0 else 0
