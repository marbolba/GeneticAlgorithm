import numpy as np

from geneticAlgorithm.genotype.abstractGenotype import Genotype
from problem.abstractProblem import GenotypeInfo
from tools import converter


class BinaryGenotype(Genotype):

    def setGenotypeInfo(self, genotypeInfo: GenotypeInfo):
        if genotypeInfo.validateParameters():
            self.genotypeInfo = genotypeInfo
            self.setLength()
        else:
            print("ERR: Genotype info invalid")

    def setLength(self):
        # Guardian block
        if self.genotypeInfo is None:
            print("ERR: Genotype info not provided")
            return

        for wordLength in self.genotypeInfo.parametersWordLength:
            self.length += wordLength

    def randomize(self):
        # guard block
        if self.length == 0:
            print('ERR: Genotype length not set!')
            return

        # binary genotype
        for i in range(self.length):
            self.genotype.append(np.random.randint(0, 2))  # binary
        print('Genotype: ', self.getGenotype())

    # converts binary array to single binary value
    def getGenotype(self):
        return int(''.join([str(elem) for elem in self.genotype]))

    # calculates bin -> value
    def calculateValue(self):
        return converter.binToDec(self.getGenotype())
