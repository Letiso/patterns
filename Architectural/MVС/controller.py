from errors import *


# Controller
class Controller:
    def __init__(self, model) -> None:
        self._model = model

    def show_items_list(self) -> None:
        self._model.read_items()

    def show_item(self, item_name) -> None:
        try:
            self._model.read_item(item_name, direct_call=True)
        except NotExistsError as error:
            notifying = self._model.make_notifying('display_missing_item_error',
                                                   item_name, error)
            self._model.notify(notifying)

    def add_item(self, item_name, price, quantity) -> None:
        assert price > 0, 'price must be greater than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        item_type = self._model.item_type

        try:
            self._model.add_item(item_name, price, quantity)

        except AlreadyExistsError as error:
            notifying = self._model.make_notifying('display_item_already_stored_error',
                                                   item_name, item_type, error)
            self._model.notify(notifying)

    def update_item(self, item_name, price, quantity) -> None:
        assert price > 0, 'price must be greater than 0'
        assert quantity >= 0, 'quantity must be greater than or equal to 0'
        item_type = self._model.item_type

        try:
            older = self._model.read_item(item_name)
            self._model.update_item(item_name, price, quantity)

            notifying = self._model.make_notifying('display_item_updated',
                                                   item_name, older['price'], older['quantity'], price, quantity)
            self._model.notify(notifying)
        except NotExistsError as error:
            notifying = self._model.make_notifying('display_item_not_yet_stored_error',
                                                   item_name, item_type, error)
            self._model.notify(notifying)

    def delete_item(self, item_name) -> None:
        item_type = self._model.item_type
        try:
            self._model.delete_item(item_name)
            notifying = self._model.make_notifying('display_item_deletion',
                                                   item_name)
            self._model.notify(notifying)

        except NotExistsError as error:
            notifying = self._model.make_notifying('display_item_not_yet_stored_error',
                                                   item_name, item_type, error)
            self._model.notify(notifying)

