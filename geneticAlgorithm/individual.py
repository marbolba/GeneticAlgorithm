import copy

from geneticAlgorithm.genotype.abstractGenotype import Genotype
from problem.abstractProblem import Problem
from settings.abstractSettings import Setting


class Individual:
    def __init__(self):
        self.genotype: Genotype = None
        self.problem: Problem = None
        self.setting: Setting = None

        self._values = None
        self._fenotype = None
        self._adaptation = None

    def setProblem(self, problem: Problem):
        self.problem = problem
        self._initGenotype()

    def setSetting(self, setting: Setting):
        self.setting = setting

    def setGenotype(self, genotype: []):
        self.genotype.genotype = genotype
        self._values = self.genotype.calculateValue()
        self._calculateFenotype()
        self._calculateAdaptation()

    def setGene(self, geneIdx, gene):
        if geneIdx < len(self.genotype.genotype):
            self.genotype.genotype[geneIdx] = gene
        else:
            print("ERR: setting gene failed")

    def refresh(self):
        self._values = self.genotype.calculateValue()
        self._calculateFenotype()
        self._calculateAdaptation()

    def _initGenotype(self):
        g = self.setting.genotypeInfo().type()
        g.setGenotypeInfo(self.setting.genotypeInfo())
        g.randomize()
        self.genotype = g

        self._values = self.genotype.calculateValue()
        self._calculateFenotype()
        self._calculateAdaptation()

    # calculates fenotype value
    def _calculateFenotype(self):
        self._fenotype = self.problem.fenotypeFunction(self._values)

    # sets adaptation function value for individual
    def _calculateAdaptation(self):
        self._adaptation = self.problem.adaptationFunction(self._fenotype)

    def getValue(self):
        return self._values

    def getFenotype(self):
        return self._fenotype

    def getAdaptation(self):
        return self._adaptation
