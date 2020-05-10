import numpy as np

from geneticAlgorithm.genotype.binaryGenotype import BinaryGenotype
from geneticAlgorithm.genotype.decimalGenotype import DecimalGenotype
from geneticAlgorithm.operations.binaryOperation import BinaryOperation
from geneticAlgorithm.operations.decinalOperation import DecimalOperation
from settings.abstractSettings import Setting, GenotypeInfo
from tools.terrainHandler import TerrainHandler


class TerrainGenotypeInfo(GenotypeInfo):
    TerrainHandler.setName("12-kwi-2020_170728")
    size = TerrainHandler.getSize()

    def __init__(self):

        self.type = DecimalGenotype

        self.reproduction = DecimalOperation.rouletteReproduction
        self.succession = DecimalOperation.eliteSuccession
        self.crossover = DecimalOperation.singlePointCrossover
        self.mutation = DecimalOperation.mutation

        # terrain step
        self.parameters = 31    # 2*maxStepsNr + 1
        self.parametersWordLength = list(1 for i in range(0, self.parameters))
        self.parametersDomain = self.domainsForStep()
    
    def domainsForStep(self):
        #settings
        maxStepsNr = 15
        maxStepLength = 50
        
        domain = []
        domain.append((0,maxStepsNr))
        for _ in range(0, maxStepsNr):
            domain.append((0, 2*np.pi))
            domain.append((0,maxStepLength))
        return domain


class TerrainSettingStep(Setting):
    def __init__(self):
        self.terrainGenotypeInfo: TerrainGenotypeInfo = TerrainGenotypeInfo()

    def generationsNumber(self):
        return 70

    def populationSize(self):
        return 200

    def mutationProbability(self):
        return 0.1

    def crossoverProbability(self):
        return 0.5

    def genotypeInfo(self):
        return self.terrainGenotypeInfo
