import copy
from random import normalvariate

import numpy as np
import time

from geneticAlgorithm.genotype.abstractGenotype import Genotype
from geneticAlgorithm.individual import Individual
from geneticAlgorithm.operations.abstractOperation import Operation
from geneticAlgorithm.population import Population
from settings.abstractSettings import Setting
from tools.timeFoo import timeFoo


class DecimalOperation(Operation):
    # REPRODUCTION
    @staticmethod
    def rouletteReproduction(population: Population):
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
        selected = np.random.rand(len(population.population))
        for sel in selected:
            for propIdx in range(len(selectChance)):
                if sel <= selectChance[propIdx]:
                    newPopulation.append(copy.deepcopy(population.population[propIdx]))
                    break

        return newPopulation

    # CROSSOVER
    @staticmethod
    def singlePointCrossover(population: [Individual], setting: Setting):
        sizeOfPopulation = len(population)
        genotypeLength = len(population[0].genotype.genotype)
        for i in range(0, sizeOfPopulation, 2):
            # guard block
            if not i + 1 < sizeOfPopulation:
                print('ERR: cannot perform crossover (index out of bound {}'.format(i + 1))

            if np.random.rand() <= setting.crossoverProbability():
                tmpGenotype1 = population[i].genotype.genotype  # ???
                tmpGenotype2 = population[i + 1].genotype.genotype  # ???
                # randomly select cut point
                cutPoint = np.random.randint(1, genotypeLength)
                # print('cx:', population[i].genotype.genotype, '&', population[i + 1].genotype.genotype, 'in', cutPoint)
                for j in range(cutPoint, genotypeLength):
                    tmpGenotype1[j], tmpGenotype2[j] = tmpGenotype2[j], tmpGenotype1[j]
                population[i].setGenotype(tmpGenotype1)  # ???
                population[i + 1].setGenotype(tmpGenotype2)  # ???
                # print('ax:', population[i].genotype.genotype, '&', population[i + 1].genotype.genotype, 'in', cutPoint)


    # MUTATION
    @staticmethod
    def mutation(population: [Individual], setting: Setting):
        for individual in population:
            p = np.random.rand(individual.genotype.length)
            mutateGeneIndicles = [i for i,v in enumerate(p) if v <= setting.mutationProbability()]
            genotype = individual.genotype.genotype

            for geneIdx in mutateGeneIndicles:
                # print("MUT 1/2",genotype[geneIdx])
                mu = genotype[geneIdx]
                sigma = 1
                x = float("{:.2f}".format(normalvariate(mu, sigma)))
                # check if is in bounds
                if (
                    x >= setting.genotypeInfo().parametersDomain[geneIdx][0]
                    and x <= setting.genotypeInfo().parametersDomain[geneIdx][1]
                ):
                    individual.setGene(geneIdx,x)
                # print("MUT 2/2", genotype[geneIdx])
            individual.refresh()