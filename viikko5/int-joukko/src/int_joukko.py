class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_joukko(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.joukko = self._luo_joukko(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return self.joukko.count(n) > 0

    def lisaa(self, n):
        if not self.kuuluu(n):
            if self.alkioiden_lkm == self.kapasiteetti:
                # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
                self.kasvata_joukkoa()

            self.joukko[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            return True

        return False

    def kasvata_joukkoa(self):
        self.kapasiteetti = self.kapasiteetti + self.kasvatuskoko
        kasvatettu_joukko = self._luo_joukko(self.kapasiteetti)
        self.kopioi_lista(self.joukko, kasvatettu_joukko)
        self.joukko = kasvatettu_joukko

    def poista(self, n):
        if self.kuuluu(n):
            self.joukko.remove(n)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_lista(self, kopioitava, kohde):
        for i in range(0, len(kopioitava)):
            kohde[i] = kopioitava[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        lista = self._luo_joukko(self.alkioiden_lkm)

        for i in range(0, len(lista)):
            lista[i] = self.joukko[i]

        return lista

    @staticmethod
    def yhdiste(pohjajoukko, lisajoukko):
        yhdistejoukko = IntJoukko(pohjajoukko.mahtavuus() + lisajoukko.mahtavuus())
        pohjalista = pohjajoukko.to_int_list()
        lisattavat = lisajoukko.to_int_list()

        pohjalista.extend(lisattavat)

        for i in range(0, len(pohjalista)):
            yhdistejoukko.lisaa(pohjalista[i])

        return yhdistejoukko

    @staticmethod
    def leikkaus(a, b):
        leikkausjoukko = IntJoukko()
        a_lista = a.to_int_list()
        b_lista = b.to_int_list()
        yhteiset = [ luku for luku in a_lista if luku in b_lista ]

        for i in range(0, len(yhteiset)):
            leikkausjoukko.lisaa(yhteiset[i])

        return leikkausjoukko

    @staticmethod
    def erotus(pohjajoukko, poistojoukko):
        poistettavat = poistojoukko.to_int_list()
        for luku in poistettavat:
            pohjajoukko.poista(luku)
        return pohjajoukko

    def __str__(self):
        tulostettava_joukko = list(map(str,self.to_int_list()))
        return "{" + ', '.join(tulostettava_joukko) + "}"
