from hissi import Hissi


class Talo:
    def __init__(self, alin, ylin, hissiluku):
        self.alin = alin
        self.ylin = ylin
        self.hissiluku = hissiluku
        self.hissilista = []
        for i in range(0, hissiluku):
            self.hissilista.append(Hissi(alin, ylin, 0))

    def aja_hissia(self, hissiluku, tavoite):
        self.hissilista[hissiluku - 1].siirry_kerrokseen(tavoite)

talo1 = Talo(0,12,2)
talo1.aja_hissia(2, 11)