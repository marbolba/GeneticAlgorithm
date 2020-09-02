import numpy as np

from problem.abstractProblem import Problem
from tools.terrainHandler import TerrainHandler
import matplotlib.pyplot as plt
from scipy.spatial import distance


class TerrainProblemPolarSel(Problem):
    def fenotypeFunction(self, values):
        points = []
        currentPosition = TerrainHandler.getWaypoints()[0]

        for i in range(1, round(values[0]) * 2 + 1, 2):
            fi = values[i]
            r = values[i + 1]
            currentPosition = TerrainHandler.getNextStepPosition(currentPosition, fi, r)
            points.append(currentPosition)
        return points

    def adaptationFunction(self, values: []):
    # settings
        # costFunction: always between <0,1>
        # costFunction = lambda x: x # linear
        # costFunction = lambda x: (1/16)*pow(16,x) # exponential (0.75,0.5)
        costFunction = lambda x: (1/64)*pow(64,x) # exponential (0.83,0.5)
        # factor / ratio:
        sum = 1000
        W = 5/3
        b = sum / (W + 1)
        a = sum - b

    # the rest

        startPoint = TerrainHandler.getWaypoints()[0]
        endPoint = TerrainHandler.getWaypoints()[1]

        distanceMax = TerrainHandler.distance((0, 0), TerrainHandler.getSize())
        costMax = 10000

        # check if there are any points on the road
        valuesLoc = values.copy()
        if len(valuesLoc) < 1:
            return 0

        # calculate distance 
        distance = TerrainHandler.distance(
            valuesLoc[len(valuesLoc) - 1],
            endPoint,
        )

        # calculate cost
        cost = 0
        valuesLoc.insert(0, startPoint)
        for i in range(0, len(valuesLoc) - 1):
            cost = cost + TerrainHandler.travelCost(valuesLoc[i], valuesLoc[i + 1])

        distance_element = (distanceMax - distance) / distanceMax
        cost_element = (costMax - cost) / costMax

        adaptationVal = a * distance_element + b * costFunction(cost_element)
        return adaptationVal if adaptationVal > 0 else 0