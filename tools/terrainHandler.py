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
    def checkIfFolderExists(folderPath):
        if not (os.path.exists(folderPath)):
            # create the directory you want to save to
            os.mkdir(folderPath)

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
        size = TerrainHandler.getSize()
        fi = math.atan2(point2[1]-point1[1],point2[0]-point1[0])
        maxR = TerrainHandler.distance(point1,point2)
        sinFi = np.sin(fi)
        cosFi = np.cos(fi)

        stepLength = 1
        cost = 0
        previousHeight = TerrainHandler.getPointHeight(round(point1[0]),round(point1[1]))
        for r in range(1,int(round(maxR)+1),stepLength):
            x,y = int(round(point1[0] + r*cosFi)),int(round(point1[1] + r*sinFi))
            if(x<size[0] and x>=0 and y<size[1] and y>=0):
                # print(":",x,y,TerrainHandler.getPointHeight(x,y),previousHeight,"=",stepLength + abs(TerrainHandler.getPointHeight(x,y)-previousHeight)*5)
                cost = cost + stepLength + abs(TerrainHandler.getPointHeight(x,y)-previousHeight)*5 # TerrainHandler.getPointAccessibility(x,y)   #temporary removed
                previousHeight = TerrainHandler.getPointHeight(x,y)
            else:
                cost = cost + 100 # punish 
        # print("cost",point1,point2," = ",cost)
        return cost
    
    @staticmethod
    def getNextStepPosition(position,fi,r):
        sinFi = np.sin(fi)
        cosFi = np.cos(fi)
        x,y = int(round(position[0] + r*cosFi)),int(round(position[1] + r*sinFi))
        return (x,y)

    @staticmethod
    def setName(folderName):
        TerrainHandler.folderPath = "assets/terrains/{}/".format(folderName)
        TerrainHandler.fetchAssets(folderName)

    @staticmethod
    def fetchAssets(folderName):
        TerrainHandler.terrain = TerrainHandler.readFromFile("assets/terrains/{}/terrain.npy".format(folderName))
        TerrainHandler.accessibility = TerrainHandler.readFromFile("assets/terrains/{}/accessibility.npy".format(folderName))
        TerrainHandler.domain = TerrainHandler.readFromFile("assets/terrains/{}/terrain-size.npy".format(folderName))

    @staticmethod
    def drawTerrainWithPoints(points: [int],generationNr:int):
        historyFolder = f"{TerrainHandler.folderPath}history/"
        # terrain
        plt.matshow(TerrainHandler.terrain)
        plt.colorbar()

        # points
        items = np.transpose([list(item) for item in points])
        plt.plot(items[0], items[1], "xr-")
        TerrainHandler.checkIfFolderExists(historyFolder)
        plt.savefig(f"{historyFolder}generation-{generationNr}.png")

        plt.show(block=False)
        plt.pause(0.3)
        plt.close()

    @staticmethod
    def drawFinalRaport(points: [int]):
        # terrain
        plt.matshow(TerrainHandler.terrain)
        plt.colorbar()

        # points
        items = np.transpose([list(item) for item in points])
        plt.plot(items[0], items[1], "xr-")
        TerrainHandler.checkIfFolderExists(TerrainHandler.folderPath)
        plt.savefig("{}result-2d.png".format(TerrainHandler.folderPath))

        plt.show()
