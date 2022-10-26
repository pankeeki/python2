import random

class Auto:
    def __init__(self, rekkari, hnopeus):
        self.rekkari = rekkari
        self.hnopeus = hnopeus
        self.atmnopeus = 0
        self.kuljettu = 0

    def huippunopeus(self):
        return self.hnopeus

    def getkuljettu(self):
        return self.kuljettu

    def getatmnopeus(self):
        return self.atmnopeus

    def kiihdytä(self, kiihdytys):
        self.atmnopeus = self.atmnopeus + kiihdytys
        if self.atmnopeus < 0:
            self.atmnopeus = 0
        elif self.atmnopeus > self.hnopeus:
            self.atmnopeus = self.hnopeus

    def kulje(self, aika):
        self.kuljettu = self.kuljettu + aika * self.atmnopeus

def kisa():
    autot = []
    for i in range(0,10):
        autot.append(Auto(f"ABC.{i+1}", random.uniform(100, 200)))

    while (True):
        for auto in autot:
            auto.kiihdytä(random.uniform(-10, 15))
            auto.kulje(1)
        for auto in autot:
            if auto.getkuljettu() >= 1000:
                return autot

auto1 = Auto("ABC-123", 142)
print(vars(auto1))
auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
print(auto1.getatmnopeus())

for auto in kisa():
    print(vars(auto))