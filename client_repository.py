from client import Client
from currency import Currency

class Repository():
    def __init__(self):
        self.clients = {}
        self.load_accounts_from_file()

    def find_client(self, login):
        return self.clients.get(login)

    def transfer_money(self, amount, login1, login2):
        login_from = self.find_client(login1)
        login_to = self.find_client(login2)
        if login_from is None or login_to is None or Repository.check_currency(amount) or Repository.check_difference(
                login_from, amount):
            print("Błędne dane!")
        else:
            login_from.substract_balance(amount)
            login_to.add_balance(amount)
            self.save_accounts_to_file()

    def load_accounts_from_file(self):
        try:
            with open("data.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    zl = data[0]
                    gr = data[1]
                    login = data[2]
                    print(data)
                    currency = Currency(int(zl), int(gr))
                    self.clients[login] = Client("", "", login, "", currency)
        except FileNotFoundError:
            print("Plik data.txt nie istnieje.")

    def save_accounts_to_file(self):
        with open("data.txt", "w") as file:
            for client in self.clients.values():
                file.write(f"{client.currency.zl},{client.currency.gr},{client.login}\n")

    @staticmethod
    def check_currency(currency):
        grosze = currency.convert_to_gr()
        return grosze < 0

    @staticmethod
    def check_difference(client, currency):
        return (client.currency.convert_to_gr() - currency.convert_to_gr()) < 0



