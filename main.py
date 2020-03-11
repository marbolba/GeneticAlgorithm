from geneticAlgorithm.ga import Ga
from problem.terrainProblem import TerrainProblem
from problem.x2Problem import X2Problem
from settings.terrainSettings import TerrainSetting
from settings.x2Setting import X2Setting


def runForX2():
    ga = Ga()
    ga.setSetting(X2Setting())
    ga.setProblem(X2Problem())
    ga.initPopulation()

    ga.startAlgorithm()


def runForTerrain():
    ga = Ga()
    ga.setSetting(TerrainSetting())
    ga.setProblem(TerrainProblem())
    ga.initPopulation()

    ga.startAlgorithm()


if __name__ == "__main__":
    runForTerrain()
