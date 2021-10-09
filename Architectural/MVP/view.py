from abc import ABC, abstractmethod


# UI
class AbstractView(ABC):
    @staticmethod
    @abstractmethod
    def show_items_list(item_type, items) -> None: pass

    @staticmethod
    @abstractmethod
    def show_item(item_type, item, item_info) -> None: pass

    @staticmethod
    @abstractmethod
    def display_missing_item_error(item, err) -> None: pass

    @staticmethod
    @abstractmethod
    def display_item_already_stored_error(item, item_type, err) -> None: pass

    @staticmethod
    @abstractmethod
    def display_item_not_yet_stored_error(item, item_type, err) -> None: pass

    @staticmethod
    @abstractmethod
    def display_item_stored(item, item_type) -> None: pass

    @staticmethod
    @abstractmethod
    def display_item_updated(item, o_price, o_quantity, n_price, n_quantity) -> None: pass

    @staticmethod
    @abstractmethod
    def display_item_deletion(name) -> None: pass


class View(AbstractView):
    @staticmethod
    def show_items_list(item_type, items) -> None:
        print(f'\n--- {item_type.upper()} LIST ---')
        for i, item in enumerate(items):
            print(f'{i + 1}. {item}')

    @staticmethod
    def show_item(item_type, item, item_info) -> None:
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
        print(f"We don't have any {item.upper()} in our {item_type} list. Please insert it first!")
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
