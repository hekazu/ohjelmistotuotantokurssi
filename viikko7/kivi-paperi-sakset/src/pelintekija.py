from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps import Vaikeusaste

class Pelintekija:
    @staticmethod
    def luo_peli(tunnus):
        if tunnus == 'a':
            return KPSPelaajaVsPelaaja()
        if tunnus == 'b':
            return KPSTekoaly(Vaikeusaste.NORMAALI)
        if tunnus == 'c':
            return KPSTekoaly(Vaikeusaste.HAASTAVA)

        return None
