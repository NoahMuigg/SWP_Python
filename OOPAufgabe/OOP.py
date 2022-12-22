class Personen:
    def __init__(self, vorname, nachname, alter, geschlecht, abteilung):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.geschlecht = geschlecht
        self.abteilung = abteilung

class Mitarbeiter(Personen):
    def __init__(self, vorname, nachname, alter, geschlecht, abteilung, firma):
        super(Mitarbeiter, self).__init__(vorname, nachname, alter, geschlecht, abteilung)
        self.firma = firma

class Gruppenleiter(Personen):
    def __init__(self, vorname, nachname, alter, geschlecht, abteilung, firma):
        super(Gruppenleiter, self).__init__(vorname, nachname, alter, geschlecht, abteilung)
        self.firma = firma

class Abteilung:
    def __init__(self, name):
        self.name = name

class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungenliste = []
        self.mitarbeiterliste = []
        self.gruppenleiterliste = []

    def anzMitarbeiter(self):
        return f'Anzahl der Mitarbeiter in der Firma {self.name}: {len(self.mitarbeiterliste)}'

    def anzGruppenleiter(self):
        return f'Anzahl der Gruppenleiter in der Firma {self.name}: {len(self.gruppenleiterliste)}'

    def anzAbteilungen(self):
        return f'Anzahl der Abteilungenin der Firma {self.name}: {len(self.abteilungenliste)}'

    def anteilGeschlechter(self):
        maenner = 0
        frauen = 0
        for i in self.mitarbeiterliste or self.gruppenleiterliste:
            if i.geschlecht == "m":
                maenner += 1
            elif i.geschlecht == "w":
                frauen += 1
        return f'Maenner: {(maenner / (maenner + frauen)) * 100}% Frauen: {(frauen / (maenner + frauen)) * 100}% sind in der Firma {self.name}'

    def grossteAbteilung(self):
        count = 0
        for i in self.abteilungenliste:
            for x in self.mitarbeiterliste and self.gruppenleiterliste:
                if x.abteilung == Abteilung or x.abteilung == Abteilung:
                    count += 1
        return f'Die größte Abteilung hat {count} Arbeiter'





def main():
    # Alle Firmen erzeugen
    firma1 = Firma("Swarovski")
    firma2 = Firma("Ja")

    # Alle Abteilungen erzeugen
    a1 = Abteilung("IT")
    a2 = Abteilung("Buchhaltung")
    a3 = Abteilung("Marketing")

    # Alle Gruppenleiter erzeugen
    gl1 = Gruppenleiter("Noah", "Muigg", 18, "m", a1, firma1)
    gl2 = Gruppenleiter("Josef", "Schallhart", 32, "m", a1, firma1)
    gl3 = Gruppenleiter("Niklas", "Muster", 33, "m", a2, firma1)
    gl4 = Gruppenleiter("Josefine", "Platzer", 55, "w", a1, firma1)

    # Alle Mitarbeiter erzeugen
    m1 = Mitarbeiter("Hermann", "Maier", 56, "m", a1, firma1)
    m2 = Mitarbeiter("Susanne", "Lustig", 60, "w", a1, firma1)
    m3 = Mitarbeiter("Susi", "Lappen", 40, "w", a2, firma1)
    m4 = Mitarbeiter("Herbert", "Bauer", 45, "m", a1, firma1)
    m5 = Mitarbeiter("Elisa", "Bauer", 20, "w", a2, firma1)
    m5 = Mitarbeiter("Elisa", "Bauer", 20, "w", a2, firma1)


    # Alle Objekte der richtigen Liste hinzufügen
    firma1.abteilungenliste.append(a1)
    firma1.gruppenleiterliste.append(gl1)
    firma1.mitarbeiterliste.append(m1)
    firma1.mitarbeiterliste.append(m2)
    firma1.mitarbeiterliste.append(m3)
    firma1.mitarbeiterliste.append(m4)
    firma1.mitarbeiterliste.append(m5)
    firma1.gruppenleiterliste.append(gl2)
    firma1.gruppenleiterliste.append(gl3)
    firma1.gruppenleiterliste.append(gl4)
    firma1.abteilungenliste.append(a2)
    firma1.abteilungenliste.append(a3)


    # Ausgaben
    print(firma1.anzMitarbeiter())
    print(firma1.anzGruppenleiter())
    print(firma1.anzAbteilungen())
    print(firma1.anteilGeschlechter())
    print(firma1.grossteAbteilung())


if __name__ == '__main__':
    main()


