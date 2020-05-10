import numpy as np

from problem.abstractProblem import Problem
from tools.terrainHandler import TerrainHandler
import matplotlib.pyplot as plt
from scipy.spatial import distance


class TerrainProblemStep(Problem):
    def goalFunction(self, values):
        points = []
        currentPosition = (0,0)
        
        for i in range(1,round(values[0])*2+1,2):
            fi = values[i]
            r = values[i+1]
            currentPosition = TerrainHandler.getNextStepPosition(currentPosition,fi,r)
            points.append(currentPosition)
        return points

    def adaptationFunction(self, values: []):
        # settings
        startPoint = [0, 0]
        endPoint = [200,20]

        distanceMax = TerrainHandler.distance(startPoint, endPoint)
        costMax = 3000
        # print(values)

        if(len(values)>0):
            # składowa dystansu - ostatni element do endpoint
            distanceElement = TerrainHandler.distance((values[len(values) - 1][0], values[len(values) - 1][1]), endPoint)

            # skladowa kosztu podróży
            cost = 0
            values.insert(0, (0, 0))
            for i in range(len(values) - 1):
                cost = cost + TerrainHandler.travelCost(values[i], values[i + 1])
            # print(values," cost ",cost)

            adaptationVal = 8000 * (distanceMax - distanceElement) / distanceMax + 3000* (costMax - cost) /costMax
            # print("distanceElement:",distanceElement,", cost of travel: ", cost,"adaptation",adaptationVal)
            return adaptationVal if adaptationVal > 0 else 0
        else:
            return 0 
