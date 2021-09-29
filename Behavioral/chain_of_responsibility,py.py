from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def setNext(self, handler): pass

    @abstractmethod
    def handle(self, request: str): pass


class BaseHandler(Handler):
    def __init__(self):
        self._nextHandler = None

    def setNext(self, handler: Handler):
        self._nextHandler = handler
        return handler

    def handle(self, request: str):
        if self._nextHandler:
            return self._nextHandler.handle(request)
        else:
            return f'Nobody can do {request}'


class FrontEndDeveloper(BaseHandler):
    def handle(self, request: str):
        if request == 'front':
            return f'{self.__class__.__name__}: I can do {request}'
        else:
            return super().handle(request)


class BackEndDeveloper(BaseHandler):
    def handle(self, request: str):
        if request == 'back':
            return f'{self.__class__.__name__}: I can do {request}'
        else:
            return super().handle(request)


class HR(BaseHandler):
    def handle(self, request: str):
        if request == 'people':
            return f'{self.__class__.__name__}: I can do {request}'
        else:
            return super().handle(request)


if __name__ == '__main__':
    def client_code(request):
        front_dev, back_dev, hr = FrontEndDeveloper(), BackEndDeveloper(), HR()
        front_dev.setNext(back_dev).setNext(hr)
        print(front_dev.handle(request))

    for job in ['back', 'front', 'test']: client_code(job)
