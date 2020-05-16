import sys
import time

from geneticAlgorithm.population import Population
from problem.abstractProblem import Problem
from report.reporter import Reporter
from settings.abstractSettings import Setting
from tools.timeFoo import timeFoo


class Ga:
    def __init__(self):
        self.population: Population = None
        self.setting: Setting = None
        self.problem: Problem = None
        self.reporter: Reporter = Reporter()

    @timeFoo
    def startAlgorithm(self):
        start_time = time.time()
        for generationId in range(self.setting.generationsNumber()):
            print(
                f"\nGeneration {generationId+1}, in time {(time.time()-start_time):.2f} seconds"
            )
            # raports
            self.reporter.reportPopulationAverage(self.population, generationId)
            self.reporter.reportBestIndividual(self.population, generationId)

            start_time = time.time()
            newPopulation = self.population.reproduction()
            self.population.succession(newPopulation)
            self.population.crossover()
            self.population.mutation()
        self.reporter.reportOutputPath(self.population)

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
