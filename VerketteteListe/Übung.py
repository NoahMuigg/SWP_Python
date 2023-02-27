import random 

class liste:
    def __init__(self, data):
        self.data = data
        self.next = None

class verketteteListe:
    def __init__(self):
        self.startElem = None
     
    def ausgabe(self):
        aktuellesElem = self.startElem
        while aktuellesElem is not None:
            print(aktuellesElem.data)
            aktuellesElem = aktuellesElem.next

    def länge(self):
        aktuellesElem = self.startElem
        counter = 0
        while aktuellesElem is not None:
            counter += 1
            aktuellesElem = aktuellesElem.next
        print(counter)
    
    def anhängen(self, elem):
        if self.startElem is None:
            self.startElem = liste(elem)
        else:
            aktuellesElem = self.startElem
            while aktuellesElem.next is not None:
                aktuellesElem = aktuellesElem.next
            aktuellesElem.next = liste(elem)
    
    def add(self, elem, position):
        pos = position - 1
        aktuellesElem = self.startElem
        zähler = 0
        neuesElem = liste(elem)
        while aktuellesElem is not None and zähler <= pos:
            zähler += 1
            aktuellesElem = aktuellesElem.next
        if pos == 0:
            self.startElem = neuesElem
            aktuellesElem.next = aktuellesElem
        else:
            neuesElem.next = aktuellesElem.next
            aktuellesElem.next = neuesElem

            
if __name__ == '__main__':
    l = verketteteListe()
    for i in range(10):
        a = random.randint(0,100)
        l.anhängen(a)
    
    
    #l.länge()
    l.anhängen(99)

    l.add(100,0)
    l.ausgabe()

