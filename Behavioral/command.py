from abc import ABC, abstractmethod


# Receiver class
class Editor:
    def __init__(self):
        self._text = self.selection = None

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
    def __init__(self, application):
        self._application = application
        self._backup = None

    @property
    def application(self):
        return self._application

    def saveBackup(self):
        self._backup = self.application.editor.text

    def undo(self):
        self.application.editor.text = self._backup

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
        self.application.editor.selection = int(input('Input wishing string to select:\n'))
        print()


class CopyCommand(Command):
    def execute(self):
        return False


class PasteCommand(Command):
    def execute(self):
        return True


class CutCommand(Command):
    def execute(self):
        return True


class UndoCommand(Command):
    def execute(self):
        self.app.undo()
        return


# Sender class
class App:
    def __init__(self):
        self._editor = Editor()
        self._history = CommandHistory()
        self._clipboard = None
        self.createUI()

    @property
    def editor(self):
        return self._editor

    @property
    def history(self):
        return self._history

    def createUI(self):
        pass

    def showUI(self):
        print('Current text:\n')
        for index, string in enumerate(self.editor.text):
            print(f'\t{index}: {string}')

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

    def clientCode(app: App):
        app.editor.text = user_text
        app.createUI()
        select = SelectCommand(app)
        select.execute()
        print(app.editor.getSelected())


    clientCode(App())
