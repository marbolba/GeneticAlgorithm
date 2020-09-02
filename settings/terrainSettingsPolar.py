import numpy as np

from geneticAlgorithm.genotype.binaryGenotype import BinaryGenotype
from geneticAlgorithm.genotype.decimalGenotype import DecimalGenotype
from geneticAlgorithm.operations.binaryOperation import BinaryOperation
from geneticAlgorithm.operations.decinalOperation import DecimalOperation
from settings.abstractSettings import Setting, GenotypeInfo
from tools.terrainHandler import TerrainHandler


class TerrainGenotypeInfo(GenotypeInfo):
    def __init__(self):

        self.type = DecimalGenotype

        self.reproduction = DecimalOperation.rouletteReproduction
        self.succession = DecimalOperation.eliteSuccession
        self.crossover = DecimalOperation.singlePointCrossover
        self.mutation = DecimalOperation.mutation

        # terrain step
        self.stepsNr = 4

        self.parameters = 2 * self.stepsNr
        self.parametersWordLength = list(1 for i in range(0, self.parameters))
        self.parametersDomain = self.domainsForPolar()

    def domainsForPolar(self):
        # settings
        maxStepLength = 100

        domain = []
        for _ in range(0, self.stepsNr):
            domain.append((0, 2 * np.pi))
            domain.append((0, maxStepLength))
        return domain


class TerrainSettingPolar(Setting):
    def __init__(self):
        self.terrainGenotypeInfo: TerrainGenotypeInfo = TerrainGenotypeInfo()

    def generationsNumber(self):
        return 50

    def populationSize(self):
        return 100

    def mutationProbability(self):
        return 0.1

    def crossoverProbability(self):
        return 0.5

    def genotypeInfo(self):
        return self.terrainGenotypeInfo
