class Auto:
    def __init__(self, rekkari, hnopeus, atmnopeus, kuljettu):
        self.rekkari = rekkari
        self.hnopeus = hnopeus
        self.atmnopeus = atmnopeus
        self.kuljettu = kuljettu

auto1 = Auto("ABC-123", 142, 0, 0)
print(vars(auto1))