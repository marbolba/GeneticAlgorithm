from geneticAlgorithm.genotype.abstractGenotype import Genotype


class Operation:
    def singlePointCrossover(self,genotype1:Genotype,genotype2:Genotype):
        raise NotImplementedError("The method not implemented")

    def mutation(self,genotype:Genotype):
        raise NotImplementedError("The method not implemented")
