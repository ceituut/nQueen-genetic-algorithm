import random
import copy
import abc



class Recombination(abc.ABC) :
    # Initialization
    def __init__(self,recombinationRate) :
        self.recombinationRate = recombinationRate

    # Checks if can be recombinate according to rate of recombination
    @abc.abstractmethod
    def CanRecombinate(self) :
        pass

    # Runs recombination according to rate and type
    @abc.abstractmethod
    def RunRecombination(self,chromosome1,chromosome2) :
        pass



class RandomPointCrossOver(Recombination) :
    def CanRecombinate(self) :
        randomValue = random.random()
        if randomValue < self.recombinationRate :
            return True
        else :
            return False

    # 1 point crossover avoiding duplicated gens (random point)
    def RunRecombination(self,chromosome1,chromosome2) :
        if self.CanRecombinate() :
            length = len(chromosome1.gensList)
            startIndex = 0
            targetIndex = random.randrange(1,length)
            tempChromosome = copy.deepcopy(chromosome1)
            CopyRemainUnique(chromosome1,chromosome2,startIndex,targetIndex,length)
            CopyRemainUnique(chromosome2,tempChromosome,startIndex,targetIndex,length)



class HalfPointCrossOver(Recombination) :
    def CanRecombinate(self) :
        randomValue = random.random()
        if randomValue < self.recombinationRate :
            return True
        else :
            return False

    # 1 point crossover avoiding duplicated gens (half point)
    def RunRecombination(self,chromosome1,chromosome2) :
        if self.CanRecombinate() :
            length = len(chromosome1.gensList)
            startIndex = 0
            targetIndex = int(length/2)
            tempChromosome = copy.deepcopy(chromosome1)
            CopyRemainUnique(chromosome1,chromosome2,startIndex,targetIndex,length)
            CopyRemainUnique(chromosome2,tempChromosome,startIndex,targetIndex,length)



class OrderOneCrossOver(Recombination) :
    def CanRecombinate(self) :
        randomValue = random.random()
        if randomValue < self.recombinationRate :
            return True
        else :
            return False

    # 1 point crossover avoiding duplicated gens (half point)
    def RunRecombination(self,chromosome1,chromosome2) :
        if self.CanRecombinate() :
            length = len(chromosome1.gensList)
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
            CopyRemainUnique(chromosome1,chromosome2,startIndex,targetIndex,length)
            CopyRemainUnique(chromosome2,tempChromosome,startIndex,targetIndex,length)



# Functions
# Copies remain part of origin chromosome to destination chromosome avoiding duplicated gens.
def CopyRemainUnique(destination,origin,startIndex,targetIndex,length) :
    destinationConstantPart = CopySection(destination,startIndex,targetIndex)
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
# Copies a section of list from start index until limit
def CopySection(chromosome,start,limit) :
    copied = []
    for index in range(start,limit) :
        copied.append(chromosome.gensList[index])
    return copied
