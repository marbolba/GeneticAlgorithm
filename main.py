from geneticAlgorithm.ga import Ga
from problem.x2 import X2
from settings.x2Setting import X2Setting



def runForX2():
    ga = Ga()
    ga.setSetting(X2Setting())
    ga.setProblem(X2())
    ga.initPopulation()

    ga.startAlgorithm()


if __name__ == "__main__":
    runForX2()
