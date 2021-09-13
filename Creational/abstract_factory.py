from abc import ABC, abstractmethod
from platform import platform

# Products


class StartButton(ABC):
    @abstractmethod
    def start_action(self): pass


class StartButtonWindows(StartButton):
    def start_action(self):
        print('Action was started at Windows OS.', end='\n')


class StartButtonLinux(StartButton):
    def start_action(self):
        print('Action was started at Linux OS.', end='\n')


class StopButton(ABC):
    @abstractmethod
    def stop_action(self): pass


class StopButtonWindows(StopButton):
    def stop_action(self):
        print('Action was stopped at Windows OS.', end='\n')


class StopButtonLinux(StopButton):
    def stop_action(self):
        print('Action was stopped at Linux OS.', end='\n')

# Factories


class ButtonsFactory(ABC):
    @abstractmethod
    def create_start_button(self): pass

    def create_stop_button(self): pass


class WindowsButtonsFactory(ButtonsFactory):
    def create_start_button(self) -> StartButtonWindows:
        return StartButtonWindows()

    def create_stop_button(self) -> StopButtonWindows:
        return StopButtonWindows()


class LinuxButtonsFactory(ButtonsFactory):
    def create_start_button(self) -> StartButtonLinux:
        return StartButtonLinux()

    def create_stop_button(self) -> StopButtonLinux:
        return StopButtonLinux()


def buttons_factory_dict(func):
    # current_os = platform()[:platform().index('-')]
    current_os = 'Linux'

    os_factories = dict(
        [(buttons_factory.__name__[:buttons_factory.__name__.index('Buttons')], buttons_factory)
         for buttons_factory in ButtonsFactory.__subclasses__()]
    )
    print(os_factories, end='\n\n')

    def wrapper():
        return func(factory := os_factories[current_os]())

    return wrapper


@buttons_factory_dict
def gui_init(factory: ButtonsFactory):
    print(f'App is using {factory.__class__.__name__} for buttons creating.')

    start_button = factory.create_start_button()
    stop_button = factory.create_stop_button()

    start_button.start_action()
    stop_button.stop_action()


if __name__ == '__main__':
    gui_init()
