import os
import math
import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt


class TerrainHandler:
    folderPath = ""
    terrain = []
    accessibility = []
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
    def getPointHeight(x, y):
        return TerrainHandler.terrain[y][x]
    
    @staticmethod
    def getPointAccessibility(x, y):
        return TerrainHandler.accessibility[y][x]

    @staticmethod
    def travelCost(point1, point2):
        cost = 0
        fi = math.atan2(point2[1]-point1[1],point2[0]-point1[0])
        maxR = TerrainHandler.distance(point1,point2)
        for r in range(1,int(round(maxR))):
            x,y = int(round(point1[0] + r*np.cos(fi))),int(round(point1[1] + r*np.sin(fi)))
            cost = cost + TerrainHandler.getPointHeight(x,y) # TerrainHandler.getPointAccessibility(x,y)   #temporary removed
        return cost

    @staticmethod
    def setName(folderName):
        TerrainHandler.folderPath = "assets/terrains/{}/".format(folderName)
        TerrainHandler.terrain = TerrainHandler.readFromFile("assets/terrains/{}/terrain.npy".format(folderName))
        TerrainHandler.accessibility = TerrainHandler.readFromFile("assets/terrains/{}/accessibility.npy".format(folderName))
        TerrainHandler.domain = TerrainHandler.readFromFile("assets/terrains/{}/terrain-size.npy".format(folderName))

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
