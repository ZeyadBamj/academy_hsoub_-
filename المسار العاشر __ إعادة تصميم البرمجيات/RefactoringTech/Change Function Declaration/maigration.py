class Hotel:

    _reservations = []

    # def add_reservation(self, customer):
    #     self.zz_add_reservation(customer, is_priority=False)
    #
    # def zz_add_reservation(self, customer, is_priority):
    #     self._reservations.append({'customer': customer, 'is_priority': is_priority})

    def add_reservation(self, customer, is_priority):
        self._reservations.append({'customer': customer, 'is_priority': is_priority})




if __name__ == "__main__":
    hotel1 = Hotel()

    customer1 = "Ahmed Salem"

    hotel1.add_reservation(customer1, True)

    print(hotel1._reservations)