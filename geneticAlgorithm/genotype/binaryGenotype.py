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
        print('Genotype: ', self.toString())

    # converts binary array to single binary value
    def toString(self, genotype: [] = None):
        if genotype is not None:
            return int(''.join([str(elem) for elem in genotype]))
        else:
            return int(''.join([str(elem) for elem in self.genotype]))

    def getPartOfGenotype(self, startIdx, endIdx):
        return self.genotype[startIdx:endIdx]

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
