from typing import Protocol


class PaymentMethod(Protocol):
    def authorize_payment(self, amount: float) -> bool:
        ...

    def process_payment(self, amount: float) -> bool:
        ...


class CreditCardPayment:
    def authorize_payment(self, amount: float) -> bool:
        print(f"Authorize credit card payment of ${amount}")
        return True

    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount}")
        return True


class PayPalPayment:
    def authorize_payment(self, amount: float) -> bool:
        print(f"Authorize PayPal payment of ${amount}")
        return True

    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount}")
        return True


def process_order(payment: PaymentMethod, amount: float):
    if payment.authorize_payment(amount):
        if payment.process_payment(amount):
            print("Payment Successful")
    else:
        print("Payment Authorization Failed")


ccp = CreditCardPayment()
ppp = PayPalPayment()

process_order(ccp, 100.0)
process_order(ppp, 200.0)