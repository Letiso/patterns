from abc import ABC, abstractmethod


# Receiver class
class Editor:
    def __init__(self):
        self._text = self._selection = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text: list):
        self._text = text

    def setSelection(self):
        self._selection = input('Input wishing string to select:')

    def getSelection(self):
        return self._text[self._selection]

    def deleteSelection(self):
        del self._text[self._selection]

    def replaceSelection(self, new_string: str):
        self._text[self._selection] = new_string


# Abstract commands class
class Command(ABC):
    def __init__(self, client, editor):
        self._client = client
        self._editor = editor
        self._backup = None

    def saveBackup(self):
        self._backup = self._editor.text

    def undo(self):
        self._editor.text = self._backup

    @abstractmethod
    def execute(self): pass


# Concrete commands
class CopyCommand(Command):
    def execute(self): pass


class PasteCommand(Command):
    def execute(self): pass


class CutCommand(Command):
    def execute(self): pass


class UndoCommand(Command):
    def execute(self): pass


# Sender class
class App: pass


# Client code
if __name__ == '__name__':
    def clientCode(app: App): pass

    clientCode(App())
