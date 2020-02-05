from geneticAlgorithm.genotype.abstractGenotype import Genotype
from geneticAlgorithm.operations.abstractOperation import Operation


class DecimalOperation(Operation):
    def singlePointCrossover(self,genotype1:Genotype,genotype2:Genotype):
        for i in range(0, len(self.population), 2):
            # guard block
            if not i + 1 < len(self.population):
                print('ERR: cannot perform crossover (index out of bound {}'.format(i + 1))

            if self._setting.crossoverProbability() <= np.random.rand():

                tmpGenotype1 = self.population[i].genotype.genotype.copy()  # ???
                tmpGenotype2 = self.population[i + 1].genotype.genotype.copy()  # ???
                # randomly select cut point
                cutPoint = np.random.randint(1, self.population[i].genotype.length)
                # print('cx:', self.population[i].genotype.genotype(), '&', self.population[i + 1].genotype.genotype(), 'in', cutPoint)
                for j in range(cutPoint, self.population[i].genotype.length):
                    tmpGenotype1[j], tmpGenotype2[j] = tmpGenotype2[j], tmpGenotype1[j]
                self.population[i].setGenotype(tmpGenotype1.copy())  # ???
                self.population[i + 1].setGenotype(tmpGenotype2.copy())  # ???
                # print('ax:', self.population[i].genotype.genotype(), '&', self.population[i + 1].genotype.genotype(), 'in', cutPoint)

    def mutation(self,genotype:Genotype):
        for indiv in self.population:
            for geneIdx in range(len(indiv.genotype.genotype)):
                if np.random.rand() <= self._setting.mutationProbability():
                    tmpGenotype = indiv.genotype.genotype.copy()
                    tmpGenotype[geneIdx] = 0 if tmpGenotype[geneIdx] == 1 else 0
                    indiv.setGenotype(tmpGenotype.copy())

