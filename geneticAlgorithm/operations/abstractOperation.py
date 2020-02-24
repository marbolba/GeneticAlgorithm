from geneticAlgorithm.genotype.abstractGenotype import Genotype
from geneticAlgorithm.individual import Individual
from settings.abstractSettings import Setting


class Operation:
    @staticmethod
    def rouletteReproduction(population: [Individual]):
        raise NotImplementedError("The method not implemented")

    @staticmethod
    def singlePointCrossover(population:[Individual], setting:Setting):
        raise NotImplementedError("The method not implemented")

    @staticmethod
    def mutation(population:[Individual], setting:Setting):
        raise NotImplementedError("The method not implemented")
