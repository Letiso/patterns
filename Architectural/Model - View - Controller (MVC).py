from typing import List, Dict, Union
from copy import deepcopy


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


# Model
class Model:
    def __init__(self, products: List[Dict[str, Union[str, int, float]]]) -> None:
        self._products: List[Dict[str, Union[str, int, float]]] = products

    def add_product(self, name: str, price: int, quantity: int) -> None:
        try:  self.read_product(name)
        except AlreadyExistsError: raise AlreadyExistsError(name, err_type='add')

        self._products.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    def read_product(self, name: str) -> Dict[str, Union[str, int, float]]:
        if not (result := [product for product in self._products
                           if product['name'] == name]): raise NotExistsError(name, err_type='read')

        return deepcopy(result[0])

    def read_products(self) -> List[Dict[str, Union[str, int, float]]]:
        return deepcopy(self._products)

    def update_product(self, name: str, price: int, quantity: int) -> None:
        try:  result = self.read_product(name)
        except NotExistsError: raise NotExistsError(name, err_type='update')

        self._products[self._products.index(result)].update({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    def delete_product(self, name: str) -> None:
        try:  result = self.read_product(name)
        except NotExistsError: raise NotExistsError(name, err_type='delete')

        del self._products[self._products.index(result)]


# Controller


# View
class View:
    pass


# Client code
if __name__ == '__main__':
    def client_code(data_base: Model): pass


    db = Model([
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ])

    db.read_product('meat')
    db.delete_product('meat')
