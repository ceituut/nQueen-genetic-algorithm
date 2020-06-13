import random
import copy
from ChromosomeModule import Chromosome
     
class Mutation :
    # Initialization
    def __init__(self,typeOfMutation,mutationRate) :
        self.mutationRate = mutationRate
        self.typeOfMutation = int(typeOfMutation)
    
    # Checks if can be mutate 
    # according to rate of mutation
    def canMutate(self) :
        randomValue = random.random()
        if randomValue < self.mutationRate :
            return True
        else :
            return False
    
    # Runs mutation according to rate and type
    def RunMutation(self,chromosome) :
        mutated = None
        length = Chromosome.length
        targetChromosome = copy.deepcopy(chromosome)
        if self.canMutate() :
            if self.typeOfMutation == 1 :
                mutated = self.Mutation1(targetChromosome,length)
            elif self.typeOfMutation == 2 :
                mutated = self.Mutation2(targetChromosome,length)
            elif self.typeOfMutation == 3 :
                mutated = self.Mutation3(targetChromosome,length)
        else :
            mutated = chromosome
        return mutated
    
    # Swap mutation
    def Mutation1(self,chromosome,length) :
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
        return chromosome

    # Insert mutation
    def Mutation2(self,chromosome,length) :
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
        return chromosome
    
    # Inversion mutation
    def Mutation3(self,chromosome,length) :
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
        return chromosome
