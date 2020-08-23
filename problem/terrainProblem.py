import numpy as np

from problem.abstractProblem import Problem
from tools.terrainHandler import TerrainHandler
import matplotlib.pyplot as plt
from scipy.spatial import distance


class TerrainProblem(Problem):
    def fenotypeFunction(self, values):
        points = []
        for i in range(0, len(values), 2):
            points.append([values[i], values[i + 1]])
        return points

    def adaptationFunction(self, values: []):
        costFunction = lambda x: 187.5 * (pow(1.028, x * 100))
        # settings
        startPoint = TerrainHandler.getWaypoints()[0]
        endPoint = TerrainHandler.getWaypoints()[1]

        distanceMax = TerrainHandler.distance(startPoint, endPoint)
        costMax = 10000

        # sprawdzenie czy sa punkty do przejscia
        valuesLoc = values.copy()
        if len(valuesLoc) < 1:
            return 0

        # składowa dystansu - ostatni element do endpoint
        distanceElement = TerrainHandler.distance(
            (valuesLoc[len(valuesLoc) - 1][0], valuesLoc[len(valuesLoc) - 1][1]), endPoint
        )

        # skladowa kosztu podróży
        cost = 0
        valuesLoc.insert(0, startPoint)
        for i in range(0, len(valuesLoc) - 1):
            cost = cost + TerrainHandler.travelCost(valuesLoc[i], valuesLoc[i + 1])

        adaptationVal = 5000 * (
            distanceMax - distanceElement
        ) / distanceMax + costFunction((costMax - cost) / costMax)
        return adaptationVal if adaptationVal > 0 else 0
