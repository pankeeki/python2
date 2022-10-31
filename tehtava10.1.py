class Hissi:
    def __init__(self, alin, ylin, kerros):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylos(self):
        self.kerros += 1
        print(f"Kerros {self.kerros}.")
    def kerros_alas(self):
        self.kerros -= 1
        print(f"Kerros {self.kerros}.")

    def siirry_kerrokseen(self, tavoite):
        if tavoite > self.ylin:
            print("Liian korkea, yritä uudestaan.")
        elif tavoite < self.alin:
            print("Liian matala, yritä uudestaan.")
        else:
            while tavoite != self.kerros:
                if tavoite > self.kerros:
                    self.kerros_ylos()
                else:
                    self.kerros_alas()
            print("Perille päästy.")

h = Hissi(0, 15, 0)
h.siirry_kerrokseen(6)
h.siirry_kerrokseen(h.alin)