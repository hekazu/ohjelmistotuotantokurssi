from tekoaly_parannettu import TekoalyParannettu
from kps import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi {siirto}")
        if self._onko_ok_siirto(ensimmaisen_siirto):
            self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return siirto
