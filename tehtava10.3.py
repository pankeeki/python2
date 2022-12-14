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
        self.hissilista[hissiluku].siirry_kerrokseen(tavoite)

    def palohalytys(self):
        for i in range(0, len(self.hissilista)):
            self.aja_hissia(i, 0)

talo1 = Talo(0,12,2)
talo1.palohalytys()