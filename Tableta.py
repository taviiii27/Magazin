from  Magazin import Produs
class Tableta(Produs):
    def __init__(self, id, produs, tip, an, pret, stoc, capacitateAplicatiiBirou):
        super().__init__(id, produs, tip, an, pret, stoc)
        self.capacitateAplicatiiBirou=capacitateAplicatiiBirou
    def folosire(self):
        for self.id in Tableta:
            if self.stoc=='disponibil':
                if self.capacitateAplicatiiBirou=='restransa':
                    return f'este nevoie si de un laptop pentru a va face treaba'
                else:
                    return f'{self.produs} este o tableta potrivita pentru munca, un device mobil ideal pentru job!'
    def inlocuiri(self):
        self.pretNou=self.pret+230
        for self.id in Tableta:
            if self.capacitateAplicatiiBirou=='extinsa peste functionalitati normale':
                self.pret=self.pretNou
                return self.pret
            else:
                return f'pretul ramane acelasi{self.pret}'

