class Flyweight:
    def __init__(self, font, size, color):
        self.font = font
        self.size = size
        self.color = color

    def draw(self, char, x, y):
        print(f"Draw '{char}' in {self.font} Size {self.size} at ({x}, {y})")


class FlyweightFactory(Flyweight):
    _flyweights = {}

    @staticmethod
    def get_flyweight(font, size, color):
        key = (font, size, color)
        if key not in FlyweightFactory._flyweights:
            FlyweightFactory._flyweights[key] = Flyweight(font, size, color)

        return FlyweightFactory._flyweights[key]

text = "HELLO"

for i, ch in enumerate(text):
    fw = FlyweightFactory.get_flyweight("Arial", 14, "Blue")
    fw.draw(ch, i * 20, 10)