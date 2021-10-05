from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operation1()
        self.first_hook()
        self.base_operation2()
        self.required_operation2()
        self.second_hook()

    def base_operation1(self) -> None:
        print(f'{self.name()}: base_operation1 implemented')

    def base_operation2(self) -> None:
        print(f'{self.name()}: base_operation2 implemented')

    @abstractmethod
    def required_operation1(self) -> None: pass

    @abstractmethod
    def required_operation2(self) -> None: pass

    def first_hook(self) -> None: pass

    def second_hook(self) -> None: pass

    def name(self) -> str:
        return self.__class__.__name__


class FirstImplementation(AbstractClass):
    def required_operation1(self) -> None:
        print(f'{self.name()}: required_operation1 implemented')

    def required_operation2(self) -> None:
        print(f'{self.name()}: required_operation2 implemented')


class SecondImplementation(AbstractClass):
    def required_operation1(self) -> None:
        print(f'{self.name()}: required_operation1 implemented')

    def required_operation2(self) -> None:
        print(f'{self.name()}: required_operation2 implemented')

    def first_hook(self) -> None:
        print(f'{self.name()}: first_hook implemented')


class ThirdImplementation(AbstractClass):
    def base_operation1(self) -> None:
        print(f'{self.name()}: base_operation1 implemented by specific way')

    def required_operation1(self) -> None:
        print(f'{self.name()}: required_operation1 implemented')

    def required_operation2(self) -> None:
        print(f'{self.name()}: required_operation2 implemented')


def client_code(concrete: AbstractClass) -> None:
    concrete.template_method()


if __name__ == '__main__':
    print(f'Same client code can work with different subclasses:\n{"—" * 50}')
    for name, concrete_class in {concrete_class.__name__: concrete_class()
                                 for concrete_class in AbstractClass.__subclasses__()}.items():
        print(f'Current subclass: {name}\n')
        client_code(concrete_class)
        print("—" * 50)
