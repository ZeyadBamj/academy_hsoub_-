from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class BaseHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

class MonkeyHandler(BaseHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)

class SquirrelHandler(BaseHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)

class DogHandler(BaseHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)

class Human(BaseHandler):
    def handle(self, request: Any):
        if request == "Cup of coffee":
            return f"Human: I'll drink the {request}"
        else:
            return super().handle(request)

def client_code(handler: BaseHandler) -> None:
    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f" {result}", end="")
        else:
            print(f" {food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()
    human = Human()

    human.set_next(squirrel).set_next(dog).set_next(monkey)

    # يجب أن يكون العميل قادرًا على إرسال طلب إلى أي مداوِل، وليس إلى أول واحد في السلسلة فقط.
    print("Chain: Monkey > Squirrel > Dog > Human")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)