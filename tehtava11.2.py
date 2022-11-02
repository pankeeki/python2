from auto2 import Auto
import random


class Sähköauto(Auto):
    def __init__(self, rekkari, hnopeus, akku):
        self.akku = akku
        super().__init__(rekkari, hnopeus)


class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, hnopeus, tankki):
        self.tankki = tankki
        super().__init__(rekkari, hnopeus)

autot = []
autot.append(Sähköauto("ABC-15", 180, 52.5))
autot.append(Polttomoottoriauto("ACD-123", 165, 32.3))
for i in autot:
    i.kiihdytä(random.randint(10,200))
    i.kulje(3)
    print(f"{i.rekkari} on ajanut {i.kuljettu} km vauhdilla {i.atmnopeus} km/h.")