from abc import ABC, abstractmethod
import copy


class NPCPrototype(ABC):
    _name = _race = _stats = _items_limit = _inventory = None

    @abstractmethod
    def clone(self): pass


class Warrior:
    def __init__(self):
        pass

    def clone(self):
        return copy.deepcopy(self)


class Archer:
    def __init__(self):
        pass

    def clone(self):
        return copy.deepcopy(self)


class Mage:
    def __init__(self):
        pass

    def clone(self):
        return copy.deepcopy(self)


class Healer:
    def __init__(self):
        pass

    def clone(self):
        return copy.deepcopy(self)


class NPCFactory: pass
