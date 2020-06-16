import random
from ParentSelectionModule import ParentSelection

class Rouletwheel(ParentSelection) :
    # Sets probability of selection according to rank of individual
    def LinearRanking(self,rank) :
        S = 2
        N = Generation.populationSize
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
            portion = self.LinearRanking(thisPerson)
            allPortions.append( endOfPortion + portion )
            endOfPortion = allPortions[thisPerson]
        return allPortions

    # Rouletwheel parent selection according to portions 
    def Select(self) :
        selectionSize = int(self.selectionRate * Generation.populationSize)
        personPortionList = self.GetPortions(Generation.populationSize)
        for index in range(selectionSize) :
            randomValue = random.random()
            for thisPerson in range(Generation.populationSize) :
                if randomValue <= personPortionList[thisPerson] :
                    self.selectedList.append( self.generation[thisPerson] )
                    break
