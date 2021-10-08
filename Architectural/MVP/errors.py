# Exceptions
class Error(Exception):
    _error = None

    def __init__(self, name: str, err_type: str = None) -> None:
        self._name: str = name
        self._err_type: str = err_type

    def __str__(self) -> str:
        return self._error


class NotExistsError(Error):
    def __init__(self, name, err_type: str = None) -> None:
        super().__init__(name, err_type)
        self._error: str = f"Can't {self._err_type} because of product '{self._name}' does not exists"


class AlreadyExistsError(Error):
    def __init__(self, name, err_type: str = None) -> None:
        super().__init__(name, err_type)
        self._error: str = f"Can't {self._err_type} because of product '{self._name}' already exists"
