import numpy as np

from geneticAlgorithm.genotype.abstractGenotype import Genotype
from tools import converter


class BinaryGenotype(Genotype):

    def randomize(self):
        # guard block
        if self.length == 0:
            print('ERR: Genotype length not set!')
            return

        # binary genotype
        for i in range(self.length):
            self.genotype.append(np.random.randint(0, 2))  # binary
        print('Genotype: ', self.toString())

    # converts binary array to single binary value
    def toString(self):
        return int(''.join([str(elem) for elem in self.genotype]))

    # calculates bin -> values
    def calculateValue(self):
        values = []
        for i in range(self.genotypeInfo.parameters):
            startIdx = np.sum(self.genotypeInfo.parametersWordLength[0:i])
            parameterGenotype = self.getPartOfGenotype(
                int(startIdx),
                int(startIdx + self.genotypeInfo.parametersWordLength[i])
            )
            # calculate value in it's range
            maxVal = converter.maxBinaryValue(parameterGenotype.__len__())
            actVal = converter.binToDec(self.toString(parameterGenotype))
            minDomain = self.genotypeInfo.parametersDomain[i][0]
            maxDomain = self.genotypeInfo.parametersDomain[i][1]
            newVal = round(minDomain + (actVal/maxVal * (maxDomain-minDomain))) # values are rounded
            values.append(newVal)
        return values
