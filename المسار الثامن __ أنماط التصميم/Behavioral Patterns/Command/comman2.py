from abc import ABC, abstractmethod

class Editor:
    def __init__(self, text=""):
        self.text = text
        self.selection = ""

    def get_selection(self):
        return self.selection

    def delete_selection(self):
        print("Editor Deleting Selection....")
        self.text = self.text.replace(self.selection, "")

    def replace_selection(self, new_text):
        print(f"Editor Replacing selection with: {new_text}")
        self.text = self.text.replace(self.selection, new_text)


class Command(ABC):
    def __init__(self, app, editor):
        self.app = app
        self.editor = editor
        self.backup = ""

    def save_backup(self):
        self.backup = self.editor.text

    def undo(self):
        self.editor.text = self.backup

    @abstractmethod
    def execute(self):
        pass

class CopyCommand(Command):
    def execute(self):
        self.app.clipboard = self.editor.get_selection()
        print(f"CopyCommand Copied: {self.app.clipboard}")
        return False

class CutCommand(Command):
    def execute(self):
        self.save_backup()
        self.app.clipboard = self.editor.get_selection()
        print(f"CutCommand Cut: {self.app.clipboard}")
        self.editor.delete_selection()
        return True

class PasteCommand(Command):
    def execute(self):
        self.save_backup()
        print(f"PasteCommand Pasting: {self.app.clipboard}")
        self.editor.replace_selection(self.app.clipboard)
        return True


class UndoCommand(Command):
    def execute(self):
        print("Undo Undoing last command....")
        self.app.undo()
        return False

class CommandHistory:
    def __init__(self):
        self.history = []

    def push(self, command):
        self.history.append(command)

    def pop(self):
        if self.history:
            return self.history.pop()
        return None

class Application:
    def __init__(self):
        self.editors = []
        self.activeEditor = None
        self.clipboard = ""
        self.history = CommandHistory()

    def execute_command(self, command):
        print(f"\nApplication Executing: {command.__class__.__name__}")
        if command.execute():
            self.history.push(command)

    def undo(self):
        command = self.history.pop()
        if command:
            command.undo()



if __name__ == "__main__":
    app = Application()
    editor = Editor("Hello World")
    editor.selection = "World"

    app.activeEditor = editor

    app.execute_command(CopyCommand(app, editor))
    app.execute_command(CutCommand(app, editor))
    app.execute_command(PasteCommand(app, editor))

    print("\nText now:", editor.text)

    app.execute_command(UndoCommand(app, editor))
    print("After undo: ", editor.text)