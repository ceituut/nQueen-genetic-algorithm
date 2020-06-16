from ChromosomeModule import Chromosome
from GenerationModule import Generation
from ReportModule import Report

class Strategy :
    # problem states 
    numberOfQueens = int(0)
    populationSize = int(0)
    generatingLimit = int(0)

    # constructor 
    def __init__(self,strategyName,parentSelector,mutationRate,crossoverRate,typeOfCrossover,typeOfMutation) :
        self.name = strategyName
        self.parentSelector = parentSelector
        self.mutationRate = mutationRate
        self.crossoverRate = crossoverRate
        self.typeOfMutation = int(typeOfMutation)
        self.typeOfCrossover = int(typeOfCrossover)
        Chromosome.length = Strategy.numberOfQueens
        Generation.populationSize = Strategy.populationSize
        self.currentGeneration = Generation()
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
            self.currentGeneration.RecombinateParents(self.typeOfCrossover,self.crossoverRate)
            self.currentGeneration.MutateOffsprings(self.typeOfMutation,self.mutationRate)
            self.currentGeneration.SurvivorSelection(self.parentSelector.selectionRate)
            self.currentGeneration.EvaluateGeneration()
            self.reportObject.AppendReport(self.currentGeneration)
