from abc import ABC, abstractmethod

# Products


class Transport(ABC):
    @abstractmethod
    def deliver(self): pass


class Truck(Transport):
    def deliver(self):
        print(f'Goods were delivered by {self.__class__.__name__}.', end='\n\n')


class Ship(Transport):
    def deliver(self):
        print(f'Goods were delivered by {self.__class__.__name__}.', end='\n\n')


class Train(Transport):
    def deliver(self):
        print(f'Goods were delivered by {self.__class__.__name__}.', end='\n\n')

# Factories


class TransportFactory(ABC):
    @abstractmethod
    def create_transport(self) -> Transport: pass


class TruckFactory(TransportFactory):
    def create_transport(self) -> Truck:
        return Truck()


class ShipFactory(TransportFactory):
    def create_transport(self) -> Ship:
        return Ship()


class TrainFactory(TransportFactory):
    def create_transport(self) -> Train:
        return Train()

# Client


def transport_factory_dict(func):
    transport_factories = dict(
        [(transport_factory.__name__[:transport_factory.__name__.index('Factory')], transport_factory)
         for transport_factory in TransportFactory.__subclasses__()]
    )
    print(f'Current available factories:\n'
          f'{transport_factories}', end='\n\n')

    def wrapper(transport_request: str):
        return func(transport_factories[transport_request.title()]())

    return wrapper


@transport_factory_dict
def logistics(factory: TransportFactory):
    print(f'Order was accepted by {factory.__class__.__name__}')
    transport = factory.create_transport()
    transport.deliver()


if __name__ == '__main__':
    for request in 'truck', 'ship', 'train': logistics(request)
