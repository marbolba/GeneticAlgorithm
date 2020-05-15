import numpy as np

from problem.abstractProblem import Problem
from tools.terrainHandler import TerrainHandler
import matplotlib.pyplot as plt
from scipy.spatial import distance


class TerrainProblemStep(Problem):
    def goalFunction(self, values):
        points = []
        currentPosition = (0, 0)

        for i in range(1, round(values[0]) * 2 + 1, 2):
            fi = values[i]
            r = values[i + 1]
            currentPosition = TerrainHandler.getNextStepPosition(currentPosition, fi, r)
            points.append(currentPosition)
        return points

    def adaptationFunction(self, values: []):
        costFunction = lambda x: 187.5 * (pow(1.028, x * 100))
        # settings
        startPoint = [0, 0]
        endPoint = [200, 20]

        distanceMax = TerrainHandler.distance(startPoint, endPoint)
        costMax = 1500
        # print(values)

        if len(values) > 0:
            # składowa dystansu - ostatni element do endpoint
            distanceElement = TerrainHandler.distance(
                (values[len(values) - 1][0], values[len(values) - 1][1]), endPoint
            )

            # skladowa kosztu podróży
            cost = 0
            values.insert(0, (0, 0))
            for i in range(len(values) - 1):
                cost = cost + TerrainHandler.travelCost(values[i], values[i + 1])

            adaptationVal = 5000 * (
                distanceMax - distanceElement
            ) / distanceMax + costFunction((costMax - cost) / costMax)
            # print("distanceElement:",(distanceMax - distanceElement) / distanceMax*100,"%, cost of travel: ", (costMax - cost) /costMax*100,"% adaptation",adaptationVal)
            return adaptationVal if adaptationVal > 0 else 0
        else:
            return 0
