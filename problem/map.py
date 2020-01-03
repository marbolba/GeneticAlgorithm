import numpy as np

from problem.abstractProblem import Problem, GenotypeInfo


class MapGenotypeInfo(GenotypeInfo):
    def __init__(self):
        self.parameters =
        self.parametersWordLength = [6]
        self.parametersDomain = [(0, 5), (0,100), (0,100)]  # TODO ended here... eg.[(0, 20), (0, 40)]
                                                            # TODO potrzebuje kodowania calkowitoliczbowego :O


class Map(Problem):
    def goalFunction(self, values):
        return np.power(values, 2)

    def adaptationFunction(self, values):
        return np.power(values[0], 2)

    def genotypeInfo(self):
        return MapGenotypeInfo()
