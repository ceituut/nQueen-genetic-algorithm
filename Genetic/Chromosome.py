import random

class Chromosome :
    length = int()
    tempChessBoard = None

    # Initialization
    def __init__(self) :
        self.gensList = []
        self.collisions = int()
        self.fitness = float()
        self.AssignRandomGens()

    # Assigns unique random value for each gen
    def AssignRandomGens(self) :
        index = 0
        randomValue = int() 
        while index < Chromosome.length :
            randomValue = random.randrange(0,Chromosome.length)
            if randomValue not in self.gensList :
                self.gensList.append(randomValue)
                index += 1

    # This fitness function doesn't evaluate row collisions
    # because type of problem is permutation
    def EvaluateFitness(self) :
        self.collisions = 0
        self.fitness = 0
        self.GenotypeToPhenoType()
        self.collisions += self.DiagonalCollisions(Chromosome.tempChessBoard)
        if self.collisions <= 99 :
            self.fitness = ( 100 - self.collisions ) / 100
        else :
            self.fitness = 1 / self.collisions

    # Makes temporary Phenotype for fitness evaluation
    def GenotypeToPhenoType(self) :
        length = Chromosome.length
        rows = Chromosome.length
        cols = Chromosome.length
        Chromosome.tempChessBoard = [ [0 for i in range(cols)] for j in range(rows) ]
        for colIndex in range(length) :
            Chromosome.tempChessBoard[self.gensList[colIndex]][colIndex] = 1

    # Counts diagonal collisions 
    def DiagonalCollisions(self,ChessBoard) :
        length = Chromosome.length
        collisions = 0
        collisions += self.TopRightCollisions(ChessBoard,length)
        collisions += self.TopLeftCollisions(ChessBoard,length)
        return collisions

    # Counts diagonal collisions 
    # from top right direction of selected gen
    # to end of that diagonal path
    def TopRightCollisions(self,ChessBoard,length) :
        collisions = 0
        step = 1
        for colIndex in range(length) :
            rowIndex = self.gensList[colIndex]
            while True :
                if ( rowIndex - step >= 0 ) and ( colIndex + step < length )   :
                    collisions += ChessBoard[rowIndex - step][colIndex + step]
                    step += 1
                else :
                    step = 1
                    break
        return collisions

    # Counts diagonal collisions 
    # from top left direction of selected gen
    # to end of that diagonal path
    def TopLeftCollisions(self,ChessBoard,length) :
        collisions = 0
        step = 1
        for colIndex in range(length) :
            rowIndex = self.gensList[colIndex]
            while True :
                if ( rowIndex - step >= 0 ) and ( colIndex - step >= 0 )  :
                    collisions += ChessBoard[rowIndex - step][colIndex - step]
                    step += 1
                else :
                    step = 1
                    break
        return collisions

