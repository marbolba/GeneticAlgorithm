from geneticAlgorithm.ga import Ga
from problem.x2 import X2
from report.reporter import reportBestIndividual, reportPopulationAverage
from settings.x2Setting import X2Setting



def runForX2():
    ga = Ga()
    ga.setSetting(X2Setting())
    ga.setProblem(X2())
    ga.initPopulation()

    for _ in range(10):
        print("\nGeneration {}".format(_))
        # raports
        reportPopulationAverage(ga.population)
        reportBestIndividual(ga.population)

        ga.population.rouletteReproduction()
        ga.population.crossover()
        ga.population.mutation()


if __name__ == "__main__":
    runForX2()
