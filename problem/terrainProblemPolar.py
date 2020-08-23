import numpy as np

from problem.abstractProblem import Problem
from tools.terrainHandler import TerrainHandler
import matplotlib.pyplot as plt
from scipy.spatial import distance


class TerrainProblemPolar(Problem):
    def fenotypeFunction(self, values):
        points = []
        currentPosition = TerrainHandler.getWaypoints()[0]

        for i in range(0, len(values), 2):
            fi = values[i]
            r = values[i + 1]
            currentPosition = TerrainHandler.getNextStepPosition(currentPosition, fi, r)
            points.append(currentPosition)
        return points

    def adaptationFunction(self, values: []):
        costFunction = lambda x: 187.5 * (pow(1.028, x * 100))
        # settings
        startPoint = TerrainHandler.getWaypoints()[0]
        endPoint = TerrainHandler.getWaypoints()[1]

        distanceMax = TerrainHandler.distance(startPoint, endPoint)
        costMax = 10000

        valuesLoc = values.copy()
        if len(valuesLoc) > 0:
            # składowa dystansu - ostatni element do endpoint
            distanceElement = TerrainHandler.distance(
                (valuesLoc[len(valuesLoc) - 1][0], valuesLoc[len(valuesLoc) - 1][1]), endPoint
            )

            # skladowa kosztu podróży
            cost = 0
            valuesLoc.insert(0, startPoint)
            for i in range(len(valuesLoc) - 1):
                cost = cost + TerrainHandler.travelCost(valuesLoc[i], valuesLoc[i + 1])

            adaptationVal = 5000 * (
                distanceMax - distanceElement
            ) / distanceMax + costFunction((costMax - cost) / costMax)
            return adaptationVal if adaptationVal > 0 else 0
        else:
            return 0
