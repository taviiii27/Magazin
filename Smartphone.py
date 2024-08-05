from Magazin import Produs
class Smartphone(Produs):
    def __init__(self, id, produs, tip, an, pret, stoc, culoare):
        super().__init__(id, produs, tip, an, pret, stoc)
        self.culoare=culoare
    def comercializare(self):
        for self.id in Smartphone:
            if self.stoc=='disponibil':
                if self.pret==4500 and self.culoare=='albastru':
                    return f'telefonul {self.produs} este unul premium, special pentru baieti'
                else: 
                    return f'telefonul {self.produs} este unul premium, dar fie pentru fete fie unisex'
            else:
                return f'reumpleti stocul {self.stoc}'
    def update(self):
        for self.id in Smartphone:
            electroniceVechi=[]
            electroniceNoi=[]
            if self.an<2017:
                self.produs.append(electroniceVechi)
            elif self.an>2021:
                self.produs.append(electroniceNoi)
            else:
                return f'smartphone-urile nu sunt nici vechi nici noi'
    