import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt


class TerrainHandler:
    fileName = "ctype"
    terrain = []
    domain = ()

    @staticmethod
    def readFromFile(fileName):
        return np.load(fileName)

    @staticmethod
    def slope(point1,point2):
        coefficients = np.polyfit((point1[0],point2[0]),(point1[1],point2[1]), 1)
        return coefficients[0], coefficients[1]

    @staticmethod
    def distance(point1,point2):
        return distance.euclidean(point1,point2)

    @staticmethod
    def setName(fileName):
        TerrainHandler.fileName = fileName
        TerrainHandler.terrain = TerrainHandler.readFromFile("assets/terrains/{}/terrain.npy".format(fileName))
        TerrainHandler.domain = TerrainHandler.readFromFile("assets/terrains/{}/size.npy".format(fileName))

    @staticmethod
    def getSize():
        return TerrainHandler.domain[1], TerrainHandler.domain[0]

    @staticmethod
    def getTerrainToughness(x,y):
        return TerrainHandler.terrain[y][x]

    @staticmethod
    def drawTerrain():
        plt.matshow(TerrainHandler.terrain)
        plt.colorbar()
        # self.checkIfFolderExists()
        # plt.savefig("{}{}-2d.png".format(self.folderPath, self.label))
        plt.show()

    @staticmethod
    def drawTerrainWithPoints(points:[int]):
        #terrain
        plt.matshow(TerrainHandler.terrain)
        plt.colorbar()
        # self.checkIfFolderExists()
        # plt.savefig("{}{}-2d.png".format(self.folderPath, self.label))

        #points
        items = np.transpose([list(item) for item in points])
        plt.plot(items[0],items[1], 'xr-')
        plt.show()
