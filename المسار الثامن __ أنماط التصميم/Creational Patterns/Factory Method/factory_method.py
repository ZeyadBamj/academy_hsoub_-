from abc import ABC, abstractmethod

class Btn(ABC):
    @abstractmethod
    def render(self):
        pass

class WinBtn(Btn):
    def render(self):
        return "Windows Button"

class MacBtn(Btn):
    def render(self):
        return "Mac Button"

class LinuxBtn(Btn):
    def render(self):
        return "Linux Button"


class Dialog(ABC):
    @abstractmethod
    def create_btn(self) -> Btn:
        pass

    def dialog_render(self):
        ok_btn = self.create_btn()
        result = f"Dialog: {ok_btn.render()}"
        return result

class WinDialog(Dialog):
    def create_btn(self) -> WinBtn:
        return WinBtn()

class MacDialog(Dialog):
    def create_btn(self) -> MacBtn:
        return MacBtn()

class LinuxDialog(Dialog):
    def create_btn(self) -> LinuxBtn:
        return LinuxBtn()


def client_code(dialog: Dialog):
    print(f"Client: The Button is...\n{dialog.dialog_render()}\n")



if __name__ == "__main__":
    print("\nApp: Windows")
    client_code(WinDialog())
    print("App: Mac")
    client_code(MacDialog())
    print("App: Linux")
    client_code(LinuxDialog())
