import numpy as np

from geneticAlgorithm.population import Population
from tools.terrainHandler import TerrainHandler


def reportBestIndividual(population: Population):
    sortedIndividuals = sorted(
        population.population, key=lambda x: x._adaptation, reverse=True
    )
    print(
        "Best individual: genome: {} value {} adaptation: {} ".format(
            sortedIndividuals[0].genotype.toString(),
            sortedIndividuals[0].getValue(),
            sortedIndividuals[0].getAdaptation(),
        )
    )  # tmp without indiv object


def reportAllIndividuals(population: Population):
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


def reportPopulationAverage(population: Population):
    adaptationAvg = np.average(
        list(map(lambda indiv: indiv.getAdaptation(), population.population))
    )
    print(
        "Population average: adaptation: {} ".format(adaptationAvg)
    )  # tmp without indiv object


def reportOutputPath(population: Population):
    sortedIndividuals = sorted(
        population.population, key=lambda x: x._adaptation, reverse=True
    )
    values = sortedIndividuals[0].getFenotype()
    TerrainHandler.drawTerrainWithPoints(values)
