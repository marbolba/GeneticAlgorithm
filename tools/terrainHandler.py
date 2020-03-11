import os
import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt


class TerrainHandler:
    folderPath = ""
    terrain = []
    domain = ()

    @staticmethod
    def readFromFile(fileName):
        return np.load(fileName)

    @staticmethod
    def checkIfFolderExists():
        if not (os.path.exists(TerrainHandler.folderPath)):
            # create the directory you want to save to
            os.mkdir(TerrainHandler.folderPath)

    @staticmethod
    def slope(point1, point2):
        a = (point2[1] - point1[1]) / (point2[0] - point1[0])
        b = point1[1] - a * point1[0]  # b = y - ax
        return a, b

    @staticmethod
    def distance(point1, point2):
        return distance.euclidean(point1, point2)

    @staticmethod
    def getSize():
        return TerrainHandler.domain[1], TerrainHandler.domain[0]

    @staticmethod
    def getTerrainToughness(x, y):
        return TerrainHandler.terrain[y][x]

    @staticmethod
    def travelCost(point1, point2):
        cost = 0
        if point1[0] == point2[0]:
            # this is vertical distance
            for y in range(min(point1[1], point2[1]), max(point1[1], point2[1])):
                cost = cost + TerrainHandler.getTerrainToughness(point1[0], y)
            return cost
        else:
            # this is linear distance
            a, b = TerrainHandler.slope(point1, point2)
            for x in range(min(point1[0], point2[0]), max(point1[0], point2[0])):
                y = int(round(a * x + b))
                cost = cost + TerrainHandler.getTerrainToughness(x, y)
            return cost

    @staticmethod
    def setName(folderName):
        TerrainHandler.folderPath = "assets/terrains/{}/".format(folderName)
        TerrainHandler.terrain = TerrainHandler.readFromFile(
            "assets/terrains/{}/terrain.npy".format(folderName)
        )
        TerrainHandler.domain = TerrainHandler.readFromFile(
            "assets/terrains/{}/size.npy".format(folderName)
        )

    @staticmethod
    def drawTerrainWithPoints(points: [int]):
        # terrain
        plt.matshow(TerrainHandler.terrain)
        plt.colorbar()

        # points
        items = np.transpose([list(item) for item in points])
        plt.plot(items[0], items[1], "xr-")
        TerrainHandler.checkIfFolderExists()
        plt.savefig("{}result-2d.png".format(TerrainHandler.folderPath))

        plt.show()
