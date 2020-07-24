import random
import copy
from Genetic.Strategy import Strategy
from Genetic.Report import Report
from Operations import ParentSelection
from Operations import Mutation
from Operations import Recombination
import matplotlib.pyplot as ploter

# Runs each strategy a specific number of times
def RunStrategy(strategy,numberOfRuns) :
    seed = 100
    for index in range(numberOfRuns) :
        random.seed(seed)
        report = strategy.reportObject
        strategy.RunGeneticAlgorithm()
        strategy.ClearGeneration()
        report.SumReports()
        seed += 100 
    report.AverageReports(numberOfRuns)
    report.WriteReport(strategy)
    PlotOnDiagram(strategy)
    del strategy   

# Plots results of each strategy on diagram 
def PlotOnDiagram(strategy) :
    generation = range(0,Strategy.generatingLimit)
    bestFitness = strategy.reportObject.totalBestList 
    ploter.plot(generation, bestFitness, label = strategy.name)   



# Get initial inputs
    # Get number of Queens
print("Enter number of Queens : ")
Strategy.chromosomeSize = int(input())
    # Get population size
print("Enter population size : ")
Strategy.populationSize = int(input())
    # Get last generation number
print("Enter generating limit : ")
Strategy.generatingLimit = int(input())
    # Get number of runs 
print("Enter number of runs : ")
numberOfRuns = int(input())
    # Create excell file 
print("Enter excell file name : ")
excellFileName = str(input())
Report.CreateExcellFile(excellFileName)



# Creating parent selectors 
RouletWheelSelector = ParentSelection.Rouletwheel(0.6)



# Creating mutation makers 
swapMutation = Mutation.Swap(0.9)
insertMutation = Mutation.Insert(0.9)
inversionMutation = Mutation.Inversion(0.9)



# Creating recombination makers 
randomPointCrossOver = Recombination.RandomPointCrossOver(0.98)
halfPointCrossOver = Recombination.HalfPointCrossOver(0.98)
OrderOneCrossOver = Recombination.OrderOneCrossOver(0.98)



# Run Genetic Algorithm according to strategy
    # Run GA for Strategy1
Strategy1 = Strategy(RouletWheelSelector,randomPointCrossOver,swapMutation)
Strategy1.name = "Strategy1"
Strategy1.description = "RouletWheelSelector,randomPointCrossOver,swapMutation"
RunStrategy(Strategy1,numberOfRuns)

    # Run GA for Strategy2
Strategy2 = Strategy(RouletWheelSelector,randomPointCrossOver,insertMutation)
Strategy2.name = "Strategy2"
Strategy2.description = "RouletWheelSelector,randomPointCrossOver,insertMutation"
RunStrategy(Strategy2,numberOfRuns)

    # Run GA for Strategy3
Strategy3 = Strategy(RouletWheelSelector,randomPointCrossOver,inversionMutation)
Strategy3.name = "Strategy3"
Strategy3.description = "RouletWheelSelector,randomPointCrossOver,inversionMutation"
RunStrategy(Strategy3,numberOfRuns)

    # Run GA for Strategy4
Strategy4 = Strategy(RouletWheelSelector,halfPointCrossOver,swapMutation)
Strategy4.name = "Strategy4"
Strategy4.description = "RouletWheelSelector,halfPointCrossOver,swapMutation"
RunStrategy(Strategy4,numberOfRuns)

    # Run GA for Strategy5
Strategy5 = Strategy(RouletWheelSelector,halfPointCrossOver,insertMutation)
Strategy5.name = "Strategy5"
Strategy5.description = "RouletWheelSelector,halfPointCrossOver,insertMutation"
RunStrategy(Strategy5,numberOfRuns)

    # Run GA for Strategy6
Strategy6 = Strategy(RouletWheelSelector,halfPointCrossOver,inversionMutation)
Strategy6.name = "Strategy6"
Strategy6.description = "RouletWheelSelector,halfPointCrossOver,inversionMutation"
RunStrategy(Strategy6,numberOfRuns)

    # Run GA for Strategy7
Strategy7 = Strategy(RouletWheelSelector,OrderOneCrossOver,swapMutation)
Strategy7.name = "Strategy7"
Strategy7.description = "RouletWheelSelector,OrderOneCrossOver,swapMutation"
RunStrategy(Strategy7,numberOfRuns)

    # Run GA for Strategy8
Strategy8 = Strategy(RouletWheelSelector,OrderOneCrossOver,insertMutation)
Strategy8.name = "Strategy8"
Strategy8.description = "RouletWheelSelector,OrderOneCrossOver,insertMutation"
RunStrategy(Strategy8,numberOfRuns)

    # Run GA for Strategy9
Strategy9 = Strategy(RouletWheelSelector,OrderOneCrossOver,inversionMutation)
Strategy9.name = "Strategy9"
Strategy9.description = "RouletWheelSelector,OrderOneCrossOver,inversionMutation"
RunStrategy(Strategy9,numberOfRuns)



# Results
    # Save excell file
Report.SaveExcellFile()
    # Show diagram
ploter.xlabel('Generation') 
ploter.ylabel('Best Fitness') 
ploter.title('NQueen-GA') 
ploter.legend() 
ploter.show() 
