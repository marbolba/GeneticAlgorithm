import random
import copy
import numpy as np

from geneticAlgorithm.individual import Individual
from problem.abstractProblem import Problem
from settings.abstractSettings import Setting


class Population:
    def __init__(self):
        self.population:[Individual] = []
        self._setting: Setting = None
        self._problem: Problem = None

    def generateRandomPopulation(self):
        # Guardian block
        if self._setting is None:
            print("ERR: cannot generate population: lack of settings")
        if self._problem is None:
            print("ERR: cannot generate population: lack of problem")
        for _ in range(self._setting.populationSize()):
            self.population.append(Individual())
        for individual in self.population:
            individual.setSetting(self._setting)
        for individual in self.population:
            individual.setProblem(self._problem)

    def setProblem(self, problem: Problem):
        self._problem = problem

    def setSetting(self, setting: Setting):
        self._setting = setting

    def rouletteReproduction(self):
        # creating select chance array
        adaptationSum = 0
        selectChance = []
        for individual in self.population:
            adaptationSum += individual.getAdaptation()
        for individual in self.population:
            selectChance.append(individual.getAdaptation() / adaptationSum)
        selectChance = np.cumsum(selectChance)

        # select new population
        newPopulation = []
        selected = np.random.rand(len(self.population))
        for sel in selected:
            for propIdx in range(len(selectChance)):
                if sel <= selectChance[propIdx]:
                    newPopulation.append(copy.deepcopy(self.population[propIdx]))
                    break

        # override with new population
        self.population = newPopulation

    def singlePointCrossover(self):
        for i in range(0, len(self.population), 2):
            # guard block
            if not i + 1 < len(self.population):
                print('ERR: cannot perform crossover (index out of bound {}'.format(i + 1))

            if self._setting.crossoverProbability() <= np.random.rand():

                tmpGenotype1 = self.population[i].genotype.genotype.copy()  # ???
                tmpGenotype2 = self.population[i + 1].genotype.genotype.copy()  # ???
                # randomly select cut point
                cutPoint = np.random.randint(1, self.population[i].genotype.length)
                # print('cx:', self.population[i].genotype.genotype(), '&', self.population[i + 1].genotype.genotype(), 'in', cutPoint)
                for j in range(cutPoint, self.population[i].genotype.length):
                    tmpGenotype1[j], tmpGenotype2[j] = tmpGenotype2[j], tmpGenotype1[j]
                self.population[i].setGenotype(tmpGenotype1.copy())  # ???
                self.population[i + 1].setGenotype(tmpGenotype2.copy())  # ???
                # print('ax:', self.population[i].genotype.genotype(), '&', self.population[i + 1].genotype.genotype(), 'in', cutPoint)

    def mutation(self):
        for indiv in self.population:
            for geneIdx in range(len(indiv.genotype.genotype)):
                if np.random.rand() <= self._setting.mutationProbability():
                    tmpGenotype = indiv.genotype.genotype.copy()
                    tmpGenotype[geneIdx] = 0 if tmpGenotype[geneIdx] == 1 else 0
                    indiv.setGenotype(tmpGenotype.copy())

