import random
from ChromosomeModule import Chromosome
     
# Checks if can be mutate 
# according to rate of mutation
def canMutate(mutationRate) :
    randomValue = random.random()
    if randomValue < mutationRate :
        return True
    else :
        return False

# Runs mutation according to rate and type
def RunMutation(chromosome,typeOfMutation,mutationRate) :
    length = Chromosome.length
    if canMutate(mutationRate) :
        if typeOfMutation == 1 :
            Mutation1(chromosome,length)
        elif typeOfMutation == 2 :
            Mutation2(chromosome,length)
        elif typeOfMutation == 3 :
            Mutation3(chromosome,length)

# Swap mutation
def Mutation1(chromosome,length) :
    firstRandomIndex = random.randrange(0,length)
    secondRandomIndex = random.randrange(0,length)
    while True :
        if firstRandomIndex != secondRandomIndex :
            break
        else :
            secondRandomIndex = random.randrange(0,length)
    temp = chromosome.gensList[firstRandomIndex]
    chromosome.gensList[firstRandomIndex] = chromosome.gensList[secondRandomIndex]
    chromosome.gensList[secondRandomIndex] = temp

# Insert mutation
def Mutation2(chromosome,length) :
    temp = []
    tempIndex = 0
    firstRandomIndex = random.randrange(0,length-1)
    secondRandomIndex = random.randrange(0,length)
    while True :
        if firstRandomIndex != secondRandomIndex :
            break
        else :
            secondRandomIndex = random.randrange(0,length)
    secondGen = chromosome.gensList[secondRandomIndex]
    for index in range(0,secondRandomIndex) :
        temp.append(chromosome.gensList[index])
    for index in range(secondRandomIndex + 1 , length) :
        temp.append(chromosome.gensList[index])
    for index in range(length) :
        if index == firstRandomIndex + 1 :
            chromosome.gensList[index] = secondGen
        else :
            chromosome.gensList[index] = temp[tempIndex]
            tempIndex += 1

# Inversion mutation
def Mutation3(chromosome,length) :
    temp = []
    tempIndex = None
    tempGen = None
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
    if firstRandomIndex + 1 == secondRandomIndex :
        tempGen = chromosome.gensList[firstRandomIndex]
        chromosome.gensList[firstRandomIndex] = chromosome.gensList[secondRandomIndex]
        chromosome.gensList[secondRandomIndex] = tempGen
    else :
        for index in range(firstRandomIndex,secondRandomIndex + 1) :
            temp.append(chromosome.gensList[index])
        tempIndex = len(temp) - 1
        for index in range(firstRandomIndex,secondRandomIndex + 1) :
            chromosome.gensList[index] = temp[tempIndex]
            tempIndex -= 1
