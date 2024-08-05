from Magazin import Produs
class Laptop(Produs):
    def __init__(self, id, produs, tip, an, pret, stoc, memorie):
        super().__init__(id, produs, tip, an, pret, stoc)
        self.memorie=memorie
    def interes(self):
        if self.memorie>=256:
            if self.client=='gamer' or self.client=='programator':
                return f'laptop ideal'
            else:
                return f'{self.pret} poate fi prea scump si {self.memorie} nenecesar de mare'
    def instalare(self):
        if self.client=='gamer':
            return f'trb avut grija sa nu se umple memoria prea repede cu jouri inutile'
        elif self.client=='programator':
            return f'ideal, laptopul poate fi folosit intens pt acest scop'
        else:
            return f'v as recomanda alt laptop'
    