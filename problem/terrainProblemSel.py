import numpy as np

from problem.abstractProblem import Problem
from tools.terrainHandler import TerrainHandler
import matplotlib.pyplot as plt
from scipy.spatial import distance


class TerrainProblemSel(Problem):
    def goalFunction(self, values):
        points = []
        for i in range(1, round(values[0]) * 2 + 1, 2):
            points.append([values[i], values[i + 1]])
        return points

    def adaptationFunction(self, values: []):
        costFunction = lambda x: 187.5 * (pow(1.028, x * 100))
        # settings
        startPoint = [0, 0]
        endPoint = [100, 150]

        distanceMax = TerrainHandler.distance(startPoint, endPoint)
        costMax = 10000

        # sprawdzenie czy sa punkty do przejscia
        if len(values) < 1:
            return 0

        # składowa dystansu - ostatni element do endpoint
        distanceElement = TerrainHandler.distance(
            (values[len(values) - 1][0], values[len(values) - 1][1]), endPoint
        )

        # skladowa kosztu podróży
        cost = 0
        values.insert(0, [0, 0])
        for i in range(0, len(values) - 1):
            cost = cost + TerrainHandler.travelCost(values[i], values[i + 1])

        adaptationVal = 5000 * (
            distanceMax - distanceElement
        ) / distanceMax + costFunction((costMax - cost) / costMax)
        return adaptationVal if adaptationVal > 0 else 0
