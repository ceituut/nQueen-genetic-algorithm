import random
import abc

class Mutation(abc.ABC) :
    # Initialization
    def __init__(self,mutationRate) :
        self.mutationRate = mutationRate

    # Checks if can be mutate according to rate of mutation
    @abc.abstractmethod
    def CanMutate(self) :
        pass

    @abc.abstractmethod
    # Runs mutation 
    def RunMutation(self,chromosome) :
        pass



class Swap(Mutation) :
    def CanMutate(self) :
        randomValue = random.random()
        if randomValue < self.mutationRate :
            return True
        else :
            return False

    def RunMutation(self,chromosome) :
        if self.CanMutate() :
            length = len(chromosome.gensList)
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



class Insert(Mutation) :
    def CanMutate(self) :
        randomValue = random.random()
        if randomValue < self.mutationRate :
            return True
        else :
            return False

    def RunMutation(self,chromosome) :
        if self.CanMutate() :
            length = len(chromosome.gensList)
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



class Inversion(Mutation) :
    def CanMutate(self) :
        randomValue = random.random()
        if randomValue < self.mutationRate :
            return True
        else :
            return False

    def RunMutation(self,chromosome) :
        if self.CanMutate() :
            length = len(chromosome.gensList)
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


