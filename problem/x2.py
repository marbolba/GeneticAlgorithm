import numpy as np

from problem.abstractProblem import Problem, GenotypeInfo


class X2GenotypeInfo(GenotypeInfo):
    def __init__(self):
        self.parameters = 2
        self.parametersWordLength = [6, 6]
        self.parametersDomain = [(0, 20), (0, 20)]


class X2(Problem):
    def goalFunction(self, values):
        return np.power(values, 2)

    def adaptationFunction(self, values):
        return np.power(values[0], 2)

    def genotypeInfo(self):
        return X2GenotypeInfo()
