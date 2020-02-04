from settings.abstractSettings import Setting


class X2Setting(Setting):
    def populationSize(self):
        return 30

    def mutationProbability(self):
        return 0.1

    def crossoverProbability(self):
        return 0.5
    
