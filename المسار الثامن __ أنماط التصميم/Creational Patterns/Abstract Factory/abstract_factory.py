from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def create_btn(self):
        pass

class WinButton(Button):
    def create_btn(self):
        return "Windows Button"


class MacButton(Button):
    def create_btn(self):
        return "Mac Button"


class Checkbox(ABC):
    @abstractmethod
    def create_checkbox(self):
        pass

    @abstractmethod
    def from_another(self, coll: Button):
        pass


class WinCheckbox(Checkbox):
    def create_checkbox(self):
        return "Windows Checkbox"

    def from_another(self, coll: Button):
        result = coll.create_btn()
        return f"collaborator with ({result})"

class MacCheckbox(Checkbox):
    def create_checkbox(self):
        return "Mac Checkbox"

    def from_another(self, coll: Button):
        result = coll.create_btn()
        return f"collaborator with ({result})"


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


def client_code(f: GUIFactory):
    button = f.create_button()
    checkbox = f.create_checkbox()
    print(f"[{checkbox.create_checkbox()}]")
    print(f"[{checkbox.from_another(button)}]\n")


if __name__ == "__main__":
    print("\nClient: Testing Windows Factory:")
    client_code(WinFactory())
    print("Client: Testing Mac Factory:")
    client_code(MacFactory())