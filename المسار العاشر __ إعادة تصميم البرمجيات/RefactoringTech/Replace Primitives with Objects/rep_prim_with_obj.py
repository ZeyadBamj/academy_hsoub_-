class Order:
    def __init__(self, data):
        self.__priority = data['priority']

    def get_priority(self):
        return self.__priority

    def get_priority_string(self):
        return str(self.__priority)

    def set_priority(self, value):
        self.__priority = Priority(value)


class Priority:
    def __init__(self, value):
        valid_values = ['very low', 'low', 'medium', 'high', 'very high']
        if value in valid_values:
            self.__value = value
        else:
            raise ValueError("Priority value must be one of {}".format(valid_values))

    def __str__(self):
        return self.__value



if __name__ == "__main__":
    order1 = Order({'id': 1, 'value': 200, 'priority': 'low'})
    order2 = Order({'id': 2, 'value': 100, 'priority': 'very high'})
    order3 = Order({'id': 3, 'value': 90, 'priority': 'high'})
    order4 = Order({'id': 4, 'value': 300, 'priority': 'medium'})

    def high_priority_count(orders):
        count = 0
        for order in orders:
            if ('high' == order.get_priority_string() or
                    'very high' == order.get_priority_string()):
                count += 1
        return count

    orders = [order1, order2, order3, order4]
    # order1.set_priority('extreme')
    print(high_priority_count(orders))