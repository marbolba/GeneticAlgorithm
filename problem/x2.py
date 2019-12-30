import numpy as np

from problem.abstractProblem import Problem


class X2(Problem):
    def goalFunction(self, value):
        return np.power(value, 2)

    def adaptationFunction(self, value):
        return np.power(value, 2)
