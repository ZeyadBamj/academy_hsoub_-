class Product:
    def __init__(self, p_name, desc, color, size, cost):
        self.p_name = p_name
        self.desc = desc
        self.color = color
        self.size = size
        self.cost = cost

    def view(self):
        return f"Name: {self.p_name} | description: {self.desc} |Color: {self.color} | Size: {self.size} | Cost: {self.cost}"

    def change_desc(self, st):
        self.desc = st
    def discount(self, dis):
         self.cost = self.cost - self.cost * dis / 100
         return self.cost
    def rate(self, rate):
        return f"{self.p_name} have rate: {rate}"


phone = Product('iphone', 'version 17', 'blue', 'pro max', 5000)

phone.change_desc('version 19')

phone.discount(50)

print(phone.view())
print(phone.rate('⭐⭐⭐'))