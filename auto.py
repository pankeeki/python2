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
        autot.append(Auto(f"ABC-{i+1}", random.uniform(100, 200)))

    while (True):
        for auto in autot:
            auto.kiihdytä(random.uniform(-10, 15))
            auto.kulje(1)
        for auto in autot:
            if auto.getkuljettu() >= 1000:
                return autot



for auto in kisa():
    print(f'{auto.rekkari}, {auto.hnopeus:.2f} km/h huippunopeus, {auto.atmnopeus:.2f} km/h nykyinen nopeus, {auto.kuljettu:.2f} km ajettu')