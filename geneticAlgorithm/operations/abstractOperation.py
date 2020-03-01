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
        population.setPopulation(newPopulation)

    @staticmethod
    def eliteSuccession(population: Population, newPopulation: [Individual]):
        sortedIndividuals = sorted(population.population, key=lambda x: x._adaptation, reverse=True)
        newPopulation[0] = sortedIndividuals[0]
        newPopulation[3] = sortedIndividuals[1]
        newPopulation[5] = sortedIndividuals[2]
        newPopulation[7] = sortedIndividuals[3]
        newPopulation[9] = sortedIndividuals[4]
        newPopulation[11] = sortedIndividuals[5]
        newPopulation[13] = sortedIndividuals[6]
        newPopulation[15] = sortedIndividuals[7]
        newPopulation[17] = sortedIndividuals[8]
        newPopulation[19] = sortedIndividuals[9]
        newPopulation[21] = sortedIndividuals[10]
        population.setPopulation(newPopulation)
