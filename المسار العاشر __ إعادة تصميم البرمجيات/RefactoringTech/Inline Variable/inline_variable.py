def useless_variable(order):
    base_price = order['quantity'] * order['item_price']
    return base_price > 1000

def without_variable(order):
    return order['quantity'] * order['item_price'] > 1000

if __name__ == "__main__":
    order = {'quantity': 550, 'item_price': 20}
    print(useless_variable(order))
    print(without_variable(order))