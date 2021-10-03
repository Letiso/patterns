from abc import ABC, abstractmethod


# Mediators interface
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: 'BaseComponent', event: str) -> None: pass


# Concrete mediators
class ConcreteMediator(Mediator):
    def __init__(self, first_component: 'FirstComponent', second_component: 'SecondComponent'):
        self._firstComponent: FirstComponent = first_component
        self._firstComponent.mediator = self

        self._secondComponent: SecondComponent = second_component
        self._secondComponent.mediator = self

        self._events: dict = {
            'A': (self._secondComponent.do_d,),
            'C': (self._firstComponent.do_b, self._secondComponent.do_d),
        }

    def notify(self, sender: 'BaseComponent', event: str) -> None:
        if event in self._events:
            print(f'\nMediator reacts on {event} action')
            for action in self._events[event]: action()
            print("_" * 10)


# Base component
class BaseComponent:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


# Concrete components
class FirstComponent(BaseComponent):
    def do_a(self) -> None:
        print('FirstComponent does A')
        self.mediator.notify(self, 'A')

    def do_b(self) -> None:
        print('FirstComponent does B')
        self.mediator.notify(self, 'B')


class SecondComponent(BaseComponent):
    def do_c(self) -> None:
        print('SecondComponent does C')
        self.mediator.notify(self, 'C')

    def do_d(self) -> None:
        print('SecondComponent does D')
        self.mediator.notify(self, 'D')


# Client code
if __name__ == '__main__':
    component1 = FirstComponent()
    component2 = SecondComponent()
    concrete_mediator = ConcreteMediator(component1, component2)


    def client_code() -> None:
        component1.do_a()
        component2.do_c()

    client_code()
