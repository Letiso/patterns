from abc import ABC, abstractmethod
from typing import List


class Context:
    def __init__(self, strategy: 'Strategy') -> None:
        self._strategy: Strategy = strategy

    @property
    def strategy(self) -> 'Strategy':
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: 'Strategy') -> None:
        self._strategy = strategy

    def sort(self) -> None:
        print(f"Sorting a list of letters using {self._strategy.__class__.__name__}")
        result = self._strategy.sorting(["a", "b", "c", "d", "e"])
        print('Result: ' + ''.join(result))


class Strategy(ABC):
    @abstractmethod
    def sorting(self, data: List) -> list: pass


class ClassicSorting(Strategy):
    def sorting(self, data: List) -> list:
        return sorted(data)


class ReversedSorting(Strategy):
    def sorting(self, data: List) -> reversed:
        return reversed(sorted(data))


if __name__ == '__main__':
    def client_code() -> None:
        strategies = {strategy.__name__: strategy() for strategy in Strategy.__subclasses__()}

        print('\bSetting "ClassicSorting" strategy for context...')
        context = Context(strategies['ClassicSorting'])
        context.sort()

        print('\nSetting "ClassicSorting" strategy for context...')
        context.strategy = strategies['ReversedSorting']
        context.sort()

    client_code()
