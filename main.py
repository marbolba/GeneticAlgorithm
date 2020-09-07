from geneticAlgorithm.ga import Ga
from problem.terrainProblem import TerrainProblem
from settings.terrainSettings import TerrainSetting
from problem.terrainProblemSel import TerrainProblemSel
from settings.terrainSettingsSel import TerrainSettingSel
from problem.x2Problem import X2Problem
from settings.x2Setting import X2Setting
from problem.terrainProblemPolar import TerrainProblemPolar
from settings.terrainSettingsPolar import TerrainSettingPolar
from problem.terrainProblemPolarSel import TerrainProblemPolarSel
from settings.terrainSettingsPolarSel import TerrainSettingPolarSel
from problem.terrainProblemFlipbit import TerrainProblemFlipbit
from settings.terrainSettingsFlipbit import TerrainSettingFlipbit
from problem.terrainProblemBoxSel import TerrainProblemBoxSel
from settings.terrainSettingsBoxSel import TerrainSettingBoxSel
from problem.terrainProblemPolarFlipbit import TerrainProblemPolarFlipbit
from settings.terrainSettingsPolarFlipbit import TerrainSettingPolarFlipbit
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


def runForTerrainFlipbit():
    ga = Ga()
    ga.setSetting(TerrainSettingFlipbit())
    ga.setProblem(TerrainProblemFlipbit())
    ga.initPopulation()

    ga.startAlgorithm()


def runForTerrainPolar():
    ga = Ga()
    ga.setSetting(TerrainSettingPolar())
    ga.setProblem(TerrainProblemPolar())
    ga.initPopulation()

    ga.startAlgorithm()


def runForTerrainPolarSel():
    ga = Ga()
    ga.setSetting(TerrainSettingPolarSel())
    ga.setProblem(TerrainProblemPolarSel())
    ga.initPopulation()

    ga.startAlgorithm()


def runForTerrainPolarFlipbit():
    ga = Ga()
    ga.setSetting(TerrainSettingPolarFlipbit())
    ga.setProblem(TerrainProblemPolarFlipbit())
    ga.initPopulation()

    ga.startAlgorithm()


def runForTerrainBoxSel():
    ga = Ga()
    ga.setSetting(TerrainSettingBoxSel())
    ga.setProblem(TerrainProblemBoxSel())
    ga.initPopulation()

    ga.startAlgorithm()


if __name__ == "__main__":
    TerrainHandler.setName("case2rounded")
    # runForTerrain()               # ch1
    # runForTerrainSel()            # ch2
    runForTerrainFlipbit()        # ch3
    # runForTerrainPolar()          # ch4
    # runForTerrainPolarSel()       # ch5
    # runForTerrainPolarFlipbit()   # ch6

    # runForTerrainFlipbit()     
