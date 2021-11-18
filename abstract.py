from abc import ABC, abstractmethod
class bank(ABC):
    @abstractmethod
    def loan(self):
        pass
    @abstractmethod
    def credit(self):
        pass
    @abstractmethod
    def debit(self):
        pass
class hdfc(bank):
    def loan(self):
        print("hdfc loan available")
    def credit(self):
        print("hdfc credit available")
    def debit(self):
        print("hdfc debit available")
    def card(self):
        print("hdfc card available")
hdfc = hdfc()
hdfc.loan()
hdfc.credit()
hdfc.debit()
hdfc.card()