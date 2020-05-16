import numpy as np

from geneticAlgorithm.population import Population
from tools.terrainHandler import TerrainHandler


class Reporter:
    def __init__(self):
        self.best = []
        self.avg = []

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

    def reportOutputPath(self, population: Population):
        sortedIndividuals = sorted(
            population.population, key=lambda x: x._adaptation, reverse=True
        )
        bestFenotype = sortedIndividuals[0].getFenotype()
        TerrainHandler.drawFinalRaport(bestFenotype, self.best, self.avg)
