class GenotypeInfo:
    def __init__(self):
        self.type = None
        self.mutation = None
        self.crossover = None
        self.parameters = None
        self.parametersWordLength = []
        self.parametersDomain = []  # eg.[(0, 20), (0, 40)]

    def validateParameters(self):
        return self.parameters == len(self.parametersWordLength) == len(self.parametersDomain)


class Setting:
    def populationSize(self):
        raise NotImplementedError("The method not implemented")

    def mutationProbability(self):
        raise NotImplementedError("The method not implemented")

    def crossoverProbability(self):
        raise NotImplementedError("The method not implemented")

    def genotypeInfo(self) -> GenotypeInfo:
        raise NotImplementedError("The method not implemented")