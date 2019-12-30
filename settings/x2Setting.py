from settings.abstractSettings import Setting


class X2Setting(Setting):
    def populationSize(self):
        return 10

    def mutationProbability(self):
        return 0.01

    def crossoverProbability(self):
        return 0.5
    
