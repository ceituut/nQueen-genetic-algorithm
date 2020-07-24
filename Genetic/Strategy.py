from .Chromosome import Chromosome
from .Generation import Generation
from .Report import Report

class Strategy :
    # problem states 
    chromosomeSize = int(0)
    populationSize = int(0)
    generatingLimit = int(0)

    # constructor 
    def __init__(self,parentSelector,recombinator,mutator) :
        self.name = None
        self.description = None
        self.mutator = mutator
        self.recombinator = recombinator
        Chromosome.length = Strategy.chromosomeSize
        Generation.populationSize = Strategy.populationSize
        self.currentGeneration = Generation()
        self.parentSelector = parentSelector
        parentSelector.source = self.currentGeneration
        self.reportObject = Report(Strategy.generatingLimit)

    # Genetic Algorithm termination check 
    def IsTerminated(self) :
        if self.currentGeneration.GoalTest() or self.currentGeneration.numberOfGeneration == ( Strategy.generatingLimit - 1 ) :
            return True
        else :
            return False

    # deletes Generation and make new Generation
    def ClearGeneration(self) :
        del self.currentGeneration
        self.currentGeneration = Generation()

    # Genetic Algorithm method
    def RunGeneticAlgorithm(self) :
        self.currentGeneration.Initialization()
        self.currentGeneration.EvaluateGeneration()
        self.reportObject.AppendReport(self.currentGeneration)
        while self.IsTerminated() != True :
            self.currentGeneration.SelectParent(self.parentSelector)
            self.currentGeneration.RecombinateParents(self.recombinator)
            self.currentGeneration.MutateOffsprings(self.mutator)
            self.currentGeneration.SurvivorSelection(self.parentSelector.selectionRate)
            self.currentGeneration.EvaluateGeneration()
            self.reportObject.AppendReport(self.currentGeneration)
