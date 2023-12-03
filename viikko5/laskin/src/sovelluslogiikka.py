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
        self.logiikka.kumoa()


class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._kumousjono = []

    def aseta_arvo(self, arvo):
        self._kumousjono.append(self._arvo)
        self._arvo = arvo

    def kumoa(self):
        self._arvo = self._kumousjono.pop()

    def arvo(self):
        return self._arvo

    def on_kumottavaa(self):
        return len(self._kumousjono) > 0
