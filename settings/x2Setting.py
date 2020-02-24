from geneticAlgorithm.genotype.binaryGenotype import BinaryGenotype
from geneticAlgorithm.genotype.decimalGenotype import DecimalGenotype
from geneticAlgorithm.operations.binaryOperation import BinaryOperation
from settings.abstractSettings import Setting, GenotypeInfo


class X2GenotypeInfo(GenotypeInfo):
    def __init__(self):
        self.type = BinaryGenotype

        self.reproduction = BinaryOperation.rouletteReproduction
        self.crossover = BinaryOperation.singlePointCrossover
        self.mutation = BinaryOperation.mutation

        self.parameters = 2
        self.parametersWordLength = [4, 4]
        self.parametersDomain = [(0, 15), (0, 15)]


class X2Setting(Setting):
    def generationsNumber(self):
        return 30

    def populationSize(self):
        return 30

    def mutationProbability(self):
        return 0.001

    def crossoverProbability(self):
        return 0.5

    def genotypeInfo(self):
        return X2GenotypeInfo()
