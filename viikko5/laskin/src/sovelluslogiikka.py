class BinaariOperaatio:
    def __init__(self, sovelluslogiikka, lukija):
        self.logiikka = sovelluslogiikka
        self.lukija = lukija

    def suorita(self):
        self.logiikka.aseta_arvo(0)


class Summa(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, lukija):
        super().__init__(sovelluslogiikka, lukija)

    def suorita(self):
        self.logiikka.aseta_arvo(self.logiikka.arvo() + int(self.lukija()))


class Erotus(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, lukija):
        super().__init__(sovelluslogiikka, lukija)

    def suorita(self):
        self.logiikka.aseta_arvo(self.logiikka.arvo() - int(self.lukija()))


class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.logiikka = sovelluslogiikka

    def suorita(self):
        self.logiikka.aseta_arvo(0)


class Kumoa:
    def __init__(self, sovelluslogiikka):
        self.logiikka = sovelluslogiikka

    def suorita(self):
        pass


class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
