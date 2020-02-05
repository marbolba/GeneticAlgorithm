import numpy as np

from problem.abstractProblem import Problem


class X2(Problem):
    def goalFunction(self, values):
        return np.power(values, 2)

    def adaptationFunction(self, values):
        return values[0] + values[1]
