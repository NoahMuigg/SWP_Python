class list:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class doppeltVerketteteListe:
    def __init__(self):
        self.startelement = None

    def hintenAnfügen(self, Wert):
        if self.startelement is not None:
            aktuellePosotion = self.startelement
            while aktuellePosotion.next is not None:
                aktuellePosotion = aktuellePosotion.next
            
            Wert.prev = aktuellePosotion
            aktuellePosotion.next = Wert
        else:
            self.startelement = Wert
