from geneticAlgorithm.genotype.abstractGenotype import Genotype
from geneticAlgorithm.individual import Individual
from geneticAlgorithm.population import Population
from settings.abstractSettings import Setting
import random
import numpy as np
import copy


class Operation:
    @staticmethod
    def rouletteReproduction(population: Population, k=None):
        if k is None:
            k = len(population.population)
        # creating select chance array
        adaptationSum = 0
        selectChance = []
        for individual in population.population:
            adaptationSum += individual.getAdaptation()
        for individual in population.population:
            selectChance.append(individual.getAdaptation() / adaptationSum)
        selectChance = np.cumsum(selectChance)

        # select new population
        newPopulation = []
        selected = np.random.rand(k)
        for sel in selected:
            for propIdx in range(len(selectChance)):
                if sel <= selectChance[propIdx]:
                    newPopulation.append(copy.deepcopy(population.population[propIdx]))
                    break

        # override with new population
        return newPopulation

    @staticmethod
    def tournamentReproduction(population: Population, tournamentSize: int = 3):
        k = len(population.population)

        # select new population
        newPopulation = []
        for _ in range(k):
            aspirants = Operation.rouletteReproduction(population, k=tournamentSize)
            sortedIndividuals = sorted(
                aspirants, key=lambda x: x.getAdaptation(), reverse=True
            )
            newPopulation.append(copy.deepcopy(sortedIndividuals[0]))

        # override with new population
        return newPopulation

    @staticmethod
    def rankReproduction(population: Population):
        sortedPopulation = sorted(
            population.population, key=lambda x: x.getAdaptation(), reverse=True
        )
        N = len(population.population)

        sum = np.sum(range(0, N))
        k = N / (N * N - sum)
        a = 1 / N - k * (1 - sum / (N * N))

        selectChance = []
        for r in range(N):
            selectChance.append(a + k * (1 - (r / N)))
        assert np.sum(selectChance) == 1.0
        selectChance = np.cumsum(selectChance)

        # select new population
        newPopulation = []
        selected = np.random.rand(N)
        for sel in selected:
            for propIdx in range(len(selectChance)):
                if sel <= selectChance[propIdx]:
                    newPopulation.append(copy.deepcopy(sortedPopulation[propIdx]))
                    break

        # override with new population
        return newPopulation

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

    # SUCCESSION
    @staticmethod
    def freshBloodSuccession(population: Population, newPopulation: [Individual]):
        # settings parameters:
        g = 0.05  # percent of fresh blood individuals
        finalPopulationSize = len(population.population)
        sortedNewPopulation = sorted(
            newPopulation, key=lambda x: x.getAdaptation(), reverse=True
        )

        for i in range(0, int(g * finalPopulationSize)):
            newIndividual = Individual()
            newIndividual.setSetting(population.population[0].setting)
            newIndividual.setProblem(population.population[0].problem)
            sortedNewPopulation[finalPopulationSize - 1 - i] = newIndividual

        random.shuffle(sortedNewPopulation)
        population.setPopulation(sortedNewPopulation)

    @staticmethod
    def eliteSuccession(population: Population, newPopulation: [Individual]):
        # settings parameters:
        g = 0.3  # percent of old population elite
        sortedOldPopulation = sorted(
            population.population, key=lambda x: x.getAdaptation(), reverse=True
        )
        sortedNewPopulation = sorted(
            newPopulation, key=lambda x: x.getAdaptation(), reverse=True
        )
        finalPopulationSize = len(sortedOldPopulation)

        for i in range(0, int(g * finalPopulationSize)):
            sortedNewPopulation[finalPopulationSize - 1 - i] = sortedOldPopulation[
                i
            ]  # exchange worst new for best old

        random.shuffle(sortedNewPopulation)
        population.setPopulation(sortedNewPopulation)
