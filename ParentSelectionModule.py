import abc
from RouletWheel import Rouletwheel
class ParentSelection(abc.ABC) :
    # Initialization
    def __init__(self,selectionRate) :
        self.selectionRate = selectionRate

    # Selects parents according to rate of selection
    @abc.abstractmethod
    def Select(self) :
        pass


