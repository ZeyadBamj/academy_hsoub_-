from abc import ABC, abstractmethod

class OrderProcessor(ABC):
    def validate_order(self):
        print("\nValidating Order")

    def calculate_total(self):
        print("Calculating Price")

    @abstractmethod
    def process_payment(self):
        pass

    def send_notification(self):
        print("Sending Email")

    def process_order(self):
        self.validate_order()
        self.calculate_total()
        self.process_payment()
        self.send_notification()

class CreditCardProcessor(OrderProcessor):
    def process_payment(self):
        print("Processing credit card payment...")

class PayPalProcessor(OrderProcessor):
    def process_payment(self):
        print("Processing PayPal payment...")


if __name__ == "__main__":
    credit = CreditCardProcessor()
    credit.process_order()

    paypal = PayPalProcessor()
    paypal.process_order()