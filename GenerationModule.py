import copy
from ChromosomeModule import Chromosome

class Generation :
    populationSize = int()

    # Initialization
    def __init__(self) :
        self.generation = []
        self.numberOfGeneration = int(0)
        self.bestChromosome = None
        self.bestFitness = float(0)
        self.totalFitness = float(0)
        self.averageFitness = float(0)
        self.selectedList = []

    # Makes Unique initial population
    def Initialization(self) :
        index = 0
        person = None
        self.generation.clear()
        while index < Generation.populationSize :
            person = Chromosome()
            if person not in self.generation :
                self.generation.append(person)
                index += 1

    # Evaluates each person in population
    def EvaluateGeneration(self) :
        self.totalFitness = 0
        self.bestFitness = 0
        for thisPerson in range(Generation.populationSize) :
            self.generation[thisPerson].EvaluateFitness()
            self.SumFitness(thisPerson)
            self.BestFitnessTest(thisPerson)
        self.averageFitness = self.totalFitness / Generation.populationSize

    # Adds fitness to total fitness
    def SumFitness(self,thisPerson) :
        self.totalFitness += self.generation[thisPerson].fitness

    # Checks best chromosome 
    def BestFitnessTest(self,thisPerson) :
        if self.bestFitness < self.generation[thisPerson].fitness :
            self.bestFitness = self.generation[thisPerson].fitness
            self.bestChromosome = copy.deepcopy(self.generation[thisPerson]) 

    # Checks if a person is goal 
    def GoalTest(self) :
        isGoal = False
        for thisPerson in range(Generation.populationSize) :
            if self.generation[thisPerson].fitness == 1 :
                isGoal = True
        return isGoal

    # Sorts generation based on fitness
    def SortGeneration(self) :
        self.generation.sort(key=lambda person: person.fitness)
                    
    # Selects parents according to strategy of selection
    def SelectParent(self,parentSelector) :
        self.SortGeneration()
        self.selectedList = parentSelector.Select()

    # Recombinates selected parents and adds them to offsprings
    def RecombinateParents(self,recombinator) :
        chromosome1 = None
        chromosome2 = None
        mateOfLast = None
        numberOfParents = len(self.selectedList)
        if numberOfParents % 2 != 0 :
            mateOfLast = copy.deepcopy(self.selectedList[numberOfParents-2])
        for index in range(0,numberOfParents,2) :
            if index < numberOfParents - 1 :
                chromosome1 = copy.deepcopy(self.selectedList[index]) 
                chromosome2 = copy.deepcopy(self.selectedList[index+1]) 
                recombinator.RunRecombination(chromosome1,chromosome2)
                self.selectedList[index] = chromosome1
                self.selectedList[index+1] = chromosome2
            elif index == numberOfParents - 1 :
                chromosome1 = mateOfLast 
                chromosome2 = copy.deepcopy(self.selectedList[index]) 
                recombinator.RunRecombination(chromosome1,chromosome2)

    # Mutates offsprings
    def MutateOffsprings(self,mutator) :
        offspringsSize = len(self.selectedList)
        for index in range(offspringsSize) :
            mutator.RunMutation(self.selectedList[index]) 
    
    # Replaces offsprings to generation
    def SurvivorSelection(self,transformRate) :
        targetIndex = int(transformRate * Generation.populationSize)
        self.numberOfGeneration += 1
        for index in range(targetIndex) :
            self.generation[index] = copy.deepcopy(self.selectedList[index]) 
        self.selectedList.clear()
  