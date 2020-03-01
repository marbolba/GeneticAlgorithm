import numpy as np

from geneticAlgorithm.genotype.binaryGenotype import BinaryGenotype
from geneticAlgorithm.genotype.decimalGenotype import DecimalGenotype
from geneticAlgorithm.operations.binaryOperation import BinaryOperation
from geneticAlgorithm.operations.decinalOperation import DecimalOperation
from settings.abstractSettings import Setting, GenotypeInfo
from tools.terrainHandler import TerrainHandler


class TerrainGenotypeInfo(GenotypeInfo):
    TerrainHandler.setName("ctype2")
    size = TerrainHandler.getSize()
    print("terrainSize: {}".format(size))

    def __init__(self):

        self.type = DecimalGenotype

        self.reproduction = DecimalOperation.rouletteReproduction
        self.succession = DecimalOperation.eliteSuccession
        self.crossover = DecimalOperation.singlePointCrossover
        self.mutation = DecimalOperation.mutation

        self.parameters = 8
        self.parametersWordLength = [1, 1, 1, 1, 1, 1, 1, 1]
        self.parametersDomain = [(0,TerrainGenotypeInfo.size[0]-1), (0,TerrainGenotypeInfo.size[1]-1),
                                 (0,TerrainGenotypeInfo.size[0]-1), (0,TerrainGenotypeInfo.size[1]-1),
                                 (0,TerrainGenotypeInfo.size[0]-1), (0,TerrainGenotypeInfo.size[1]-1),
                                 (0,TerrainGenotypeInfo.size[0]-1), (0,TerrainGenotypeInfo.size[1]-1)
                                 ]


class TerrainSetting(Setting):
    def generationsNumber(self):
        return 50

    def populationSize(self):
        return 100

    def mutationProbability(self):
        return 1

    def crossoverProbability(self):
        return 0.5

    def genotypeInfo(self):
        return TerrainGenotypeInfo()
