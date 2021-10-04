from abc import ABC, abstractmethod


# Interface and abstract class
class Handler(ABC):
    @abstractmethod
    def setNext(self, handler): pass

    @abstractmethod
    def handle(self, request: str) -> str: pass


class BaseHandler(Handler):
    def __init__(self):
        self._nextHandler = None

    def setNext(self, handler: Handler) -> Handler:
        self._nextHandler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> str:
        if self._nextHandler:
            return self._nextHandler.handle(request)
        else:
            return f'Nobody can do {request}'


# Concrete handlers
class FrontEndDeveloperHandler(BaseHandler):
    def handle(self, request: str) -> str:
        if request == 'front':
            return f'{self.__class__.__name__}: I can do {request}'
        else:
            return super().handle(request)


class BackEndDeveloperHandler(BaseHandler):
    def handle(self, request: str) -> str:
        if request == 'back':
            return f'{self.__class__.__name__}: I can do {request}'
        else:
            return super().handle(request)


class HRHandler(BaseHandler):
    def handle(self, request: str) -> str:
        if request == 'people':
            return f'{self.__class__.__name__}: I can do {request}'
        else:
            return super().handle(request)


# Client code
if __name__ == '__main__':
    def client_code(request):
        front_dev, back_dev, hr = FrontEndDeveloperHandler(), BackEndDeveloperHandler(), HRHandler()
        front_dev.setNext(back_dev).setNext(hr)
        print(front_dev.handle(request))

    for job in ['back', 'front', 'test']: client_code(job)
