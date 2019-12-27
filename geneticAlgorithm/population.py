import random
import copy
import numpy as np

from geneticAlgorithm.individual import Individual
from problem.abstractProblem import Problem


class Population:
    def __init__(self, size):
        self._population = []
        self._size = size

        self._generateRandomPopulation()

    def _generateRandomPopulation(self):
        for _ in range(self._size):
            self._population.append(Individual())

    def setProblem(self, problem: Problem):
        for individual in self._population:
            individual.setProblem(problem)

    def raportBestIndividual(self):
        # dtype = [('_adaptation', float)]
        # a = np.array(self._population, dtype=dtype)
        # sortedIndividuals = np.sort(a, order='_adaptation')[::-1]
        sortedIndividuals = sorted(self._population, key=lambda x: x._adaptation, reverse=True)
        print('Best individual: genome: {} value {} adaptation: {} '.format(sortedIndividuals[0]._genotype.getGenotype(), sortedIndividuals[0].getValue(),
                                                                            sortedIndividuals[0].getAdaptation()))  # tmp without indiv object
        print(list(map(lambda indiv: (indiv._genotype.getGenotype(), indiv.getAdaptation()), self._population)))

    def reportPopulationAverage(self):
        adaptationAvg = np.average(list(map(lambda indiv: indiv.getAdaptation(), self._population)))
        print('Population average: adaptation: {} '.format(adaptationAvg))  # tmp without indiv object

    def rouletteReproduction(self):
        # creating select chance array
        adaptationSum = 0
        selectChance = []
        for individual in self._population:
            adaptationSum += individual.getAdaptation()
        for individual in self._population:
            selectChance.append(individual.getAdaptation() / adaptationSum)
        selectChance = np.cumsum(selectChance)

        # select new population
        newPopulation = []
        selected = np.random.rand(len(self._population))
        for sel in selected:
            for propIdx in range(len(selectChance)):
                if sel <= selectChance[propIdx]:
                    newPopulation.append(copy.deepcopy(self._population[propIdx]))
                    break

        # override with new population
        self._population = newPopulation

    def singlePointCrossover(self):
        newPopulation = []
        for i in range(0, len(self._population), 2):
            # guard block
            if not i + 1 < len(self._population):
                print('ERR: cannot perform crossover (index out of bound {}'.format(i + 1))

            tmpGenotype1 = self._population[i]._genotype.genotype.copy()  # ???
            tmpGenotype2 = self._population[i + 1]._genotype.genotype.copy()  # ???
            # randomly select cut point
            cutPoint = np.random.randint(1, self._population[i]._genotype.length)
            # print('cx:', self._population[i]._genotype.getGenotype(), '&', self._population[i + 1]._genotype.getGenotype(), 'in', cutPoint)
            for j in range(cutPoint, self._population[i]._genotype.length):
                tmpGenotype1[j], tmpGenotype2[j] = tmpGenotype2[j], tmpGenotype1[j]
            self._population[i].setGenotype(tmpGenotype1.copy())  # ???
            self._population[i + 1].setGenotype(tmpGenotype2.copy())  # ???
            # print('ax:', self._population[i]._genotype.getGenotype(), '&', self._population[i + 1]._genotype.getGenotype(), 'in', cutPoint)

    def mutation(self,probability):
        for indiv in self._population:
            for geneIdx in range(len(indiv._genotype.genotype)):
                if np.random.rand() <= probability:
                    tmpGenotype = indiv._genotype.genotype.copy()
                    tmpGenotype[geneIdx] = 0 if tmpGenotype[geneIdx] == 1 else 0
                    indiv.setGenotype(tmpGenotype.copy())
