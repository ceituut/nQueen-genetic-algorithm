import random
import abc
class ParentSelection(abc.ABC) :
    # Initialization
    def __init__(self,selectionRate) :
        self.selectionRate = selectionRate
        self.selectedList = []
        self.source = None

    # Selects parents according to rate of selection
    @abc.abstractmethod
    def Select(self) :
        pass


class Rouletwheel(ParentSelection) :
    # Sets probability of selection according to rank of individual
    def LinearRanking(self,rank,populationSize) :
        S = 2
        N = populationSize
        probability = float()
        probability = 2 * rank * (S-1)
        probability /= (N * (N-1)) 
        probability += ((2-S)/N)
        return probability

    # Gets portion for each individual
    def GetPortions(self,populationSize) :
        allPortions = []
        portion = 0
        endOfPortion = 0
        for thisPerson in range(populationSize) :
            portion = self.LinearRanking(thisPerson,populationSize)
            allPortions.append( endOfPortion + portion )
            endOfPortion = allPortions[thisPerson]
        return allPortions

    # Rouletwheel parent selection according to portions 
    def Select(self) :
        populationSize = len(self.source.generation)
        selectionSize = int(self.selectionRate * populationSize)
        personPortionList = self.GetPortions(populationSize)
        for index in range(selectionSize) :
            randomValue = random.random()
            for thisPerson in range(populationSize) :
                if randomValue <= personPortionList[thisPerson] :
                    self.selectedList.append( self.source.generation[thisPerson] )
                    break
        return self.selectedList

