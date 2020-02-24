from geneticAlgorithm.genotype.binaryGenotype import BinaryGenotype
from geneticAlgorithm.genotype.decimalGenotype import DecimalGenotype
from geneticAlgorithm.operations.binaryOperation import BinaryOperation
from geneticAlgorithm.operations.decinalOperation import DecimalOperation
from settings.abstractSettings import Setting, GenotypeInfo


class X2GenotypeInfo(GenotypeInfo):
    def __init__(self):
        self.type = DecimalGenotype

        self.reproduction = DecimalOperation.rouletteReproduction
        self.crossover = DecimalOperation.singlePointCrossover
        self.mutation = DecimalOperation.mutation

        self.parameters = 2
        self.parametersWordLength = [1, 1]
        self.parametersDomain = [(0, 9), (0, 9)]


class X2Setting(Setting):
    def generationsNumber(self):
        return 30

    def populationSize(self):
        return 30

    def mutationProbability(self):
        return 0.1

    def crossoverProbability(self):
        return 0.5

    def genotypeInfo(self):
        return X2GenotypeInfo()
