from geneticAlgorithm.ga import Ga
from problem.x2 import X2
from report.reporter import reportBestIndividual, reportPopulationAverage
from settings.x2Setting import X2Setting
from tools.rescaler import Rescaler


def runForX2():
    ga = Ga()
    ga.setSetting(X2Setting())
    ga.setProblem(X2())
    ga.initPopulation()

    for _ in range(15):
        print("\nGeneration {}".format(_))

        # raports
        reportPopulationAverage(ga.population)
        reportBestIndividual(ga.population)

        ga.population.rouletteReproduction()
        ga.population.singlePointCrossover()
        ga.population.mutation(0.01)

    # return np.load(fileName) #load data!!


if __name__ == "__main__":
    # runForX2()

    arr =
    print(Rescaler.renormalize())