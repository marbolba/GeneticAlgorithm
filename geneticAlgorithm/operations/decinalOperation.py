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
    def singlePointCrossover(
        population: [Individual], setting: Setting
    ):  ##this is averaging crossover
        for i in range(0, len(population), 2):
            # guard block
            if not i + 1 < len(population):
                print(
                    "ERR: cannot perform crossover (index out of bound {}".format(i + 1)
                )

            if setting.crossoverProbability() <= np.random.rand():
                tmpGenotype1 = population[i].genotype.genotype.copy()  # ???
                tmpGenotype2 = population[i + 1].genotype.genotype.copy()  # ???
                # randomly select in-between point
                for gen in range(population[i].genotype.length):
                    diff = (
                        population[i + 1].genotype.genotype[gen]
                        - population[i].genotype.genotype[gen]
                    )
                    if diff == 0:
                        cutPoint = 0
                    elif diff > 0:
                        cutPoint = np.random.randint(0, diff + 1)
                    else:
                        cutPoint = np.random.randint(diff, 0 + 1)
                    # print('cx:(',gen,')', tmpGenotype1, '&', tmpGenotype2,'in', cutPoint)
                    tmpGenotype1[gen] = tmpGenotype1[gen] + cutPoint
                    tmpGenotype2[gen] = tmpGenotype2[gen] - cutPoint
                    # print('ax:(',gen,')', tmpGenotype1, '&', tmpGenotype2, 'in', cutPoint)
                population[i].setGenotype(tmpGenotype1.copy())  # ???
                population[i + 1].setGenotype(tmpGenotype2.copy())  # ???

    # MUTATION
    @staticmethod
    def mutation(population: [Individual], setting: Setting):
        for indiv in population:
            p = np.random.rand(indiv.genotype.length)
            mutateGeneIndicles = [i for i,v in enumerate(p) if v <= setting.mutationProbability()]
            genotype = indiv.genotype.genotype

            for geneIdx in mutateGeneIndicles:
                # print("MUT 1/2",genotype[geneIdx])
                # do rozkladu normalnego
                mu = genotype[geneIdx]
                sigma = 1
                x = round(normalvariate(mu, sigma))
                # check if is in bounds
                if (
                    x >= setting.genotypeInfo().parametersDomain[geneIdx][0]
                    and x <= setting.genotypeInfo().parametersDomain[geneIdx][1]
                ):
                    indiv.setGene(geneIdx,x)
                # print("MUT 2/2", genotype[geneIdx])
            indiv.refresh()