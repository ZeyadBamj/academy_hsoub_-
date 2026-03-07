from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a,b):
        pass


class ConcreteAdd(Strategy):
    def execute(self, a,b):
        return a + b

class ConcreteSub(Strategy):
    def execute(self, a,b):
        return a - b

class ConcreteMult(Strategy):
    def execute(self, a,b):
        return a * b

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, s: Strategy):
        self._strategy = s

    def execute_strategy(self, a, b):
        print(self._strategy.execute(a,b))


if __name__ == "__main__":
    context = Context(ConcreteAdd())
    print("Strategy Add:", 2, "And", 5)
    context.execute_strategy(2, 5)

    context = Context(ConcreteSub())
    print("Strategy Sub:", 2, "And", 5)
    context.execute_strategy(2, 5)

    context = Context(ConcreteMult())
    print("Strategy Mult:", 2, "And", 5)
    context.execute_strategy(2, 5)