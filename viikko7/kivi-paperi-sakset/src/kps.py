from tuomari import Tuomari
from enum import Enum


class Vaikeusaste(Enum):
    NORMAALI = 1
    HAASTAVA = 2


class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print("Kiitos!")
            print(tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

    # Tämä on joka pelissä sama, hoituu näin yläluokassa kätevästi
    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # Tämä taas ei toimi tällaisenaan, mutta toteutetaan vaikka herrasmieskivi
    def _toisen_siirto(self, ensimmaisen_siirto):
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
