import random


class list:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class doppeltVerketteteListe:
    def __init__(self):
        self.startElement = None
        self.endElement = None


    # Mit dieser Methode kann man einen Wert am Ende der Liste hinzufügen 
    def elementHintenAnfügen(self, Wert):
        if self.startElement is None:
            self.startElement = list(Wert)
        if self.startElement is not None:
            aktuellePosition = self.startElement
            while aktuellePosition.next is not None:
                aktuellePosition = aktuellePosition.next
            aktuellePosition.prev = aktuellePosition
            aktuellePosition.next = list(Wert)
        else:
            self.startElement = Wert

    
    # Die ganze Liste wird ausgegeben
    def allesAusgeben(self):
        aktuellePosition = self.startElement
        while aktuellePosition is not None:
            print(aktuellePosition.data)
            aktuellePosition = aktuellePosition.next 

        aktuellePosition = self.endElement
        while aktuellePosition is not None:
            print(aktuellePosition.data)
            aktuellePosition = aktuellePosition.prev


    # Die Länge der Liste wird ausgegeben
    def längeListe(self):
        aktuelleListe = self.startElement
        zähler = 0
        while aktuelleListe is not None:
            zähler += 1
            aktuelleListe = aktuelleListe.next
        print("Die aktuelle Liste besitzt", zähler, "Elemente")
    

    # Die Werte der Liste werden zusammengezählt und ausgegeben
    def sum(self):
        summe = 0
        aktuelleListe = self.startElement
        while aktuelleListe is not None:
            summe += aktuelleListe.data
            aktuelleListe = aktuelleListe.next
        print("Die Summe der aktuellen Liste beträgt:", summe)

    
    # Mit dieser Methode kann man einen Wert auf eine beliebige Position in der Liste hinzufügen 
    def elemBeliebigEinfügen(self, Wert, Position):
        elemNeu = list(Wert)
        aktuelleListe = self.startElement
        zähler = 1
        intPosition = int(Position)
        while aktuelleListe.next is not None and zähler <= intPosition-1:
            aktuelleListe = aktuelleListe.next
            zähler += 1
        if Position == 1:
            elemNeu.next = aktuelleListe
            aktuelleListe.previous = elemNeu
            self.startElement = elemNeu
        else:
            elemNeu.next = aktuelleListe.next
            if aktuelleListe.next is not None:
                aktuelleListe.next.previous = elemNeu
            aktuelleListe.next = elemNeu
            elemNeu.previous = aktuelleListe
    

    # Methoden zum Einfügen von Elementen und zum Erstellen der Liste...
    def elemLöschen(self, Position):
        aktuelleListe = self.startElement
        zähler = 1
        intPosition = int(Position)
        while aktuelleListe is not None and zähler < intPosition:
            aktuelleListe = aktuelleListe.next
            zähler += 1
        if aktuelleListe is None:
            return
        if aktuelleListe == self.startElement:
            self.startElement = aktuelleListe.next
        if aktuelleListe.next is not None:
            aktuelleListe.next.previous = aktuelleListe.previous
        if aktuelleListe.previous is not None:
            aktuelleListe.previous.next = aktuelleListe.next
        del aktuelleListe


def home():
    vListe = doppeltVerketteteListe()
    for i in range(10):
        i = random.randint(0,100)
        vListe.elementHintenAnfügen(i)
    los = True
    while los == True:
        eingabe = input("Was möchten Sie machen? Sie können auswählen zwischen: " 
        "\nGesamte Liste ausgeben (ausgabe) \neinen Wert am Ende der Liste anfügen (hinten) "
        "\nlänge der Liste (l) \nSumme der Werte (s) \neinen Wert an einer beliebigen Position einfügen (beliebig)" 
        "\nElement löschen (löschen)\nverlassen (v): ")
        if eingabe == "ausgabe":
            vListe.allesAusgeben()
            print()
        if eingabe == "hinten":
            a = input("Bitte geben Sie einen Wert ein:")
            vListe.elementHintenAnfügen(a)
            print()
        if eingabe == "l":
            vListe.längeListe()
            print()
        if eingabe == "s":
            vListe.sum()
            print()
        if eingabe == "beliebig":
            a = input("Bitte geben Sie einen Wert ein:")
            b = input("Bitte geben Sie einen Position, an welcher der gewünschte Wert eingefügt werden soll: ")
            vListe.elemBeliebigEinfügen(a,b)
            print()
        if eingabe == "v":
            exit()
        if eingabe == "löschen":
            a = input("Bitte eine Position eingeben, welche Sie löschen wollen: ")
            vListe.elemLöschen(a)
            print()




if __name__ == '__main__':
    home()


