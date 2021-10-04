from abc import ABC, abstractmethod


class Context:
    _state = None

    def __init__(self, states: dict) -> None:
        self.switch_state(states['FirstState'])
        self._states: dict = states

        for concrete_state in states.values():
            concrete_state.context = self

    @property
    def states(self) -> dict:
        return self._states

    @states.setter
    def states(self, states: dict) -> None:
        self._states = states

    def switch_state(self, state: 'State') -> None:
        print(f'\nContext: switching a state\nfrom {self._state}\nto {state}...\n')
        self._state = state

    def first_request(self) -> None:
        self._state.first_handler()

    def second_request(self) -> None:
        self._state.second_handler()


class State(ABC):
    _context = None

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def first_handler(self) -> None: pass

    @abstractmethod
    def second_handler(self) -> None: pass


class FirstState(State):
    def first_handler(self) -> None:
        print(f'FirstState: handling the first_request...')
        print(f"FirstState: there's need to switch context state to 'SecondState'")
        self.context.switch_state(self.context.states["SecondState"])

    def second_handler(self) -> None:
        print(f'"FirstState" is handling the second_request...')


class SecondState(State):
    def first_handler(self) -> None:
        print(f'"SecondState" is handling the first_request...')

    def second_handler(self) -> None:
        print(f'SecondState: handling the second_request...')
        print(f"SecondState: there's need to switch context state to 'FirstState'")
        self.context.switch_state(self.context.states["FirstState"])


if __name__ == '__main__':
    def client_code() -> None:
        states: dict = {state.__class__.__name__: state for state in (FirstState(), SecondState())}
        context = Context(states)

        context.first_request()
        context.second_request()

    client_code()
