import sys
import time

from geneticAlgorithm.population import Population
from problem.abstractProblem import Problem
from report.reporter import (
    reportPopulationAverage,
    reportBestIndividual,
    reportOutputPath,
)
from settings.abstractSettings import Setting


class Ga:
    def __init__(self):
        self.population: Population = None
        self.setting: Setting = None
        self.problem: Problem = None

    def startAlgorithm(self):
        start_time = time.time()
        for generationId in range(self.setting.generationsNumber()):
            print("\nGeneration {0}, in time {1:.2f} seconds".format(generationId,time.time()-start_time))
            # raports
            reportPopulationAverage(self.population)
            reportBestIndividual(self.population)

            start_time = time.time()
            newPopulation = self.population.reproduction()
            self.population.succession(newPopulation)
            self.population.crossover()
            self.population.mutation()
        reportOutputPath(self.population)

    def initPopulation(self):
        # Guardian block
        if self.setting is None or self.problem is None:
            print("ERR: setting or problem no set, cannot initialize population")
            sys.exit(0)

        self.population = Population()
        self.population.setProblem(self.problem)
        self.population.setSetting(self.setting)
        self.population.generateRandomPopulation()

    def setProblem(self, problem: Problem):
        self.problem = problem

    def setSetting(self, setting: Setting):
        self.setting = setting
