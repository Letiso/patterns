from abc import ABC, abstractmethod
from copy import copy, deepcopy


class Prototype(ABC):
    @abstractmethod
    def __copy__(self): pass

    @abstractmethod
    def __deepcopy__(self): pass


