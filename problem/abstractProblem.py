from abc import ABC


class Problem:
    def goalFunction(self, value):
        raise NotImplementedError("The method not implemented")

    def adaptationFunction(self, value):
        raise NotImplementedError("The method not implemented")

    def genotypeInfo(self):
        raise NotImplementedError("The method not implemented")
