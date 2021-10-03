from abc import ABC, abstractmethod

from datetime import datetime
from random import sample
from string import ascii_letters as letters, digits


class Originator:
    def __init__(self, state: str) -> None:
        self._state: str = state
        self._caretaker: Caretaker = Caretaker(self)

        print(f"Originator's original state is:\n{self._state}\n{'_' * 30}")

    @property
    def caretaker(self) -> 'Caretaker':
        return self._caretaker

    @staticmethod
    def generate_new_condition(length: int) -> str:
        return "".join(sample(letters + digits, length))

    def important_action(self) -> None:
        self._caretaker.backup()

        print('\nOriginator doing an important action... ')
        self._state = self.generate_new_condition(30)
        print(f"And it's condition was changed:\n{self._state}\n{'_' * 30}")

    def save_condition(self) -> 'Memento':
        print('Making a memento...')
        return ConcreteMemento(self._state)

    def undo(self) -> None:
        print('Restoring from memento...')
        self._state = self._caretaker.undo()
        print(f'And condition now is:\n{self._state}')


class Memento(ABC):
    @abstractmethod
    def get_state(self) -> str: pass

    @abstractmethod
    def get_metadata(self) -> str: pass


class ConcreteMemento(Memento):
    def __init__(self, state: str):
        self._state: str = state
        self._date: str = str(datetime.now())[:19]

    def get_state(self) -> str:
        return self._state

    def get_metadata(self) -> str:
        return f"{self._date} \\ {self._state[:8]}"


class Caretaker:
    def __init__(self, originator):
        self._history: list = []
        self._originator: Originator = originator

    def backup(self) -> None:
        print("Making Originator's state backup...")
        self._history.append(self._originator.save_condition())

    def undo(self) -> str or None:
        if not len(self._history): return

        print("Restoring Originator's state from backup...")
        return self._history.pop().get_state()

    def show_history(self) -> None:
        print('Current history stack:')
        for memento in self._history:
            print(memento.get_metadata())
        print('_' * 30)


if __name__ == "__main__":
    originator_instance: Originator = Originator('Initial state')

    def client_code(originator: Originator) -> None:

        originator.important_action()

        originator.important_action()

        originator.important_action()

        originator.caretaker.show_history()

        print(f"\nLet's undo!")
        originator.undo()

        print("\nAnd do it again!")
        originator.undo()

        print("\nAnd again!")
        originator.undo()

    client_code(originator_instance)
