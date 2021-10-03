from abc import ABC, abstractmethod
from random import sample, randrange


# Publishers interface
class Publisher(ABC):
    @abstractmethod
    def subscribe(self, subscriber: 'Subscriber', product_type: str) -> None: pass

    @abstractmethod
    def unsubscribe(self, subscriber: 'Subscriber', product_type: str) -> None: pass

    @abstractmethod
    def notify(self, notifying: dict) -> None: pass


# Concrete publishers
class Shop(Publisher):
    def __init__(self) -> None:
        self._products: dict = {
            'phones': {
                'Meizu': True,
                'OnePlus': True,
                'Redmi': True,
                'Samsung': None
            },
            'tv': {
                'LG': True,
                'Samsung': True,
                'Xiaomi': True,
                'Ozone': None
            },
            'notebooks': {
                'Asus': True,
                'HP': True,
                'Lenovo': True,
                'Predator': None
            },
        }
        self._subscribers = {productType: [] for productType in self._products}

    @property
    def products(self) -> dict:
        return self._products

    def update_assortment(self, products: dict) -> None:
        if not products: return

        for productType in products:
            self._products[productType].update(products[productType])
            notifying = {'publisher': self.__class__.__name__,
                         'subscriber': None,
                         'message': 'Was appeared a products from your wishlist in our assortment',
                         'productType': productType}

            self.notify(notifying)

    def subscribe(self, subscriber: 'Subscriber', product_type: str) -> None:
        self._subscribers[product_type].append(subscriber)

    def unsubscribe(self, subscriber: 'Subscriber', product_type: str) -> None:
        del (products := self._subscribers[product_type])[products.index(subscriber)]

    def notify(self, notifying: dict) -> None:
        for subscriber in self._subscribers[notifying['productType']]:
            notifying['message'] = f'Greetings, {subscriber.name}!\n' + notifying["message"].split("\n")[-1]
            subscriber.update(notifying)


# Subscriber abstract class
class Subscriber(ABC):
    @abstractmethod
    def update(self, notifying: dict) -> None: pass


# Concrete subscribers
class Customer(Subscriber):
    def __init__(self, name: str, wishlist: list) -> None:
        self._name: str = name
        self._wishlist: list = wishlist

    @property
    def name(self) -> str:
        return self._name

    @property
    def wishlist(self) -> list:
        return self._wishlist

    def update(self, notifying: dict) -> None:
        print(f'\nTaking massage from {notifying["publisher"]}\n'
              f'Message:\n{notifying["message"]}:\n'
              f'{notifying["productType"]}')


# Client code
if __name__ == '__main__':
    def get_random_name() -> str:
        first_names = ['Christopher', 'Roger', 'Peter', 'Emily', 'Diana', 'Helen']
        last_names = ['Wade', 'Page', 'Neal', 'Ray', 'Mitchell', 'Hill', 'Watson']

        return f'{first_names[randrange(len(first_names))]} {last_names[randrange(len(last_names))]}'


    def client_code() -> None:
        shop = Shop()
        customers = [Customer(get_random_name(), sample(sorted(shop.products), randrange(1, 4)))
                     for customer in range(3)]

        for customer in customers:
            print(f'{customer.name} - {customer.wishlist}')
            for productType in customer.wishlist:
                shop.subscribe(customer, productType)

        shop.update_assortment({
            'phones': {
                'Samsung': True},
            'tv': {
                'Ozone': True}
        })


    client_code()
