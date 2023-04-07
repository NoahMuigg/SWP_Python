import random

class arrayList:
    def __init__(self):
        self.data = []

    # Mit dieser Methode kann man einen Wert am Ende des Arrays hinzufügen 
    def hintenHinzufügen(self, value):
        self.data = self.elemBeliebigEinfügen(self.data, value)

    # Die Länge der Liste wird ausgegeben
    def längeListe(self):
        return self.getlength(self.data)

    # Die ganze Liste wird ausgegeben
    def allesAusgeben(self):
        self.printelements(self.data)

    # Mit dieser Methode kann man einen Wert auf eine beliebige Position in der Liste hinzufügen 
    def elemBeliebigEinfügen(self, lst, value):
        l = []
        for element in lst:
            l.append(element)
        l.append(value)
        return l

    def sum(self, lst):
        summe = 0
        for e in lst:
            summe += lst[e]
        return summe

    def getlength(self, lst):
        count = 0
        for element in lst:
            count += 1
        return count

    
    def printelements(self, lst):
        for element in lst:
            print(element)



if __name__ == "__main__":
    l = arrayList()
    for i in range(10):
        l.hintenHinzufügen(random.randint(1, 100))
    print("Länge des Arrays:", l.längeListe())
    print("Folgende Elemente befinden sich in dem Array:")
    l.allesAusgeben()