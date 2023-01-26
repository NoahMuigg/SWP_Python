from random import randint as zufall
from flask import Flask
import json
from __init__ import create_app
from flask_restful import Api

app = create_app()
api = Api(app)

moeglichkeiten = ["Stein", "Papier", "Schere", "Spock", "Echse"]
ergebnis = {"Unentschieden" : 0, "Gewonnen" : 0, "Verloren" : 0,"Stein" :0
    , "Papier" :0, "Schere" :0, "Spock" :0, "Echse": 0}
dataFile = {}
g = [0, 0, 0, 0, 0]

def spiel():
    eingabe = input("Wähle Schere, Stein, Papier, Spock oder Echse:")
    ergebnis[eingabe] += 1
    indexEingabe = moeglichkeiten.index(eingabe)
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
    print("Du hat gewaehlt: " + eingabe)
    print(ergebnis)
    erneutSpielen()
    
        
def erneutSpielen():
    richtig = True
    while richtig == True:
        weiter = input("Wollen Sie weiter spielen? (J, N):")
        if weiter != "J" or "N":
            print("Falsche Eingabe")
        if weiter == "J":
            spiel()
            richtig = False
        if weiter == "N":
            home()
            richtig = False
    

def daten_aktualisieren():
    file = open("templates/stats.txt", "r")
    saved = file.read()
    if saved:
        save_json = json.loads(saved)
        combine(ergebnis, save_json)
    file.close()
    file = open("templates/stats.txt", "w")
    json.dump(dataFile, file)
    file.close()
    print("Daten wurden aktualisiert!!!\n")


def daten_loeschen():
    daten = {"Unentschieden" : 0, "Gewonnen" : 0, "Verloren" : 0,"Stein" :0
        , "Papier" :0, "Schere" :0, "Spock" :0, "Echse": 0}
    ergebnis = daten
    g = [0, 0, 0, 0, 0]
    file = open("templates/stats.txt", "w")
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



