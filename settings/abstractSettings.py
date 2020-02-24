class GenotypeInfo:
    def __init__(self):
        self.type = None

        self.reproduction = None
        self.mutation = None
        self.crossover = None

        self.parameters = None
        self.parametersWordLength = []
        self.parametersDomain = []  # eg.[(0, 20), (0, 40)]

    def validateParameters(self):
        return self.parameters == len(self.parametersWordLength) == len(self.parametersDomain) \
               and self.type is not None and self.reproduction is not None and self.mutation is not None and self.crossover


class Setting:
    def generationsNumber(self):
        raise NotImplementedError("The method not implemented")

    def populationSize(self):
        raise NotImplementedError("The method not implemented")

    def mutationProbability(self):
        raise NotImplementedError("The method not implemented")

    def crossoverProbability(self):
        raise NotImplementedError("The method not implemented")

    def genotypeInfo(self) -> GenotypeInfo:
        raise NotImplementedError("The method not implemented")
