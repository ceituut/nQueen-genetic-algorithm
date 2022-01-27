# NQueen-Genetic Algorithm  
NQueen problem with Genetic Algorithm

![NQueen Image](NQueenImage.jpg)

## The Goal  
This project aim is to test different strategies for NQueen problem and compare them according to their charts for specified problem. _for example 20Queen_  
Results can be plot on diagram and can be store on excell file for manually insert chart.   
_-Common man it's just a NQueen problem solver !_    
No ! This is not only a simple NQueen problem with Genetic Algorithm. 
* __Define your own strategy and test it for NQueen problem.__
* __Change problem and test different strategies on it.__ 

## Before Usage 
I used XlsxWriter module in this project.  
[XlsxWriter](https://xlsxwriter.readthedocs.io) is a Python module that can be used to write text, numbers, formulas and hyperlinks to multiple worksheets in an Excel 2007+ XLSX file.
Please install it by this command :   
```bash
pip install XlsxWriter
``` 

## Usage
Steps to test your own strategy :
1. Create your own operation class
2. Create operation objects
3. Create your own strategy and pass your operation objects as parameters
4. Run strategy and test it

### 🔷🔷 How can i create my own operations ?
in [Operations](/Operations/) directory :
* __Create Parent Selection Operation :__ You are able to create your own parent selection class inside [ParentSelection.py](/Operations/ParentSelection.py). Your class should inherit form ParentSelection class and implement select() method.  
```python
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

# Your parent selection class 
class MyParentSelection(ParentSelection) :
    def select(self) :
        pass
```

* __Create Recombination Operation :__ You are able to create your own Recombination class inside [Recombination.py](/Operations/Recombination.py). Your class should inherit form Recombination class and implement CanRecombinate() and RunRecombination() methodes.
```python
class Recombination(abc.ABC) :
    # Initialization
    def __init__(self,recombinationRate) :
        self.recombinationRate = recombinationRate

    # Checks if can be recombinate according to rate of recombination
    @abc.abstractmethod
    def CanRecombinate(self) :
        pass

    # Runs recombination according to rate and type
    @abc.abstractmethod
    def RunRecombination(self,chromosome1,chromosome2) :
        pass

# Your recombination class
class MyRecombination(Recombination) :
    def CanRecombinate(self) :
        pass

    def RunRecombination(self,chromosome1,chromosome2) :
        pass
```

* __Create Mutation Operation :__ You are able to create your own Mutaion class inside [Mutation.py](/Operations/Mutation.py).Your class should inherit form Mutation class and implement CanMutate() and RunMutation() methodes.
```python
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

# Your mutation class 
class MyMutation(Mutation) :

    def CanMutate(self) :
        pass

    def RunMutation(self,chromosome) :
        pass
```

### 🔷🔷 How can i define my own strategy ?
After creating operations , inside [main.py](/main.py) make object from your operation class just like example. 
* __Create your parent selection object :__ 
```python
myParentSelectionObject = ParentSelection.MyParentSelection()  
# for example
RouletWheelSelector = ParentSelection.Rouletwheel(0.6)  
```  

* __Create your recombination object :__
```python
myRecombinationObject = Recombination.MyRecombination()  
# for example
randomPointCrossOver = Recombination.RandomPointCrossOver(0.98)
```

* __Create your mutation object :__
```python
myMutationObject = Mutation.MyMutation()
# for example
swapMutation = Mutation.Swap(0.9)
```
Finally , create your own strategy like this and pass related parameters :  
```python
myStrategyObject = Strategy(MyParentSelectionObject,MyRecombinationObject,MyMutationObject)
myStrategyObject.name = "my strategy name"
myStrategyObject.description = "my strategy description"
RunStrategy(myStrategyObject,numberOfRuns)
``` 
```python
# for example
Strategy1 = Strategy(RouletWheelSelector,randomPointCrossOver,swapMutation)
Strategy1.name = "Strategy1"
Strategy1.description = "RouletWheelSelector,randomPointCrossOver,swapMutation"
RunStrategy(Strategy1,numberOfRuns)
```
__Attention :__ let numberOfRuns parameter have its own value and dont pass a number; because all strategies will test with same number of runs. 
 
### 🔷🔷 How can i change problem ?
You are able to change chromosome class and test your own permutation problem without any headache.  
__Just Create your own Chromosome :__ You should have this properties and methodes inside your own Chromosome class in [Genetic](/Genetic/) directory :
```python
class Chromosome :
    # Your length of Chromosome 
    length = int()

    # Initialization
    def __init__(self) :
        self.gensList = []
        self.collisions = int()
        self.fitness = float()
        self.AssignRandomGens()

    # Assigns unique random value for each gen
    def AssignRandomGens(self) :
        pass
    
    # Evaluates fitenss
    def EvaluateFitness(self) :
        pass
    
    # It converts Genotype to Phenotype /////////////////
    # To use it for ShowBestChromosome() method in Report.py
    # and/or to use for fitness calculations
    def GenotypeToPhenoType(self) :
        pass

    # It can be used for showing phenotype 
    def ShowPhenotype(self) :
        pass
```
 
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.  

## Thanks
  Unlimited thanks to God   
  Special thanks to my master [Dr. Siamak Sarmady](https://sarmady.com/siamak/)   
  hope you enjoy 🤗🌹  

>:blossom:Imam Mahdi(As) declared :
> we are aware of all your news 
> and none of your actions is hidden from us.
