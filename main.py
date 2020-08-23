from geneticAlgorithm.ga import Ga
from problem.terrainProblem import TerrainProblem
from problem.terrainProblemSel import TerrainProblemSel
from problem.x2Problem import X2Problem
from settings.terrainSettings import TerrainSetting
from problem.terrainProblemPolar import TerrainProblemPolar
from settings.terrainSettingsPolar import TerrainSettingPolar
from settings.terrainSettingsSel import TerrainSettingSel
from settings.x2Setting import X2Setting
from tools.terrainHandler import TerrainHandler


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


def runForTerrainSel():
    ga = Ga()
    ga.setSetting(TerrainSettingSel())
    ga.setProblem(TerrainProblemSel())
    ga.initPopulation()

    ga.startAlgorithm()


def runForTerrainPolar():
    ga = Ga()
    ga.setSetting(TerrainSettingPolar())
    ga.setProblem(TerrainProblemPolar())
    ga.initPopulation()

    ga.startAlgorithm()


if __name__ == "__main__":
    TerrainHandler.setName("21-cze-2020_004739")
    runForTerrainPolar()
