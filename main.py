from currency import Currency
from client_repository import Repository

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

class AccountManager(QWidget):
    def __init__(self):
        super().__init__()
        #  user powinien byc ustawiany po zalogowaniu
        #  user powinien byc z logowania ustawiany, jest teraz zahardkodowany i zawsze bedzie userem o loginie 111
        self.username = "111"
        self.client_repository = Repository()
        self.logged = self.client_repository.find_client("111")
        #print(self.logged)
        self.init_ui()

    #  metoda do wstawienia gui, uzyta w init:
    def init_ui(self):
        #  layout gora -> dol
        self.layout = QVBoxLayout(self)
        #  odpowiednie widzety
        self.label_balance1 = QLabel("Balance1")

        self.edit_ammount = QLineEdit(self)
        self.edit_ammount.setPlaceholderText("Podaj kwote (np 100,00 zl):")
        self.edit_client = QLineEdit(self)
        self.edit_client.setPlaceholderText("Podaj konto:")

        self.btn_transfer = QPushButton("Wyslij",self)
        #  Podpinamy przycisk pod metodę do transferu, ktora napiszemy
        self.btn_transfer.clicked.connect(self.transfer)

        #  dodajemy widzety
        self.layout.addWidget(self.label_balance1)
        self.layout.addWidget(self.edit_ammount)
        self.layout.addWidget(self.edit_client)
        self.layout.addWidget(self.btn_transfer)

        self.setWindowTitle("Account manager")

        self.update_balance_label()

    #  metoda do logiki po przycisnieciu przycisku
    def transfer(self):
        amount_str = self.edit_ammount.text()
        to_account = self.edit_client.text()
        amount = Currency.string_to_currency(amount_str)
        from_account = self.logged.login
        self.client_repository.transfer_money(amount, from_account, to_account)

        self.update_balance_label();
        self.edit_ammount.clear();
        self.edit_client.clear();

    #  update srodkow na koncie po dodaniu usera i kliknieciu przycisku
    def update_balance_label(self):
        balance1 = self.logged.currency
        balance2 = " "
        client2 = self.client_repository.find_client(self.edit_client.text())
        if client2:
            balance2 = client2.currency
        self.label_balance1.setText(f"My account balance: {balance2}")
        self.label_balance1.setText(f"My account balance: {balance1}")

#  odpalamy aplikacje
if __name__ == '__main__':
    app = QApplication([])
    main_window = AccountManager()
    main_window.show()
    app.exec()


