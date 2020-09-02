import numpy as np
import os

from geneticAlgorithm.population import Population
from tools.terrainHandler import TerrainHandler
from geneticAlgorithm.individual import Individual
from settings.abstractSettings import Setting


class Reporter:
    def __init__(self, setting: Setting):
        self.settings = setting
        self.best = []
        self.avg = []
        self.online = []
        self.offline = []

    def reportBestIndividual(self, population: Population, generationNr: int):
        bestIndividual = sorted(
            population.population, key=lambda x: x._adaptation, reverse=True
        )[0]
        bestAdaptation = float("{:.2f}".format(bestIndividual.getAdaptation()))
        self.best.insert(generationNr, bestAdaptation)
        """print(
            "Best individual: \n- genome: {} \n- value {} \n- adaptation: {} ".format(
                bestIndividual.genotype.toString(),
                bestIndividual.getValue(),
                bestAdaptation,
            )
        )  # tmp without indiv object
        TerrainHandler.drawTerrainWithPoints(
            bestIndividual.getFenotype(), generationNr
        )"""

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
        adaptationAvg = float("{:.2f}".format(adaptationAvg))
        self.avg.insert(generationNr, adaptationAvg)
        """print(
            "Population average: adaptation: {} ".format(adaptationAvg)
        )  # tmp without indiv object"""

    def reportResults(self, population: Population):
        sortedIndividuals = sorted(
            population.population, key=lambda x: x._adaptation, reverse=True
        )
        bestIndividual = sortedIndividuals[0]

        # calculate quality
        # distance
        best_individual_end_point = bestIndividual.getFenotype()[
            len(bestIndividual.getFenotype()) - 1
        ]
        end_point = TerrainHandler.getWaypoints()[1]
        distance_to_goal = TerrainHandler.distance(best_individual_end_point, end_point)
        # cost
        cost = 0
        valuesLoc = bestIndividual.getFenotype().copy()
        valuesLoc.insert(0, TerrainHandler.getWaypoints()[0])
        for i in range(0, len(valuesLoc) - 1):
            cost = cost + TerrainHandler.travelCost(valuesLoc[i], valuesLoc[i + 1])
        distance_to_goal = float("{:.2f}".format(distance_to_goal))
        cost = float("{:.2f}".format(cost))

        # report to files
        self.reportOutputPath(bestIndividual)
        self.saveToFile("avg", self.avg)
        self.saveToFile("best", self.best)
        self.saveToFile("online", self.online)
        self.saveToFile("offline", self.offline)
        self.saveToFile("distance_to_goal", distance_to_goal)
        self.saveToFile("cost_of_travel", cost)

        # readable report
        historyFolder = f"{TerrainHandler.getName()}{TerrainHandler.getResultId()}"
        with open(f"{historyFolder}result.txt", "w") as text_file:
            text_file.write(
                "Generations nr: {} \n".format(self.settings.generationsNumber())
            )
            text_file.write(
                "Population size: {} \n".format(self.settings.populationSize())
            )
            text_file.write(
                "Best individual: {} \n".format(bestIndividual.getFenotype())
            )
            text_file.write("Avg history: {} \n".format(self.avg))
            text_file.write("Best history: {} \n".format(self.best))
            text_file.write("Distance to goal: {}\n".format(distance_to_goal))
            text_file.write("Cost of travel: {}\n".format(cost))
            text_file.write(
                "Convergence online: {:.2f} \n".format(
                    self.online[len(self.online) - 1]
                )
            )
            text_file.write(
                "Convergence offline: {:.2f} \n".format(
                    self.offline[len(self.offline) - 1]
                )
            )

    def reportOutputPath(self, bestIndividual: Individual):
        bestFenotype = bestIndividual.getFenotype()
        TerrainHandler.drawFinalRaport(bestFenotype, self.best, self.avg)

    def reportConvergence(self):
        self.online.append(float("{:.2f}".format(np.mean(self.avg))))
        self.offline.append(float("{:.2f}".format(np.mean(self.best))))

    def saveToFile(self, name, value):
        historyFolder = f"{TerrainHandler.getName()}{TerrainHandler.getResultId()}"
        self.checkIfFolderExists(historyFolder)
        np.save("{}{}".format(historyFolder, name), value)

    def checkIfFolderExists(self, folderPath):
        if not (os.path.exists(folderPath)):
            # create the directory you want to save to
            os.mkdir(folderPath)
