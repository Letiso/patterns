from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self): pass


class Truck(Transport):
    def deliver(self):
        print(f'Goods were delivered by {self.__class__.__name__}\n')


class Ship(Transport):
    def deliver(self):
        print(f'Goods were delivered by {self.__class__.__name__}\n')


class Train(Transport):
    def deliver(self):
        print(f'Goods were delivered by {self.__class__.__name__}\n')


class TransportFactory(ABC):
    @abstractmethod
    def create_transport(self): pass


class TruckFactory(TransportFactory):
    def create_transport(self) -> Truck:
        return Truck()


class ShipFactory(TransportFactory):
    def create_transport(self) -> Ship:
        return Ship()


class TrainFactory(TransportFactory):
    def create_transport(self) -> Train:
        return Train()


def transport_factory_types_dict(func):
    transport_types = dict(
        [(transport.__name__[:transport.__name__.index('Factory')], transport)
         for transport in TransportFactory.__subclasses__()]
    )
    print(transport_types, end='\n\n')

    def wrapper(transport_request: str):
        return func(transport_request, transport_types)

    return wrapper


@transport_factory_types_dict
def logistics(transport_request: str, transport_types: dict = None):
    transport_request = transport_request.title()
    print(f'Order was accepted by {transport_types[transport_request].__name__}')
    transport = transport_types[transport_request]().create_transport()
    transport.deliver()


logistics('ship')
logistics('train')
logistics('truck')
