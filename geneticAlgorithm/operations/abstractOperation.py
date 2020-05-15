from geneticAlgorithm.genotype.abstractGenotype import Genotype
from geneticAlgorithm.individual import Individual
from geneticAlgorithm.population import Population
from settings.abstractSettings import Setting
import random


class Operation:
    @staticmethod
    def rouletteReproduction(population: Population):
        raise NotImplementedError("The method not implemented")

    @staticmethod
    def singlePointCrossover(population: [Individual], setting: Setting):
        raise NotImplementedError("The method not implemented")

    @staticmethod
    def mutation(population: [Individual], setting: Setting):
        raise NotImplementedError("The method not implemented")

    # SUCCESSION
    @staticmethod
    def trivialSuccession(population: Population, newPopulation: [Individual]):
        population.setPopulation(newPopulation)

    @staticmethod
    def eliteSuccession(population: Population, newPopulation: [Individual]):
        # settings parameters:
        g = 0.3  # percent of old population elite
        sortedOldPopulation = sorted(
            population.population, key=lambda x: x._adaptation, reverse=True
        )
        sortedNewPopulation = sorted(
            newPopulation, key=lambda x: x._adaptation, reverse=True
        )
        finalPopulationSize = len(sortedOldPopulation)

        for i in range(0, int(g * finalPopulationSize)):
            # print(sortedNewPopulation[finalPopulationSize-1-i]._adaptation,"for", sortedOldPopulation[i]._adaptation)
            sortedNewPopulation[finalPopulationSize - 1 - i] = sortedOldPopulation[
                i
            ]  # exchange worst new for best old

        random.shuffle(sortedNewPopulation)
        population.setPopulation(sortedNewPopulation)
