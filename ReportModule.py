import xlsxwriter
from ChromosomeModule import Chromosome

class Report :
    workbook = None
    workSheet = None
    numberOfReport = int(-1)

    # Initialization
    def __init__(self,generatingLimit) :
        self.generatingLimit = generatingLimit
        self.currentBestList = []
        self.currentAverageList = []
        self.totalBestList = [0 for columnIndex in range(self.generatingLimit)]
        self.totalAverageList = [0 for columnIndex in range(self.generatingLimit)]
        self.bestChromosome = None
    
    # Creates Excell file and adds worksheet to it
    def CreateExcellFile(excellFileName) :
        excellFileName += '.xlsx'
        Report.workbook = xlsxwriter.Workbook(excellFileName)
        Report.workSheet = Report.workbook.add_worksheet()

    # Writes Data of related strategy to created excell file
    def WriteToExcell(self,strategyName,dataList) :
        self.WriteStrategyName(strategyName)
        rowIndex = Report.numberOfReport
        columnIndex = 1
        for data in dataList :
            Report.workSheet.write(rowIndex,columnIndex,data)
            columnIndex += 1

    # Writes strategy name in proper row and column
    def WriteStrategyName(self,strategyName) :
        rowIndex = Report.numberOfReport
        columnIndex = 0
        Report.workSheet.write(rowIndex,columnIndex,strategyName)

    # Saves excell file and closes it
    def SaveExcellFile() :
        Report.workbook.close()
    
    # Append statistics of current generation 
    def AppendReport(self,thisGeneration) :
        self.currentBestList.append(thisGeneration.bestFitness)
        self.currentAverageList.append(thisGeneration.averageFitness)
        self.bestChromosome = thisGeneration.bestChromosome

    # Sums statistics of all generations in a round of run
    def SumReports(self) :
        totalLength = self.generatingLimit
        currentLength = len(self.currentBestList)
        self.FillList(self.currentBestList)
        self.FillList(self.currentAverageList)
        for columnIndex in range(totalLength) :
            self.totalBestList[columnIndex] += self.currentBestList[columnIndex]
            self.totalAverageList[columnIndex] += self.currentAverageList[columnIndex]
        self.ClearReport()

    # Calculates average statistics of all rounds
    def AverageReports(self,numberOfRuns) :
        size = self.generatingLimit
        for columnIndex in range(size) :
            self.totalBestList[columnIndex] /= numberOfRuns
            self.totalAverageList[columnIndex] /= numberOfRuns

    # Write reports to excell file and shows some result
    def WriteReport(self,strategy) :
        self.ShowBestChromosome()
        print(strategy.name)
        print(strategy.description)
        print("Best Fitness List of all generations : ")
        print(self.totalBestList)
        print("")
        print("")
        # print("Average Fitness List of all generations : ")
        # print(self.totalAverageList)
        Report.numberOfReport += 1
        self.WriteToExcell(strategy.name,self.totalBestList)
    
    # Fills a list with it's final value
    def FillList(self,List) :
        fillingNumber = List[-1]
        startIndex = len(List)
        totalLength = self.generatingLimit
        self.AdjustSizeOfList(List,totalLength)
        for columnIndex in range(startIndex,totalLength) :
            List[columnIndex] = fillingNumber

    # Adjust size of list to expectes length
    def AdjustSizeOfList(self,List,ExpectedLength) :
        listLength = len(List)
        if listLength < ExpectedLength :
            for columnIndex in range(listLength,ExpectedLength) :
                List.append(0)

    # Shows best chromosome that has been found
    def ShowBestChromosome(self) :
        self.bestChromosome.GenotypeToPhenoType()
        for rowIndex in range(Chromosome.length) :
            for colIndex in range(Chromosome.length) :
                if Chromosome.tempChessBoard[rowIndex][colIndex] :
                    print("Q " , end="")
                else :
                    print("# " , end="")
            print("  ")

    # Clears temporary report of current round
    def ClearReport(self) :
        self.currentBestList.clear()
        self.currentAverageList.clear()


