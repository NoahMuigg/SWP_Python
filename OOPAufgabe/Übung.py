class auto:
    def __init__(self, Marke, Modell, Baujahr, Geschwindigkeit):
        self.Marke = Marke
        self.Modell = Modell
        self.Baujahr = Baujahr
        self.Geschwindigkeit = Geschwindigkeit
    
    def beschleunigen(self):
        self.Geschwindigkeit += 10
        print(self.Geschwindigkeit)
    
    def bremsen(self):
        self.Geschwindigkeit -= 10
        print(self.Geschwindigkeit)
    
class lkw(auto):
    def __init__(self, Marke, Modell, Baujahr, Geschwindigkeit, ladeKapa):
        super().__init__(Marke, Modell, Baujahr, Geschwindigkeit)
        self.ladeKapa = ladeKapa

class pkw(auto):
    def __init__(self, Marke, Modell, Baujahr, Geschwindigkeit, anzTüren):
        super().__init__(Marke, Modell, Baujahr, Geschwindigkeit)
        self.anzTüren = anzTüren


if __name__ == '__main__':
    p1 = pkw("Audi", "A6", 2020, 100, 4)
    l1 = lkw("asdf", "Ahjg", 2010, 60, 400)

    p1.beschleunigen()
    l1.bremsen()


