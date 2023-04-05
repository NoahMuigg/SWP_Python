class list:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class doppeltVerketteteListe:
    def __init__(self):
        self.startelement = None


    # Mit dieser Methode kann man einen Wert am Ende der Liste hinzufügen 
    def hintenAnfügen(self, Wert):
        if self.startelement is not None:
            aktuellePosition = self.startelement
            while aktuellePosition.next is not None:
                aktuellePosition = aktuellePosition.next
            
            Wert.prev = aktuellePosition
            aktuellePosition.next = Wert
        else:
            self.startelement = Wert

    
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
    





