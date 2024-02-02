
class Currency():

    def __init__(self, zl=0, gr=0):
        self.zl = zl
        self.gr = gr

    def __add__(self, other):
        add = self.convert_to_gr() + other.convert_to_gr()
        return Currency.zl_gr(add)

    def __sub__(self, other):
        sub = self.convert_to_gr() - other.convert_to_gr()
        return Currency.zl_gr(sub)

    def __str__(self):
        return f"{self.zl}zł, {self.gr} gr"

    def __gt__(self, other):
        return self.convert_to_gr() > other.convert_to_gr()

    @staticmethod
    def string_to_currency(string):
        zl_gr_lista = string.strip().split(",")
        zl = int(zl_gr_lista[0])
        gr = int(zl_gr_lista[1])
        if gr > 99:
            raise ValueError("Za duza liczba groszy!")
        return Currency(zl, gr)

    @staticmethod
    def zl_gr(gr):
        zloty = gr // 100
        grosze = gr % 100
        return Currency(zloty, grosze)

    def convert_to_zl(self):
        return self.gr * 0.1 + self.zl

    def convert_to_gr(self):
        return self.zl * 100 + self.gr


