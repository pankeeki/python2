class Auto:
    kuljettu = 0
    atmnopeus = 0

    def __init__(self, rekkari, hnopeus, atmnopeus, kuljettu):
        self.rekkari = rekkari
        self.hnopeus = hnopeus
        self.atmnopeus = atmnopeus
        self.kuljettu = kuljettu

    def huippunopeus(self):
        return self.hnopeus

    def kiihdytä(self, kiihdytys):
        self.atmnopeus = self.atmnopeus + kiihdytys
        if self.atmnopeus < 0:
            self.atmnopeus = 0
        elif self.atmnopeus > self.hnopeus:
            self.atmnopeus = self.hnopeus


auto1 = Auto("ABC-123", 142, 0, 0)
print(vars(auto1))
auto1.kiihdytä(30)
print(auto1.atmnopeus)
auto1.kiihdytä(70)
print(auto1.atmnopeus)
auto1.kiihdytä(50)
print(auto1.atmnopeus)
auto1.kiihdytä(-200)
print(auto1.atmnopeus)
