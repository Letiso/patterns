from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @abstractmethod
    def accept(self, visitor: 'Visitor') -> None: pass


class FirstComponent(Component):
    def accept(self, visitor: 'Visitor') -> None:
        visitor.visit_first_component(self)

    def special_first_component_logic(self) -> str:
        print(f"{self.__class__.__name__}: Doing special logic...")

        return 'A'


class SecondComponent(Component):
    def accept(self, visitor: 'Visitor') -> None:
        visitor.visit_second_component(self)

    def exclusive_second_component_logic(self) -> str:
        print(f"{self.__class__.__name__}: Doing special logic...")

        return 'B'


class Visitor:
    @abstractmethod
    def visit_first_component(self, component: FirstComponent) -> None: pass

    @abstractmethod
    def visit_second_component(self, component: SecondComponent) -> None: pass


class FirstVisitor(Visitor):
    def visit_first_component(self, component: FirstComponent) -> None:
        print(f"{component.special_first_component_logic()} + FirstVisitor additional logic")

    def visit_second_component(self, component: SecondComponent) -> None:
        print(f"{component.exclusive_second_component_logic()} + FirstVisitor additional logic\n")


class SecondVisitor(Visitor):
    def visit_first_component(self, component: FirstComponent) -> None:
        print(f"{component.special_first_component_logic()} + SecondVisitor additional logic")

    def visit_second_component(self, component: SecondComponent) -> None:
        print(f"{component.exclusive_second_component_logic()} + SecondVisitor additional logic\n")


def client_code(components: List[Component], visitor: Visitor) -> None:
    for component in components:
        component.accept(visitor)


if __name__ == '__main__':
    componentsList = [component() for component in Component.__subclasses__()]

    for string, concrete_visitor in zip(
            ("The client code works with all visitors via the base Visitor interface:",
             "It allows the same client code to work with different types of visitors:"),
            Visitor.__subclasses__()):

        print(f"{'—' * 70}\n{string}\n")
        client_code(componentsList, concrete_visitor())
