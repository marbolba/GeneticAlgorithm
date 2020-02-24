import numpy as np

from problem.abstractProblem import Problem


class TerrainProblem(Problem):
    def goalFunction(self, values):
        return np.power(values, 2)

    def adaptationFunction(self, values):
        return np.power(values[0] + values[1], 2)
