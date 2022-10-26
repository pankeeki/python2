class Auto:
    def __init__(self, rekkari, hnopeus, atmnopeus, kuljettu):
        self.rekkari = rekkari
        self.hnopeus = hnopeus
        self.atmnopeus = 0
        self.kuljettu = 0

    def huippunopeus(self):
        return self.hnopeus

    def kiihdytä(self, kiihdytys):
        self.atmnopeus = self.atmnopeus + kiihdytys
        if self.atmnopeus < 0:
            self.atmnopeus = 0
        elif self.atmnopeus > self.hnopeus:
            self.atmnopeus = self.hnopeus

    def kulje(self, aika):
        self.kuljettu = self.kuljettu + aika * self.atmnopeus

auto1 = Auto("ABC-123", 142, 0, 0)

print(vars(auto1))
auto1.kiihdytä(30)
print(vars(auto1))
auto1.kiihdytä(70)
print(vars(auto1))
auto1.kulje(1.5)
auto1.kiihdytä(50)
print(vars(auto1))
auto1.kiihdytä(-200)
print(auto1.atmnopeus)