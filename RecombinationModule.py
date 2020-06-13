import random
import copy
from ChromosomeModule import Chromosome

class Recombination :
    # Initialization
    def __init__(self,typeOfCrossover,crossoverRate) :
        self.crossoverRate = crossoverRate
        self.typeOfCrossover = typeOfCrossover

    # Checks if can be recombinate 
    # according to rate of recombination
    def canRecombinate(self) :
        randomValue = random.random()
        if randomValue < self.crossoverRate :
            return True
        else :
            return False

    # Runs recombination according to rate and type
    def RunRecombination(self,chromosome1,chromosome2) :
        children = []
        length = Chromosome.length
        parent1 = copy.deepcopy(chromosome1)
        parent2 = copy.deepcopy(chromosome2)
        if self.canRecombinate :
            if self.typeOfCrossover == 1 :
                children = self.Crossover1(parent1,parent2,length)
            elif self.typeOfCrossover == 2 :
                children = self.Crossover2(parent1,parent2,length)
            elif self.typeOfCrossover == 3 :
                children = self.Crossover3(parent1,parent2,length)
        else :
            children = list( (parent1,parent2) )
        return children

    # 1 point crossover avoiding duplicated gens (random point)
    def Crossover1(self,chromosome1,chromosome2,length) :
        startIndex = 0
        targetIndex = random.randrange(1,length)
        tempChromosome = copy.deepcopy(chromosome1)
        child1 = self.CopyRemainUnique(chromosome1,chromosome2,startIndex,targetIndex,length)
        child2 = self.CopyRemainUnique(chromosome2,tempChromosome,startIndex,targetIndex,length)
        return list( (child1,child2) )

    # 1 point crossover avoiding duplicated gens (half point)
    def Crossover2(self,chromosome1,chromosome2,length) :
        startIndex = 0
        targetIndex = int(length/2)
        tempChromosome = copy.deepcopy(chromosome1)
        child1 = self.CopyRemainUnique(chromosome1,chromosome2,startIndex,targetIndex,length)
        child2 = self.CopyRemainUnique(chromosome2,tempChromosome,startIndex,targetIndex,length)
        return list( (child1,child2) )

    # order 1 crossover
    def Crossover3(self,chromosome1,chromosome2,length) :
        firstRandomIndex = random.randrange(0,length)
        secondRandomIndex = random.randrange(0,length)
        while True :
            if firstRandomIndex != secondRandomIndex :
                break
            else :
                secondRandomIndex = random.randrange(0,length)
        if firstRandomIndex > secondRandomIndex :
            tempIndex = firstRandomIndex
            firstRandomIndex = secondRandomIndex
            secondRandomIndex = tempIndex
        startIndex = firstRandomIndex
        targetIndex = secondRandomIndex
        tempChromosome = copy.deepcopy(chromosome1)
        child1 = self.CopyRemainUnique(chromosome1,chromosome2,startIndex,targetIndex,length)
        child2 = self.CopyRemainUnique(chromosome2,tempChromosome,startIndex,targetIndex,length)
        return list( (child1,child2) )
            
    # Copies remain part of origin chromosome to destination chromosome avoiding duplicated gens.
    def CopyRemainUnique(self,destination,origin,startIndex,targetIndex,length) :
        destinationConstantPart = self.CopySection(destination,startIndex,targetIndex)
        originIndex = targetIndex
        destinationIndex = targetIndex
        while destinationIndex != startIndex :
            if origin.gensList[originIndex] not in destinationConstantPart :
                destination.gensList[destinationIndex] = origin.gensList[originIndex]
                destinationIndex += 1
            originIndex += 1
            if originIndex == length :
                originIndex = 0
            if destinationIndex == length :
                destinationIndex = 0
        return destination

    # Copies a section of list from start index until limit
    def CopySection(self,chromosome,start,limit) :
        copied = []
        for index in range(start,limit) :
            copied.append(chromosome.gensList[index])
        return copied
