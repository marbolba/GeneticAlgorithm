from abc import ABC


class GenotypeInfo:
    def __init__(self):
        self.parameters = None
        self.parametersWordLength = []
        self.parametersDomain = []  # eg.[(0, 20), (0, 40)]

    def validateParameters(self):
        return self.parameters == len(self.parametersWordLength) == len(self.parametersDomain)


class Problem:
    # Problem function
    def goalFunction(self, value):
        raise NotImplementedError("The method not implemented")

    # Solution salary
    def adaptationFunction(self, value):
        raise NotImplementedError("The method not implemented")

    def genotypeInfo(self):
        raise NotImplementedError("The method not implemented")
