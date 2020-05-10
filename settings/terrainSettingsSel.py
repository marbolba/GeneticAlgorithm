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
        
        # terrain basic
        maxStepsNr = 8
        self.parameters = 2*maxStepsNr+1    # do not change
        self.parametersWordLength = list(1 for i in range(0, self.parameters))
        self.parametersDomain = [(0,maxStepsNr)] +list((0, TerrainHandler.getSize()[i % 2] - 1) for i in range(0, int(self.parameters-1)))

class TerrainSettingSel(Setting):
    def __init__(self):
        self.terrainGenotypeInfo: TerrainGenotypeInfo = TerrainGenotypeInfo()

    def generationsNumber(self):
        return 30

    def populationSize(self):
        return 200

    def mutationProbability(self):
        return 0.1

    def crossoverProbability(self):
        return 0.5

    def genotypeInfo(self):
        return self.terrainGenotypeInfo
