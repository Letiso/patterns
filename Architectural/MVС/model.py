from typing import List, Dict, Union
from copy import deepcopy
from errors import *


# Business-logic
class Model:
    def __init__(self, items: List[Dict[str, Union[str, int, float]]]) -> None:
        self._items: List[Dict[str, Union[str, int, float]]] = items
        self._item_type: str = 'Products assortment'

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

    def read_item(self, name: str) -> Dict[str, Union[str, int, float]]:
        if not (result := [product for product in self._items
                           if product['name'] == name]): raise NotExistsError(name, err_type='read')

        return deepcopy(result[0])

    def read_items(self) -> List[Dict[str, Union[str, int, float]]]:
        return deepcopy(self._items)

    def update_item(self, name: str, price: int, quantity: int) -> None:
        try:
            result = self.read_item(name)
            self._items[self._items.index(result)].update({
                'name': name,
                'price': price,
                'quantity': quantity
            })
        except NotExistsError:
            raise NotExistsError(name, err_type='update')

    def delete_item(self, name: str) -> None:
        try:
            result = self.read_item(name)
        except NotExistsError:
            raise NotExistsError(name, err_type='delete')

        del self._items[self._items.index(result)]
