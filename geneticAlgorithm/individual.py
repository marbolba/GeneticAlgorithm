import copy

import numpy as np

from geneticAlgorithm.binaryGenotype import BinaryGenotype
from problem.abstractProblem import Problem
from settings.abstractSettings import Setting


class Individual:
    def __init__(self):
        self.genotype = None
        self._problem = None
        self._setting = None

        self._value = None
        self._fenotype = None
        self._adaptation = None

    def setProblem(self, problem: Problem):
        self._problem = problem
        self._initGenotype()

    def setSetting(self, setting: Setting):
        self._setting = setting

    def setGenotype(self, genotype:[]):
        self.genotype.genotype = copy.deepcopy(genotype)

        self._value = self.genotype.calculateValue()
        self._calculateFenotype()
        self._calculateAdaptation()

    def _initGenotype(self):
        g = BinaryGenotype()
        g.setLength(self._setting.genotypeLenght())
        g.randomize()
        self.genotype = g
        print(self.genotype)

        self._value = self.genotype.calculateValue()
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
