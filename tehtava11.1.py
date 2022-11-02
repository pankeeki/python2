class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}", end=', ')


class lehti(Julkaisu):
    def __init__(self, nimi, pt):
        self.pt = pt
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"päätoimittaja {self.pt}")


class kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumäärä):
        self.kirjailija = kirjailija
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"kirjailija {self.kirjailija}, sivumäärä {self.sivumäärä}")


julkaisut = []
julkaisut.append(lehti("Aku Ankka","Aki Hyyppä"))
julkaisut.append(kirja("Hytti nro 6", "Rosa Liksom", 200))
for i in julkaisut:
    i.tulosta_tiedot()