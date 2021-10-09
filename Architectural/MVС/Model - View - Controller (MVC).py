from model import Model
from controller import Controller
from view import View

my_items = [{'name': 'bread', 'price': 0.5, 'quantity': 20},
            {'name': 'milk', 'price': 1.0, 'quantity': 10},
            {'name': 'wine', 'price': 10.0, 'quantity': 5}, ]

model = Model(my_items)
current_view = View(Controller(model))
model.subscribe(current_view)


def client_code(view: View):
    print('MVC: Model - View - Controller')

    view.show_items_list()

    view.show_item('chocolate')
    view.show_item('bread')

    view.add_item('bread', price=1.0, quantity=5)
    view.add_item('chocolate', price=2.0, quantity=10)

    view.show_item('chocolate')

    view.update_item('milk', price=1.2, quantity=20)
    view.update_item('ice cream', price=3.5, quantity=20)

    view.delete_item('fish')
    view.delete_item('bread')


# Client code
if __name__ == '__main__':
    client_code(current_view)
