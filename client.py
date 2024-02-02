from currency import Currency

class Client():

    def __init__(self, name, surname, login, password, currency=None):
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        if currency:
            self.currency = currency
        else:
            self.currency = Currency(0,0)

    def substract_balance(self, currency):
        self.currency = self.currency - currency

    def add_balance(self, currency):
         self.currency = self.currency + currency

    def __str__(self):
        return f"{self.name} {self.surname} {self.currency}"

    def __repr__(self):
        return f"{self.name} {self.surname} {self.currency}"













































































































