from abc import ABC, abstractmethod
class furniture(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ",amount)
#This function is telling us to pass in an argument, but we won't tell you how or what kind
#of data it will be
        @abstractmethod
        def payment(self,amount):
            pass

class DebitCardPayment(furniture):
#here we've defined how to implement the payment function from it's parent payslip class.
    def payment(self,amount):
        print('Your purchase amount of {} exceeds your $100 limit. Please pick a less expensive item. '.format(amount))
    
obj = DebitCardPayment()
obj.paySlip("$600")
obj.payment("$600")
