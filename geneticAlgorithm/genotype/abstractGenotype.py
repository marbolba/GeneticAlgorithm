from problem.abstractProblem import GenotypeInfo


class Genotype:
    def __init__(self):
        self.genotype = []
        self.genotypeInfo:GenotypeInfo = None
        self.length = 0

    def randomize(self):
        raise NotImplementedError("The method not implemented")

    def toString(self):
        raise NotImplementedError("The method not implemented")