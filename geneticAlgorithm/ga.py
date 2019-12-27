from geneticAlgorithm.population import Population
from problem.abstractProblem import Problem
from problem.x2 import X2


class Ga:
    def __init__(self):
        self._population = None
        self._problem = None

    def initPopulation(self, size):
        self._population = Population(size)

    def setProblem(self, problem: Problem):
        self._population.setProblem(problem)


if __name__ == "__main__":
    ga = Ga()
    ga.initPopulation(10)
    ga.setProblem(X2())

    for _ in range(15):
        print("\nGeneration {}".format(_))
        # raports
        ga._population.reportPopulationAverage()
        ga._population.raportBestIndividual()

        ga._population.rouletteReproduction()
        ga._population.singlePointCrossover()
        ga._population.mutation(0.01)

