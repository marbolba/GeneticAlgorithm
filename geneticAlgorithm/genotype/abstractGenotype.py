from settings.abstractSettings import GenotypeInfo


class Genotype:
    def __init__(self):
        self.genotype = []
        self.genotypeInfo:GenotypeInfo = None
        self.length = 0

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

    def getPartOfGenotype(self, startIdx, endIdx):
        return self.genotype[startIdx:endIdx]

    def randomize(self):
        raise NotImplementedError("The method not implemented")

    def toString(self):
        raise NotImplementedError("The method not implemented")

    def calculateValue(self):
        raise NotImplementedError("The method not implemented")