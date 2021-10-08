from model import Model
from controller import Controller
from view import View


# Client code
if __name__ == '__main__':
    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    def client_code(controller: Controller):
        print('MVC: Model - View - Controller')

        controller.show_items_list()

        controller.show_item('chocolate')
        controller.show_item('bread')

        controller.add_item('bread', price=1.0, quantity=5)
        controller.add_item('chocolate', price=2.0, quantity=10)

        controller.show_item('chocolate')

        controller.update_item('milk', price=1.2, quantity=20)
        controller.update_item('ice cream', price=3.5, quantity=20)

        controller.delete_item('fish')
        controller.delete_item('bread')

    client_code(Controller(Model(my_items), View()))
