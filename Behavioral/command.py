from abc import ABC, abstractmethod
from copy import deepcopy


# Receiver class
class Editor:
    def __init__(self):
        self._text = None
        self.selection = 0

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text: list):
        self._text = text

    def getSelected(self):
        return self._text[self.selection]

    def deleteSelected(self):
        del self._text[self.selection]

    def replaceSelected(self, new_string: str):
        self._text[self.selection] = new_string


# Abstract commands class
class Command(ABC):
    def __init__(self, application, editor):
        self._application = application
        self._editor = editor
        self._backup = None

    @property
    def app(self):
        return self._application

    @property
    def editor(self):
        return self._editor

    def saveBackup(self):
        self._backup = deepcopy(self.editor.text)

    def undo(self):
        self.editor.text = self._backup

    @abstractmethod
    def execute(self): pass


# Command history
class CommandHistory:
    def __init__(self):
        self._stack = []

    def push(self, command: Command):
        self._stack.append(command)

    def pop(self):
        return self._stack.pop()


# Concrete commands
class SelectCommand(Command):
    def execute(self):
        self.app.showText()
        self.editor.selection = int(input('Input wishing string to select:\n'))


class CopyCommand(Command):
    def execute(self):
        self.app.clipboard = self.editor.getSelected()
        print(f'{self.app.clipboard} was copied')


class PasteCommand(Command):
    def execute(self):
        self.saveBackup()
        self.editor.replaceSelected(self.app.clipboard)
        print(f'{self.app.clipboard} was pasted')
        return True


class CutCommand(Command):
    def execute(self):
        self.saveBackup()
        self.app.clipboard = self.editor.getSelected()
        self.editor.deleteSelected()
        print(f'{self.app.clipboard} was cut')
        return True


class UndoCommand(Command):
    def execute(self):
        self.app.undo()
        print('Making undo...')


# Sender class
class App:
    def __init__(self):
        self._editor = Editor()
        self._history = CommandHistory()
        self.clipboard = None
        self._buttons = [('SelectButton', SelectCommand(self, self._editor)),
                         ('CopyButton', CopyCommand(self, self._editor)),
                         ('CutButton', CutCommand(self, self._editor)),
                         ('PasteButton', PasteCommand(self, self._editor)),
                         ('UndoButton', UndoCommand(self, self._editor)), ]

    @property
    def history(self):
        return self._history

    @property
    def editor(self):
        return self._editor

    def showText(self):
        print(f'{"—" * 50}\nCurrent text:\n')
        for index, string in enumerate(self.editor.text):
            print(f'\t{index}: {string}')
        print("—" * 50)

    def showButtons(self):
        self.showText()
        print(f'Available actions:\n{"_" * 100}')
        for index, button in enumerate(self._buttons):
            print(f'\t|{index}: {button[0]}|', end='\t')
        print(f'\n{"_" * 100}')

        button = int(input('\nSelect wishing button to press:\n'))
        self.executeCommand(self._buttons[button][-1])
        input()

    def executeCommand(self, command: Command):
        if command.execute():
            self.history.push(command)

    def undo(self):
        if command := self.history.pop():
            command.undo()


# Client code
if __name__ == '__main__':
    user_text = ['First string',
                 'Second string',
                 'Third string',
                 'Fourth string',
                 'Fifth string', ]


    def clientCode(app: App, ):
        app.editor.text = user_text

        while True:
            app.showButtons()


    clientCode(App())
