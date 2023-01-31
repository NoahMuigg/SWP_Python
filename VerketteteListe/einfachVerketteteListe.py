class liste:
    def __init__(self, data):
        self.data = data
        self.next = None

class verketteteListe:
    def __init__(self):
        self.startElement = None
    
    def allesAusgeben(self):
        aktuelleListe = self.startElement
        while aktuelleListe is not None:
            print(aktuelleListe.data)
            aktuelleListe = aktuelleListe.next

    def elementHintenAnfügen(self, Wert):
        aktuelleListe = self.startElement
        while aktuelleListe.next is not None:
            aktuelleListe = aktuelleListe.next
        aktuelleListe.next = liste(Wert)
    
    # Fehler: Der Zähler erhöht sich nicht
    def längeListe(self):
        aktuelleListe = self.startElement
        zähler = 0
        while aktuelleListe is not None:
            zähler =+ 1
            aktuelleListe = aktuelleListe.next
        print("Die aktuelle Liste besitzt", zähler, "Elemente")
                

if __name__ == '__main__':
    vListe = verketteteListe()
    l1 = liste(1)
    l2 = liste(2)
    l3 = liste(3)

    vListe.startElement = l1

    l1.next = l2
    l2.next = l3

    # Händisches ausgeben von den einzelnen Elementen der verketteten Liste
    print("Hängisch ausgegeben + Händisch hinzugefügt")
    print(vListe.startElement.data)
    print(vListe.startElement.next.data)
    print(vListe.startElement.next.next.data)
    print()

    # Alle Elemente aus der verketteten Liste ausgeben
    print("Automatisch ausgegeben + Händisch hinzugefügt")
    vListe.allesAusgeben()
    print()

    # Element hinten hinzufügen
    print("Automatisch ausgegeben + Automatisch hinzugefügt")
    vListe.elementHintenAnfügen(4)
    vListe.allesAusgeben()
    print()

    # Länge der Liste ausgeben
    vListe.elementHintenAnfügen(5)
    vListe.längeListe()