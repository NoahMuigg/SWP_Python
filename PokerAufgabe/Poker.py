import random

versuche = 100000
handZahlen = []
handSymbole = []

def zahlen(nummer):
    nummer %= 13
    return nummer

def symbole(nummer):
    nummer %= 4
    if nummer == 0:
        return "Herz"
    if nummer == 1:
        return "Kreuz"
    if nummer == 2:
        return "Karo"
    if nummer == 3:
        return "Pik"



def getKarten(min, max):
    karten = []
    for x in range(min, max + 1):
        karten.append(x)
    for j in range(5):
        zufallsindex = random.randrange(0, max - min + 1)
        letzte = len(karten) - 1 - j
        karten[zufallsindex], karten[letzte] = karten[letzte], karten[zufallsindex]
    return karten[-5:]


def isteseinPaar(zahl):
    dublikat_Zahlen = [nummer for nummer in zahl if zahl.count(nummer) > 1]
    dublikate = list(set(dublikat_Zahlen))
    return len(dublikat_Zahlen), dublikate

statistik = {"Royal Flush": 0, "Straight Flush": 0, "Vierling": 0, "Full House": 0, "Flush": 0, "Straße": 0,
             "Drilling": 0, "Zwei Paare": 0, "Paar": 0, "Highest Card": 0}

def flushes(symbol, zahl):
    if symbol.count(symbol[0]) == len(symbol):
        symbol.sort()
        if zahl[0] == zahl[-1] - 4 and zahl[-1] == 12:
            statistik["Royal Flush"] += 1
        elif zahl[0] == zahl[-1] - 4:
            statistik["Straight Flush"] += 1
        else:
            statistik["Flush"] += 1

def vierling(zahl):
    if isteseinPaar(zahl)[0] == 4 and len(isteseinPaar(zahl)[1]) == 1:
        statistik["Vierling"] += 1


def fullHouse(zahl):
    if isteseinPaar(zahl)[0] == 5 and len(isteseinPaar(zahl)[1]) == 2:
        statistik["Full House"] += 1

def strasse(zahl):
    zahl.sort()
    if zahl[0] == zahl[-1] - 4 and len(isteseinPaar(zahl)[1]) == 0:
        statistik["Straße"] += 1

def drilling(zahl):
    if isteseinPaar(zahl)[0] == 3:
        statistik["Drilling"] += 1


def zweiPaare(zahl):
    if isteseinPaar(zahl)[0] == 4 and len(isteseinPaar(zahl)[1]) == 2:
        statistik["Zwei Paare"] += 1


def paar(zahl):
    if isteseinPaar(zahl)[0] == 2:
        statistik["Paar"] += 1


def highCard():
        hoheKarte = versuche - statistik["Royal Flush"] - statistik["Straight Flush"] - statistik["Flush"] - statistik["Vierling"] - \
                               statistik["Full House"] - statistik["Drilling"] - statistik["Zwei Paare"] - statistik["Paar"] - statistik["Straße"]
        statistik["Highest Card"] = statistik["Highest Card"] + hoheKarte


def main():
    global handZahlen, handSymbole
    for x in range(versuche):
        meineKarten = getKarten(1, 52)
        for i in meineKarten:
            handZahlen.append(zahlen(i))
            handSymbole.append(symbole(i))
        flushes(handSymbole, handZahlen)
        vierling(handZahlen)
        drilling(handZahlen)
        strasse(handZahlen)
        paar(handZahlen)
        zweiPaare(handZahlen)
        fullHouse(handZahlen)
        handZahlen = []
        handSymbole = []

    highCard()
    prozent = []
    for i in statistik:
        a = statistik[i] / versuche * 100
        a = round(a, 5)
        prozent.append(a)
    print(prozent)
    print(statistik)


if __name__ == "__main__":
    main()


