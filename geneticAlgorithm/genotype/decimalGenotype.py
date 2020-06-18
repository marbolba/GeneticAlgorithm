import numpy as np

from geneticAlgorithm.genotype.abstractGenotype import Genotype
from tools import converter


class DecimalGenotype(Genotype):
    def __init__(self):
        super(DecimalGenotype, self).__init__()

    def randomize(self):
        # guard block
        if self.length == 0:
            print("ERR: Genotype length not set!")
            return

        # binary genotype
        for i in range(self.length):
            rg = (
                self.genotypeInfo.parametersDomain[i][1]
                - self.genotypeInfo.parametersDomain[i][0]
            )
            randVal = self.genotypeInfo.parametersDomain[i][0] + np.random.rand() * rg
            self.genotype.append(
                float("{:.2f}".format(randVal))
            )  # decimal, customizable
        # print("Genotype: ", self.toString())

    def toString(self):
        return "".join([str(elem) + "|" for elem in self.genotype])

    def calculateValue(self):
        return self.genotype
