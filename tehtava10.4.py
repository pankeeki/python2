from auto import Auto, kisa, auto


class Kilpailu:
    def __init__(self, nimi, kilsat, autolista):
        self.nimi = nimi
        self.kilsat = kilsat
        self.autolista = []

    def tunti_kuluu(self, Auto):
        for Auto in self.autolista:
            Auto.kiihdytä()
            Auto.kulje()

    def tulosta_tilanne(self):
        for auto in self.autolista:
            print(vars(auto))

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.getkuljettu >= 1000:
                return True
            else:
                return False



lista_autoista = Auto.kisa()
Romuralli = Kilpailu("Suuri romuralli", 8000, lista_autoista)