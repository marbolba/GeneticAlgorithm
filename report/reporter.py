import numpy as np
import os

from geneticAlgorithm.population import Population
from tools.terrainHandler import TerrainHandler
from geneticAlgorithm.individual import Individual


class Reporter:
    def __init__(self):
        self.best = []
        self.avg = []
        self.online = 0
        self.offline = 0

    def reportBestIndividual(self, population: Population, generationNr: int):
        sortedIndividuals = sorted(
            population.population, key=lambda x: x._adaptation, reverse=True
        )
        self.best.insert(generationNr, sortedIndividuals[0].getAdaptation())
        print(
            "Best individual: \n- genome: {} \n- value {} \n- adaptation: {} ".format(
                sortedIndividuals[0].genotype.toString(),
                sortedIndividuals[0].getValue(),
                sortedIndividuals[0].getAdaptation(),
            )
        )  # tmp without indiv object
        TerrainHandler.drawTerrainWithPoints(
            sortedIndividuals[0].getFenotype(), generationNr
        )

    def reportAllIndividuals(self, population: Population):
        print(
            list(
                map(
                    lambda indiv: (
                        population.genotype.toString(),
                        population.getAdaptation(),
                    ),
                    population.population,
                )
            )
        )

    def reportPopulationAverage(self, population: Population, generationNr: int):
        adaptationAvg = np.average(
            list(map(lambda indiv: indiv.getAdaptation(), population.population))
        )
        self.avg.insert(generationNr, adaptationAvg)
        print(
            "Population average: adaptation: {} ".format(adaptationAvg)
        )  # tmp without indiv object

    def reportResults(self, population: Population):
        sortedIndividuals = sorted(
            population.population, key=lambda x: x._adaptation, reverse=True
        )
        bestIndividual = sortedIndividuals[0]
        self.reportOutputPath(bestIndividual)
        self.saveToFile("avg", self.avg)
        self.saveToFile("best", self.best)
        self.saveToFile("online", self.online)
        self.saveToFile("offline", self.offline)
        # readable report
        historyFolder = f"{TerrainHandler.getName()}{TerrainHandler.getResultId()}"
        with open(f"{historyFolder}result.txt", "w") as text_file:
            text_file.write(
                "Generations nr: {} \n".format(settings.generationsNumber())
            )
            text_file.write("Population size: {} \n".format(settings.populationSize()))
            text_file.write("Best individual: {} \n".format(bestIndividual.getFenotype()))
            text_file.write("Avg history: {} \n".format(self.avg))
            text_file.write("Best history: {} \n".format(self.best))
            text_file.write("Convergence online: {} \n".format(self.online))
            text_file.write("Convergence offline: {} \n".format(self.offline))

    def reportOutputPath(self, bestIndividual:Individual):
        bestFenotype = bestIndividual.getFenotype()
        TerrainHandler.drawFinalRaport(bestFenotype, self.best, self.avg)

    def reportConvergence(self):
        self.online = np.mean(self.avg)
        self.offline = np.mean(self.best)
        print("Online convergence: {}".format(self.online))
        print("Offline convergence: {}".format(self.offline))

    def saveToFile(self, name, value):
        historyFolder = f"{TerrainHandler.getName()}{TerrainHandler.getResultId()}"
        self.checkIfFolderExists(historyFolder)
        np.save("{}{}".format(historyFolder, name), value)

    def checkIfFolderExists(self, folderPath):
        if not (os.path.exists(folderPath)):
            # create the directory you want to save to
            os.mkdir(folderPath)
