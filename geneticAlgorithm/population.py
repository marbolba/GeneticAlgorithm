import random
import copy
import numpy as np

from geneticAlgorithm.individual import Individual
from problem.abstractProblem import Problem
from settings.abstractSettings import Setting


class Population:
    def __init__(self):
        self.population: [Individual] = []
        self.setting: Setting = None
        self.problem: Problem = None
        self.reproductionImplementation = None
        self.successionImplementation = None
        self.mutationImplementation = None
        self.crossoverImplementation = None

    def generateRandomPopulation(self):
        # Guardian block
        if self.setting is None:
            print("ERR: cannot generate population: lack of settings")
        if self.problem is None:
            print("ERR: cannot generate population: lack of problem")
        for _ in range(self.setting.populationSize()):
            self.population.append(Individual())
        for individual in self.population:
            individual.setSetting(self.setting)
        for individual in self.population:
            individual.setProblem(self.problem)

    def setPopulation(self, newPopulation: [Individual]):
        self.population = newPopulation

    def setProblem(self, problem: Problem):
        self.problem = problem

    def setSetting(self, setting: Setting):
        self.setting = setting
        self.setting.genotypeInfo().validateParameters()
        self.reproductionImplementation = setting.genotypeInfo().reproduction
        self.successionImplementation = setting.genotypeInfo().succession
        self.crossoverImplementation = setting.genotypeInfo().crossover
        self.mutationImplementation = setting.genotypeInfo().mutation

    # DO NOT CHANGE
    def reproduction(self):
        return self.reproductionImplementation(self)

    def succession(self, newPopulation):
        self.successionImplementation(self, newPopulation)

    def crossover(self):
        self.crossoverImplementation(self.population, self.setting)

    def mutation(self):
        self.mutationImplementation(self.population, self.setting)
