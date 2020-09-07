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
        self.maxStepsNr = 10

        self.parameters = 3 * self.maxStepsNr
        self.parametersWordLength = list(1 for i in range(0, self.parameters))
        self.parametersDomain = self.domainsForPolarSel()

    def domainsForPolarSel(self):
        # settings
        maxStepLength = 100

        domain = []
        for _ in range(0, self.maxStepsNr):
            domain.append((0, 2 * np.pi))
            domain.append((0, maxStepLength))
            domain.append((0, 100))
        return domain


class TerrainSettingPolarFlipbit(Setting):
    def __init__(self):
        self.terrainGenotypeInfo: TerrainGenotypeInfo = TerrainGenotypeInfo()

    def generationsNumber(self):
        return 30

    def populationSize(self):
        return 100

    def mutationProbability(self):
        return 0.01

    def crossoverProbability(self):
        return 1

    def genotypeInfo(self):
        return self.terrainGenotypeInfo
