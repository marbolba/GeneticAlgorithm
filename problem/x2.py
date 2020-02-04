import numpy as np

from geneticAlgorithm.genotype.binaryGenotype import BinaryGenotype
from geneticAlgorithm.genotype.decimalGenotype import DecimalGenotype
from problem.abstractProblem import Problem, GenotypeInfo


class X2GenotypeInfo(GenotypeInfo):
    def __init__(self):
        self.type = DecimalGenotype
        self.parameters = 2
        self.parametersWordLength = [2, 2]
        self.parametersDomain = [(0, 15), (0, 10)]


class X2(Problem):
    def goalFunction(self, values):
        return np.power(values, 2)

    def adaptationFunction(self, values):
        return values[0]

    def genotypeInfo(self):
        return X2GenotypeInfo()
