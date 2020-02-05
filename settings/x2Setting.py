from geneticAlgorithm.genotype.decimalGenotype import DecimalGenotype
from settings.abstractSettings import Setting, GenotypeInfo


class X2GenotypeInfo(GenotypeInfo):
    def __init__(self):
        self.type = DecimalGenotype
        self.parameters = 2
        self.parametersWordLength = [1, 1]
        self.parametersDomain = [(0, 15), (0, 10)]


class X2Setting(Setting):
    def populationSize(self):
        return 30

    def mutationProbability(self):
        return 0.1

    def crossoverProbability(self):
        return 0.5

    def genotypeInfo(self):
        return X2GenotypeInfo()
