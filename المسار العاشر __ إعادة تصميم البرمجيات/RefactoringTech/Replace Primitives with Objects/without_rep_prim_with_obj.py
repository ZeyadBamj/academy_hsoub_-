class Order:
    def __init__(self, data):
        self.priority = data['priority']



if __name__ == "__main__":
    order1 = Order({'id': 1, 'value': 200, 'priority': 'low'})
    order2 = Order({'id': 2, 'value': 100, 'priority': 'very high'})
    order3 = Order({'id': 3, 'value': 90, 'priority': 'high'})
    order4 = Order({'id': 4, 'value': 300, 'priority': 'medium'})

    def high_priority_count(orders):
        high_priority_orders = [order for order in orders
                                if 'high' == order.priority
                                or 'very high' == order.priority]
        return len(high_priority_orders)

    orders = [order1, order2, order3, order4]
    print(high_priority_count(orders))