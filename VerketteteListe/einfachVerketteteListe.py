import random 

class liste:
    def __init__(self, data):
        self.data = data
        self.next = None

class verketteteListe:
    def __init__(self):
        self.startElement = None
    
    # Die ganze Liste wird ausgegeben
    def allesAusgeben(self):
        aktuelleListe = self.startElement
        while aktuelleListe is not None:
            print(aktuelleListe.data)
            aktuelleListe = aktuelleListe.next

    # Mit dieser Methode kann man einen Wert am Ende der Liste hinzufügen 
    def elementHintenAnfügen(self, Wert):
        if self.startElement is None:
            self.startElement = liste(Wert)
        else:
            aktuelleListe = self.startElement
            while aktuelleListe.next is not None:
                aktuelleListe = aktuelleListe.next
            aktuelleListe.next = liste(Wert)

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
        aktuelleListe = self.startElement
        summe = 0
        while aktuelleListe is not None:
            summe += aktuelleListe.data
            aktuelleListe = aktuelleListe.next
        print("Die Summe der aktuellen Liste beträgt:", summe)
    
    # Mit dieser Methode kann man einen Wert auf eine beliebige Position in der Liste hinzufügen 
    def elemBeliebigEinfügen(self, Wert, Position):
        elemNeu = liste(Wert)
        aktuelleListe = self.startElement
        zähler = 1
        intPosition = int(Position)
        while aktuelleListe.next is not None and zähler <= intPosition-1:
            aktuelleListe = aktuelleListe.next
            zähler += 1
        if Position == 1:
            elemNeu.next = aktuelleListe
            self.startElement = elemNeu
        else:
            elemNeu.next = aktuelleListe.next
            aktuelleListe.next = elemNeu
    
    # Mit dieser Methode kann man ein belibieges Element aus der Liste löschen
    def elemLöschen(self, Position):
        aktuelleListe = self.startElement
        zähler = 1
        vorher = None
        intPosition = int(Position)
        while aktuelleListe.next is not None and zähler <= intPosition-1:
            vorher = aktuelleListe
            aktuelleListe = aktuelleListe.next
            zähler += 1
        if Position == 1:
            self.startElement = aktuelleListe.next
            del aktuelleListe
        else:
            vorher.next = aktuelleListe.next
            del aktuelleListe



def home():
    vListe = verketteteListe()
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