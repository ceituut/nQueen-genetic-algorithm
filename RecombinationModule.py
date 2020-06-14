import random
import copy
from ChromosomeModule import Chromosome

# Checks if can be recombinate 
# according to rate of recombination
def canRecombinate(crossoverRate) :
    randomValue = random.random()
    if randomValue < crossoverRate :
        return True
    else :
        return False

# Runs recombination according to rate and type
def RunRecombination(chromosome1,chromosome2,typeOfCrossover,crossoverRate) :
    length = Chromosome.length
    if canRecombinate(crossoverRate) :
        if typeOfCrossover == 1 :
            Crossover1(chromosome1,chromosome2,length)
        elif typeOfCrossover == 2 :
            Crossover2(chromosome1,chromosome2,length)
        elif typeOfCrossover == 3 :
            Crossover3(chromosome1,chromosome2,length)

# 1 point crossover avoiding duplicated gens (random point)
def Crossover1(chromosome1,chromosome2,length) :
    startIndex = 0
    targetIndex = random.randrange(1,length)
    tempChromosome = copy.deepcopy(chromosome1)
    CopyRemainUnique(chromosome1,chromosome2,startIndex,targetIndex,length)
    CopyRemainUnique(chromosome2,tempChromosome,startIndex,targetIndex,length)

# 1 point crossover avoiding duplicated gens (half point)
def Crossover2(chromosome1,chromosome2,length) :
    startIndex = 0
    targetIndex = int(length/2)
    tempChromosome = copy.deepcopy(chromosome1)
    CopyRemainUnique(chromosome1,chromosome2,startIndex,targetIndex,length)
    CopyRemainUnique(chromosome2,tempChromosome,startIndex,targetIndex,length)

# order 1 crossover
def Crossover3(chromosome1,chromosome2,length) :
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
