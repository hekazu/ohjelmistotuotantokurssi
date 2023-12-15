from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from kps import KiviPaperiSakset, Vaikeusaste

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self,vaikeusaste):
        if vaikeusaste == Vaikeusaste.NORMAALI:
            self._tekoaly = Tekoaly()
        if vaikeusaste == Vaikeusaste.HAASTAVA:
            self._tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        if self._onko_ok_siirto(ensimmaisen_siirto):
            self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return siirto
