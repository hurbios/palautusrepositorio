KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                return True
        return False

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_lista(self.ljono, taulukko_old)
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)

            return True

        return False

    def poista(self, n):
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                self.ljono[i] = 0

                for j in range(i, self.alkioiden_lkm - 1):
                    apu = self.ljono[j]
                    self.ljono[j] = self.ljono[j + 1]
                    self.ljono[j + 1] = apu

                self.alkioiden_lkm = self.alkioiden_lkm - 1
                return True
        return False

    def kopioi_lista(self, a, b):
        for i, a_item in enumerate(a):
            b[i] = a_item

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        taulut = a.to_int_list() + b.to_int_list()
        for item in taulut:
            x.lisaa(item)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        b_taulu = b.to_int_list()
        for item in filter(lambda x: x in b_taulu, a.to_int_list()):
            y.lisaa(item)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()

        for item in a.to_int_list():
            z.lisaa(item)

        for item in b.to_int_list():
            z.poista(item)

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
