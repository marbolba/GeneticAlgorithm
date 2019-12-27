import numpy as np

from tools import converter


class BinaryGenotype:
    def __init__(self):
        self.genotype = []
        self.length = 0

    def setLength(self, len):
        self.length = len

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

