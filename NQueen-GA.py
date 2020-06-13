import random
import copy
import matplotlib.pyplot as plt
from StrategyModule import Strategy
from ReportModule import Report

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
    report.WriteReport(strategy.name)
    PlotOnDiagram(strategy)
    del strategy   

# Plots results of each strategy on diagram 
def PlotOnDiagram(strategy) :
    generation = range(0,Strategy.generatingLimit)
    bestFitness = strategy.reportObject.totalBestList 
    plt.plot(generation, bestFitness, label = strategy.name)   



# Get initial inputs
    # Get number of Queens
print("Enter number of Queens : ")
Strategy.numberOfQueens = int(input())
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



# Run Genetic Algorithm according to strategy
    # Run GA for Strategy1
Strategy1 = Strategy("Strategy1",0.9 , 0.98 , 1 , 1)
RunStrategy(Strategy1,numberOfRuns)

    # Run GA for Strategy2
Strategy2 = Strategy("Strategy2",0.9 , 0.98 , 1 , 2)
RunStrategy(Strategy2,numberOfRuns)

    # Run GA for Strategy3
Strategy3 = Strategy("Strategy3",0.90 , 0.98 , 1 , 3)
RunStrategy(Strategy3,numberOfRuns)

    # Run GA for Strategy4
Strategy4 = Strategy("Strategy4",0.9 , 0.98 , 2 , 1)
RunStrategy(Strategy4,numberOfRuns)

    # Run GA for Strategy5
Strategy5 = Strategy("Strategy5",0.9 , 0.98 , 2 , 2)
RunStrategy(Strategy5,numberOfRuns)

    # Run GA for Strategy6
Strategy6 = Strategy("Strategy6",0.9 , 0.98 , 2 , 3)
RunStrategy(Strategy6,numberOfRuns)

    # Run GA for Strategy7
Strategy7 = Strategy("Strategy7",0.9 , 0.98 , 3 , 1)
RunStrategy(Strategy7,numberOfRuns)

    # Run GA for Strategy8
Strategy8 = Strategy("Strategy8",0.9 , 0.98 , 3 , 2)
RunStrategy(Strategy8,numberOfRuns)

    # Run GA for Strategy9
Strategy9 = Strategy("Strategy9",0.9 , 0.98 , 3 , 3)
RunStrategy(Strategy9,numberOfRuns)



# Results
    # Save excell file
Report.SaveExcellFile()
    # Show diagram
plt.xlabel('Generation') 
plt.ylabel('Best Fitness') 
plt.title('NQueen-GA') 
plt.legend() 
plt.show() 
