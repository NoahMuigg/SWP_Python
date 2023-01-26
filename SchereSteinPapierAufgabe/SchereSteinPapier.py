from random import randint as zufall
from flask import Flask
import json
from website import create_app
from flask_restful import Api
import matplotlib.pyplot as plt

app = create_app()
api = Api(app)

moeglichkeiten = ["Stein", "Papier", "Schere", "Spock", "Echse"]
ergebnis = {"Unentschieden" : 0, "Gewonnen" : 0, "Verloren" : 0,"Stein" :0
    , "Papier" :0, "Schere" :0, "Spock" :0, "Echse": 0}
statsfürGamemode = {"Stein" :0, "Papier" :0, "Schere" :0, "Spock" :0, "Echse": 0} 
dataFile = {}
g = [0, 0, 0, 0, 0]
computerHard = 0

def spiel():
    auswahl = input("Wähle einen Spielmodus aus: Hard oder Normal")
    eingabe = input("Wähle Schere, Stein, Papier, Spock oder Echse:")
    ergebnis[eingabe] += 1
    statsfürGamemode[eingabe] += 1
    indexEingabe = moeglichkeiten.index(eingabe)
    if auswahl == "Normal":
        if eingabe in moeglichkeiten:
            computer = zufall(0,4)
            if (indexEingabe + 2) > 4:
                indexEingabe -= 5
            if indexEingabe == computer:
                print("Unentschieden")
                ergebnis["Unentschieden"] += 1
            if moeglichkeiten[computer] == moeglichkeiten[indexEingabe+2] \
                    or moeglichkeiten[computer] == moeglichkeiten[indexEingabe-1]:
                print("Gewonnen")
                ergebnis["Gewonnen"] += 1
            if moeglichkeiten[computer] == moeglichkeiten[indexEingabe-2] \
                    or moeglichkeiten[computer] == moeglichkeiten[indexEingabe+1]:
                print("Verloren")
                ergebnis["Verloren"] += 1

        print("Computer hat gewaehlt: " + moeglichkeiten[computer])

    elif auswahl == "Hard":
        häufigstets = max(statsfürGamemode, key=statsfürGamemode.get)
        if häufigstets == "Stein":
            computerHard = 1
        elif häufigstets == "Papier":
            computerHard = 2
        elif häufigstets == "Schere":
            computerHard = 3
        elif häufigstets == "Spock":
            computerHard = 4
        else:
            computerHard = 0

        if eingabe in moeglichkeiten:
            if (indexEingabe + 2) > 4:
                indexEingabe -= 5
            if indexEingabe == computerHard:
                print("Unentschieden")
                ergebnis["Unentschieden"] += 1
            if moeglichkeiten[computerHard] == moeglichkeiten[indexEingabe+2] \
                    or moeglichkeiten[computerHard] == moeglichkeiten[indexEingabe-1]:
                print("Gewonnen")
                ergebnis["Gewonnen"] += 1
            if moeglichkeiten[computerHard] == moeglichkeiten[indexEingabe-2] \
                    or moeglichkeiten[computerHard] == moeglichkeiten[indexEingabe+1]:
                print("Verloren")
                ergebnis["Verloren"] += 1
        print("Computer hat gewaehlt: " + moeglichkeiten[computerHard])
        
    print("Du hast gewaehlt: " + eingabe)
    print(ergebnis)
    erneutSpielen()
    
        
def erneutSpielen():
    richtig = True
    while richtig == True:
        weiter = input("Wollen Sie weiter spielen? (J, N):")
        if weiter == "J":
            spiel()
            richtig = False
        elif weiter == "N":
            home()
            richtig = False
        else:
            print("Falsche Eingabe")
    

def daten_aktualisieren():
    file = open("website/data/stats.txt", "r")
    saved = file.read()
    if saved:
        save_json = json.loads(saved)
        combine(ergebnis, save_json)
    file.close()
    file = open("website/data/stats.txt", "w")
    json.dump(dataFile, file)
    file.close()
    print("Daten wurden aktualisiert!!!\n")


def daten_loeschen():
    daten = {"Unentschieden" : 0, "Gewonnen" : 0, "Verloren" : 0,"Stein" :0
        , "Papier" :0, "Schere" :0, "Spock" :0, "Echse": 0}
    ergebnis = daten
    g = [0, 0, 0, 0, 0]
    file = open("website/data/stats.txt", "w")
    json.dump(daten, file)
    file.close()
    print("Daten wurden gelöscht!!!\n")

def combine(a, b):
    for i in a:
        dataFile[i] = a[i] + b[i]
    return a

def home(): 
    los = True
    while los == True:
        wahlen = input("Waehlen Sie aus zwischen: spiel, stats, speichern, loeschen oder exit: ")
        if wahlen == "spiel":
            spiel()
        elif wahlen == "stats":
            print(dataFile)
            print()
        elif wahlen == "speichern":
            daten_aktualisieren()
        elif wahlen == "loschen":
            daten_loeschen()
        elif wahlen == "exit":
            exit()
    
if __name__ == "__main__":
    home()
    spiel()



