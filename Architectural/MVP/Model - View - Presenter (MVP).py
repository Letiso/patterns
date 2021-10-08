from model import Model
from presenter import Presenter
from view import View


# Client code
if __name__ == '__main__':
    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    def client_code(presenter: Presenter):
        print('MVP: Model - View - Presenter')
        presenter.show_items_list()

        presenter.show_item('chocolate')
        presenter.show_item('bread')

        presenter.add_item('bread', price=1.0, quantity=5)
        presenter.add_item('chocolate', price=2.0, quantity=10)

        presenter.show_item('chocolate')

        presenter.update_item('milk', price=1.2, quantity=20)
        presenter.update_item('ice cream', price=3.5, quantity=20)

        presenter.delete_item('fish')
        presenter.delete_item('bread')

    client_code(Presenter(Model(my_items), View()))
