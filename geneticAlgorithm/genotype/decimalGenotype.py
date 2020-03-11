import numpy as np

from geneticAlgorithm.genotype.abstractGenotype import Genotype
from tools import converter


class DecimalGenotype(Genotype):
    def __init__(self):
        super(DecimalGenotype, self).__init__()

    def randomize(self):
        # guard block
        if self.length == 0:
            print('ERR: Genotype length not set!')
            return

        # binary genotype
        for i in range(self.length):
            self.genotype.append(np.random.randint(self.genotypeInfo.parametersDomain[i][0], self.genotypeInfo.parametersDomain[i][1] + 1))  # decimal, customizable
        print('Genotype: ', self.toString())

    # TODO make this prettier
    def toString(self):
        return int(''.join([str(elem) for elem in self.genotype]))

    def calculateValue(self):
        values = []
        for i in range(0,self.genotypeInfo.parameters):
            startIdx = np.sum(self.genotypeInfo.parametersWordLength[0:i])
            parameterGenotype = self.getPartOfGenotype(
                int(startIdx),
                int(startIdx + self.genotypeInfo.parametersWordLength[i])
            )
            values.append(parameterGenotype[0])
        return values
