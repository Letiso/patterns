from errors import *


# Controller
class Presenter:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def show_items_list(self) -> None:
        items = self.model.read_items()
        item_type = self.model.item_type

        self.view.show_items_list(item_type, items)

    def show_item(self, item_name) -> None:
        try:
            item = self.model.read_item(item_name)
            item_type = self.model.item_type
            self.view.show_item(item_type, item_name, item)
        except NotExistsError as error:
            self.view.display_missing_item_error(item_name, error)

    def add_item(self, name, price, quantity) -> None:
        assert price > 0, 'price must be greater than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        item_type = self.model.item_type

        try:
            self.model.add_item(name, price, quantity)
            self.view.display_item_stored(name, item_type)
        except AlreadyExistsError as error:
            self.view.display_item_already_stored_error(name, item_type, error)

    def update_item(self, name, price, quantity) -> None:
        assert price > 0, 'price must be greater than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        item_type = self.model.item_type

        try:
            older = self.model.read_item(name)
            self.model.update_item(name, price, quantity)
            self.view.display_item_updated(
                name, older['price'], older['quantity'], price, quantity)
        except NotExistsError as error:
            self.view.display_item_not_yet_stored_error(name, item_type, error)

    def delete_item(self, name) -> None:
        item_type = self.model.item_type
        try:
            self.model.delete_item(name)
            self.view.display_item_deletion(name)
        except NotExistsError as error:
            self.view.display_item_not_yet_stored_error(name, item_type, error)
