import copy

import numpy as np

from geneticAlgorithm.genotype.abstractGenotype import Genotype
from geneticAlgorithm.individual import Individual
from geneticAlgorithm.operations.abstractOperation import Operation
from geneticAlgorithm.population import Population
from settings.abstractSettings import Setting


class BinaryOperation(Operation):
    @staticmethod
    def singlePointCrossover(population: [Individual], setting: Setting):
        for i in range(0, len(population), 2):
            # guard block
            if not i + 1 < len(population):
                print(
                    "ERR: cannot perform crossover (index out of bound {}".format(i + 1)
                )

            if setting.crossoverProbability() <= np.random.rand():
                tmpGenotype1 = population[i].genotype.genotype.copy()  # ???
                tmpGenotype2 = population[i + 1].genotype.genotype.copy()  # ???
                # randomly select cut point
                cutPoint = np.random.randint(1, population[i].genotype.length)
                # print('cx:',i, population[i].genotype.genotype, '&', population[i + 1].genotype.genotype, 'in', cutPoint)
                for j in range(cutPoint, population[i].genotype.length):
                    tmpGenotype1[j], tmpGenotype2[j] = tmpGenotype2[j], tmpGenotype1[j]
                population[i].setGenotype(tmpGenotype1.copy())  # ???
                population[i + 1].setGenotype(tmpGenotype2.copy())  # ???
                # print('ax:',i, population[i].genotype.genotype, '&', population[i + 1].genotype.genotype, 'in', cutPoint)

    @staticmethod
    def mutation(population: [Individual], setting: Setting):
        for indiv in population:
            for geneIdx in range(len(indiv.genotype.genotype)):
                if np.random.rand() <= setting.mutationProbability():
                    tmpGenotype = indiv.genotype.genotype.copy()
                    tmpGenotype[geneIdx] = 0 if tmpGenotype[geneIdx] == 1 else 0
                    indiv.setGenotype(tmpGenotype.copy())
