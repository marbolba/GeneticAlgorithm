from geneticAlgorithm.ga import Ga
from problem.x2 import X2
from settings.x2Setting import X2Setting


def runForX2():
    ga = Ga()
    ga.setSetting(X2Setting())
    ga.setProblem(X2())
    ga.initPopulation()

    for _ in range(15):
        print("\nGeneration {}".format(_))
        # raports
        ga.population.reportPopulationAverage()
        ga.population.raportBestIndividual()

        ga.population.rouletteReproduction()
        ga.population.singlePointCrossover()
        ga.population.mutation(0.01)


if __name__ == "__main__":
    runForX2()
