from abc import ABC


# Observer
class Subscriber:
    _methods = None

    def update(self, notifying: dict) -> None:
        self._methods[notifying['method_name']](*notifying['args'])


# UI
class View(Subscriber):
    def __init__(self, controller):
        self._controller = controller
        self._methods: dict = {method_name: method
                               for method_name, method in self.__class__.__dict__.items()
                               if 'item' in method_name}

    # Requests part
    def show_items_list(self) -> None:
        self._controller.show_items_list()

    def show_item(self, item_name) -> None:
        self._controller.show_item(item_name)

    def add_item(self, name: str, price, quantity) -> None:
        self._controller.add_item(name, price, quantity)

    def update_item(self, name: str, price, quantity) -> None:
        self._controller.update_item(name, price, quantity)

    def delete_item(self, name) -> None:
        self._controller.delete_item(name)

    # Display part
    @staticmethod
    def display_items_list(item_type, items) -> None:
        print(f'\n--- {item_type.upper()} LIST ---')
        for i, item in enumerate(items):
            print(f'{i + 1}. {item}')

    @staticmethod
    def display_item(item_type, item, item_info) -> None:
        print('\n//////////////////////////////////////////////////////////////')
        print(f'Good news, we have some {item.upper()}!')
        print(f'{item_type.upper()} INFO: {item_info}')
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_item_error(item, err) -> None:
        print('\n**************************************************************')
        print(f'We are sorry, but we have no {item.upper()}!')
        print(f'{err}')
        print('**************************************************************')

    @staticmethod
    def display_item_already_stored_error(item, item_type, err) -> None:
        print('\n**************************************************************')
        print(f'Sorry, but we already have {item.upper()} in our {item_type} list!')
        print(f'{err}')
        print('**************************************************************')

    @staticmethod
    def display_item_not_yet_stored_error(item, item_type, err) -> None:
        print('\n**************************************************************')
        print(f"We don't have any {item.upper()} in our {item_type} list. Please add it first!")
        print(f'{err}')
        print('**************************************************************')

    @staticmethod
    def display_item_stored(item, item_type) -> None:
        print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(f'We have just added some {item.upper()} to our {item_type} list!')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_item_updated(item, o_price, o_quantity, n_price, n_quantity) -> None:
        print('\n---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print(f'Change {item} price: {o_price} --> {n_price}')
        print(f'Change {item} quantity: {o_quantity} --> {n_quantity}')
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_deletion(name) -> None:
        print('\n--------------------------------------------------------------')
        print(f'We have just removed {name} from our list')
        print('--------------------------------------------------------------')
