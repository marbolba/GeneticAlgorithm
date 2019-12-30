from abc import ABC


class Problem:
    def genotypeLenght(self):
        raise NotImplementedError("The method not implemented")

    def goalFunction(self, value):
        raise NotImplementedError("The method not implemented")

    def adaptationFunction(self, value):
        raise NotImplementedError("The method not implemented")
