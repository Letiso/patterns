from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self):
        self._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @abstractmethod
    def getResult(self): pass


class Leaf(Component):
    def getResult(self) -> str:
        return 'Leaf'


class Branch(Component):
    def __init__(self):
        super().__init__()
        self._children, self._result = list(), list()

    def addChild(self, child):
        self._children.append(child)
        child.parent = self

    def removeChild(self, child):
        self._children.remove(child)
        child.parent = None

    def getResult(self) -> str:
        for child in self._children:
            self._result.append(child.getResult())
        return f'Branch({" + ".join(self._result)})'


if __name__ == '__main__':
    leafOne = Leaf()
    leafTwo = Leaf()
    leafThree = Leaf()

    branchOne = Branch()
    branchTwo = Branch()

    branchOne.addChild(leafTwo)
    branchTwo.addChild(leafThree)
    branchOne.addChild(branchTwo)

    tree = Branch()
    tree.addChild(branchOne)
    tree.addChild(leafOne)

    print(f"{'_' * 70}\ntree structure : {tree.getResult()}\n", end=f"{'_' * 70}\n")
