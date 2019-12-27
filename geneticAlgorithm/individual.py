import copy

import numpy as np

from geneticAlgorithm.binaryGenotype import BinaryGenotype
from problem.abstractProblem import Problem


class Individual:
    def __init__(self):
        self._genotype = None
        self._problem = None

        self._value = None
        self._fenotype = None
        self._adaptation = None

    def setProblem(self, problem: Problem):
        self._problem = problem

        self._initGenotype()

    def setGenotype(self, genotype:[]):
        self._genotype.genotype = copy.deepcopy(genotype)

        self._value = self._genotype.calculateValue()
        self._calculateFenotype()
        self._calculateAdaptation()

    def _initGenotype(self):
        g = BinaryGenotype()
        g.setLength(self._problem.genotypeLenght())
        g.randomize()
        self._genotype = g

        self._value = self._genotype.calculateValue()
        self._calculateFenotype()
        self._calculateAdaptation()

    # calculates fenotype value
    def _calculateFenotype(self):
        self._fenotype = self._problem.goalFunction(self._value)

    # sets adaptation function value for individual
    def _calculateAdaptation(self):
        self._adaptation = self._problem.adaptationFunction(self._fenotype)

    def getValue(self):
        return self._value

    def getFenotype(self):
        return self._fenotype

    def getAdaptation(self):
        return self._adaptation
