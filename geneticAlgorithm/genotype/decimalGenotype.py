import numpy as np

from geneticAlgorithm.genotype.abstractGenotype import Genotype
from tools import converter


class DecimalGenotype(Genotype):
    def __init__(self):
        super(DecimalGenotype, self).__init__()
        self.minVal = 0
        self.maxVal = 10

    def randomize(self):
        # guard block
        if self.length == 0:
            print('ERR: Genotype length not set!')
            return

        # binary genotype
        for i in range(self.length):
            self.genotype.append(np.random.randint(self.minVal, self.maxVal + 1))  # decimal, customizable
        print('Genotype: ', self.toString())

    # TODO make this prettier
    def toString(self, genotype: [] = None):
        if genotype is not None:
            return int(''.join([str(elem) for elem in genotype]))
        else:
            return int(''.join([str(elem) for elem in self.genotype]))

    def calculateValue(self):
        values = []
        for i in range(self.genotypeInfo.parameters):
            startIdx = np.sum(self.genotypeInfo.parametersWordLength[0:i])
            parameterGenotype = self.getPartOfGenotype(
                int(startIdx),
                int(startIdx + self.genotypeInfo.parametersWordLength[i])
            )
            # calculate value in it's range
            maxVal = pow(10, parameterGenotype.__len__())
            actVal = parameterGenotype.#how to convert [5,2] to 52 ?
            print(actVal)
            minDomain = self.genotypeInfo.parametersDomain[i][0]
            maxDomain = self.genotypeInfo.parametersDomain[i][1]
            newVal = round(minDomain + (actVal / maxVal * (maxDomain - minDomain)))  # values are rounded
            values.append(newVal)
        return values
