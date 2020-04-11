import copy

from geneticAlgorithm.genotype.abstractGenotype import Genotype
from problem.abstractProblem import Problem
from settings.abstractSettings import Setting


class Individual:
    def __init__(self):
        self.genotype: Genotype = None
        self._problem: Problem = None
        self._setting: Setting = None

        self._values = None
        self._fenotype = None
        self._adaptation = None

    def setProblem(self, problem: Problem):
        self._problem = problem
        self._initGenotype()

    def setSetting(self, setting: Setting):
        self._setting = setting

    def setGenotype(self, genotype: []):
        self.genotype.genotype = genotype
        self._values = self.genotype.calculateValue()
        self._calculateFenotype()
        self._calculateAdaptation()

    def setGene(self,geneIdx,gene):
        if(geneIdx<len(self.genotype.genotype)):
            self.genotype.genotype[geneIdx] = gene
        else:
            print("ERR: setting gene failed")
    
    def refresh(self):
        self._values = self.genotype.calculateValue()
        self._calculateFenotype()
        self._calculateAdaptation()

    def _initGenotype(self):
        g = self._setting.genotypeInfo().type()
        g.setGenotypeInfo(self._setting.genotypeInfo())
        g.randomize()
        self.genotype = g

        self._values = self.genotype.calculateValue()
        self._calculateFenotype()
        self._calculateAdaptation()

    # calculates fenotype value
    def _calculateFenotype(self):
        self._fenotype = self._problem.goalFunction(self._values)

    # sets adaptation function value for individual
    def _calculateAdaptation(self):
        self._adaptation = self._problem.adaptationFunction(self._fenotype)

    def getValue(self):
        return self._values

    def getFenotype(self):
        return self._fenotype

    def getAdaptation(self):
        return self._adaptation
