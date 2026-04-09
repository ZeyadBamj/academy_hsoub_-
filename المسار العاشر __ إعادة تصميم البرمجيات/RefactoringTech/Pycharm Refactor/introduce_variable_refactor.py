discount_rate = 0.05
order = {'quantity': 550, 'item_price': 20}



def get_price():
     # price is base price - quantity discount + shipping
     base_price = order['quantity'] * order['item_price']
     quantity_discount = max(0, order['quantity'] - 500) * order['item_price'] * discount_rate
     shipping = min(base_price * 0.1, 100)
     return base_price - quantity_discount + shipping

def get_price2():
    base_price = order['quantity'] * order['item_price']
    quantity_discount = max(0, order['quantity'] - 500) * order['item_price'] * 0.05
    shipping = min(order['quantity'] * order['item_price'] * 0.1, 100)
    return base_price - quantity_discount + shipping


if __name__ == '__main__':
    print(get_price())
    print(get_price2())