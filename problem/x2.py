import numpy as np

from problem.abstractProblem import Problem


class GenotypeInfo:
    parameters = 2
    parameteresWordLength = [6, 6]
    parameteresDomain = [(0, 20), (0, 40)]

    def validateParameters(self):
        print(self.parameteres() == len(self.parameteresWordLength) == len(self.parameteresDomain))
        return self.parameteres() == len(self.parameteresWordLength) == len(self.parameteresDomain)


class X2(Problem):
    def goalFunction(self, value):
        return np.power(value, 2)

    def adaptationFunction(self, value):
        return np.power(value, 2)

    def genotypeInfo(self):
        return GenotypeInfo()
