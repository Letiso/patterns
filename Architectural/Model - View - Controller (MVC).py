from typing import List, Dict, Union
from copy import deepcopy


def singleton(cls):
    instance = cls()

    def wrapper(): return instance

    return wrapper


@singleton
class Assortment:
    def __init__(self):
        self.products: List[Dict[str, Union[str, int, float]]] = list()
        self.errors: Dict[str: str] = {
            'exists': 'product already exists',
            'not_exists': "product doesn't exists",
        }

    def set_products(self, products: List[Dict[str, Union[str, int, float]]]):
        self.products = products

    def add_product(self, name: str, price: int, quantity: int):
        if self.read_product(name): return f'"{name.title()}" ' + self.errors['exists']

        self.products.append({'name': name,
                              'price': price,
                              'quantity': quantity})

    def read_product(self, name: str):
        if not (result := [product for product in self.products
                           if product['name'] == name]):
            return f'"{name.title()}" ' + self.errors['not_exists']

        return deepcopy(result[0])

    def read_products(self):
        return deepcopy(self.products)


if __name__ == '__main__':
    db = Assortment()

    db.set_products([
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ])

    print(db.add_product(**{'name': 'wine', 'price': 10.0, 'quantity': 10}))
    print(db.read_product('bread'))
    print(db.read_product('water'))
