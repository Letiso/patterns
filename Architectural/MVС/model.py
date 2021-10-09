from typing import List, Dict, Union
from copy import deepcopy
from abc import ABC, abstractmethod
from errors import *


# Observer abstract class
class Publisher(ABC):

    @staticmethod
    def make_notifying(method_name: str, *args: any) -> Dict[str, any]:
        return {'method': method_name,
                'args': args}

    @abstractmethod
    def subscribe(self, subscriber) -> None: pass

    @abstractmethod
    def unsubscribe(self, subscriber) -> None: pass

    @abstractmethod
    def notify(self, notifying: dict) -> None: pass


# Business-logic
class Model(Publisher):
    def __init__(self, items: List[Dict[str, Union[str, int, float]]]) -> None:
        self._items: List[Dict[str, Union[str, int, float]]] = items
        self._item_type: str = 'Products assortment'
        self._subscribers: List = []

    @property
    def item_type(self) -> str:
        return self._item_type

    def add_item(self, name: str, price: int, quantity: int) -> None:
        try:
            self.read_item(name)
            raise AlreadyExistsError(name, err_type='add')
        except NotExistsError:
            self._items.append({
                'name': name,
                'price': price,
                'quantity': quantity
            })
            notifying = self.make_notifying('display_item_stored', name, self._item_type)
            self.notify(notifying)

    def read_items(self) -> None:
        notifying = self.make_notifying('display_items_list', self._item_type, self._items)
        self.notify(notifying)

    def read_item(self, name: str, direct_call: bool = False) -> dict:
        if not (itemsList := [product for product in self._items
                              if product['name'] == name]): raise NotExistsError(name, err_type='read')

        if direct_call:
            notifying = self.make_notifying('display_item', self._item_type, name, itemsList[0])
            self.notify(notifying)

        return itemsList[0]

    def update_item(self, item_name: str, price: int, quantity: int) -> None:
        try:
            item = self.read_item(item_name)
            self._items[self._items.index(item)].update({
                'name': item_name,
                'price': price,
                'quantity': quantity
            })
        except NotExistsError:
            raise NotExistsError(item_name, err_type='update')

    def delete_item(self, name: str) -> None:
        try:
            result = self.read_item(name)
        except NotExistsError:
            raise NotExistsError(name, err_type='delete')

        del self._items[self._items.index(result)]

    # Publisher part
    def subscribe(self, subscriber) -> None:
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber) -> None:
        del (items := self._subscribers)[items.index(subscriber)]

    def notify(self, notifying: dict) -> None:
        for subscriber in self._subscribers:
            subscriber.update(notifying)
