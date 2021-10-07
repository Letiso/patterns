from typing import List, Dict, Union
from copy import deepcopy


class Model:
    def __init__(self, products: List[Dict[str, Union[str, int, float]]]):
        self._products: List[Dict[str, Union[str, int, float]]] = products
        self._errors: Dict[str: str] = {
            'exists': 'product already exists',
            'not_exists': "product doesn't exists",
        }

    def set_products(self, products: List[Dict[str, Union[str, int, float]]]):
        self._products = products

    def add_product(self, name: str, price: int, quantity: int):
        if self.read_product(name): return f'"{name.title()}" ' + self._errors['exists']

        self._products.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    def read_product(self, name: str):
        if not (result := [product for product in self._products
                           if product['name'] == name]):
            return f'"{name.title()}" ' + self._errors['not_exists']

        return deepcopy(result[0])

    def read_products(self):
        return deepcopy(self._products)

    def update_product(self, name: str, price: int, quantity: int) -> Union[str, None]:
        if (result := self.read_product(name)) is str: return result

        self._products[self._products.index(result)].update({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    def delete_product(self, name: str) -> Union[str, None]:
        if (result := self.read_product(name)) is str: return result

        del self._products[self._products.index(result)]


class View:
    pass


if __name__ == '__main__':
    def client_code(data_base: Model): pass

    db = Model([
            {'name': 'bread', 'price': 0.5, 'quantity': 20},
            {'name': 'milk', 'price': 1.0, 'quantity': 10},
            {'name': 'wine', 'price': 10.0, 'quantity': 5},
        ])
