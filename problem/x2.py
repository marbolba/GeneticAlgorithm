import numpy as np

from problem.abstractProblem import Problem, GenotypeInfo


class X2GenotypeInfo(GenotypeInfo):
    def __init__(self):
        self.parameters = 1
        self.parametersWordLength = [6]
        self.parametersDomain = [(0, 20)]  # eg.[(0, 20), (0, 40)]


class X2(Problem):
    def goalFunction(self, value):
        return np.power(value, 2)

    def adaptationFunction(self, value):
        return np.power(value, 2)

    def genotypeInfo(self):
        return X2GenotypeInfo()
