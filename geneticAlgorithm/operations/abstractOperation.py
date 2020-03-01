from geneticAlgorithm.genotype.abstractGenotype import Genotype
from geneticAlgorithm.individual import Individual
from geneticAlgorithm.population import Population
from settings.abstractSettings import Setting


class Operation:
    @staticmethod
    def rouletteReproduction(population: Population):
        raise NotImplementedError("The method not implemented")

    @staticmethod
    def singlePointCrossover(population:[Individual], setting:Setting):
        raise NotImplementedError("The method not implemented")

    @staticmethod
    def mutation(population:[Individual], setting:Setting):
        raise NotImplementedError("The method not implemented")

    # SUCCESSION
    @staticmethod
    def trivialSuccession(population: Population, newPopulation: [Individual]):
        print("setting new:",newPopulation)
        population.setPopulation(newPopulation)

    @staticmethod
    def eliteSuccession(population: Population, newPopulation: [Individual]):
        sortedIndividuals = sorted(population.population, key=lambda x: x._adaptation, reverse=True)
        # newPopulation[0] = sortedIndividuals[0]
        # population = newPopulation
