import numpy as np


class TerrainHandler:
    @staticmethod
    def readFromFile(fileName) -> [[]]:
        return np.load(fileName)
