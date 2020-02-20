import sys

from geneticAlgorithm.population import Population
from problem.abstractProblem import Problem
from settings.abstractSettings import Setting


class Ga:
    def __init__(self):
        self.population:Population = None
        self._setting:Setting = None
        self._problem:Problem = None

    def initPopulation(self):
        # Guardian block
        if self._setting is None or self._problem is None:
            print('ERR: setting or problem no set, cannot initialize population')
            sys.exit(0)

        self.population = Population()
        self.population.setProblem(self._problem)
        self.population.setSetting(self._setting)
        self.population.generateRandomPopulation()

    def setProblem(self, problem: Problem):
        self._problem = problem

    def setSetting(self, setting: Setting):
        self._setting = setting


