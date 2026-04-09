class Order:
    def __init__(self, record):
        self._data = record

    def quantity(self):
        return self._data['quantity']

    def item_price(self):
        return self._data['item_price']

    def base_price(self):
        return self.quantity() * self.item_price()

    def quantity_discount(self):
        return max(0, self.quantity() - 500) * self.item_price() * 0.05

    def shipping(self):
        return min(self.quantity() * self.item_price() * 0.1, 100)

    def price(self):
        return self.base_price() - self.quantity_discount() + self.shipping()


order = {'quantity': 550, 'item_price': 20}



def get_price():
     # price is base price - quantity discount + shipping
     return order['quantity'] * order['item_price'] - max(0, order['quantity'] - 500) * order['item_price'] * 0.05 + min(order['quantity'] * order['item_price'] * 0.1, 100)

def get_price2():
    base_price = order['quantity'] * order['item_price']
    quantity_discount = max(0, order['quantity'] - 500) * order['item_price'] * 0.05
    shipping = min(order['quantity'] * order['item_price'] * 0.1, 100)
    return base_price - quantity_discount + shipping


if __name__ == '__main__':
    print(get_price())
    print(get_price2())

    order_obj = Order({'quantity': 550, 'item_price': 20})
    print(order_obj.price())