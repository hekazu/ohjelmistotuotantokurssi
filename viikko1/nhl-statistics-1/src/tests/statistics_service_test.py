import unittest
from statistics_service import StatisticsService,SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # käytetään verkkoyhteydetöntä "stub"-oliota
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_pelaajan_haku_toimii(self):
        pelaaja = self.stats.search("Kurri")

        self.assertEqual(str(pelaaja), "Kurri EDM 37 + 53 = 90")

    def test_olemattoman_pelaajan_haku_palauttaa_nonen(self):
        pelaaja = self.stats.search("Olematon")

        self.assertIsNone(pelaaja)

    def test_yhden_tiimin_pelaajat_haettavissa(self):
        edm_jasenet = self.stats.team("EDM")
        pit_jasenet = self.stats.team("PIT")

        self.assertEqual(len(edm_jasenet), 3)
        self.assertEqual(len(pit_jasenet), 1)

    def test_top_palauttaa_annetun_maaran_pelaajia(self):
        top3 = self.stats.top(3)

        self.assertEqual(len(top3), 3)

    def test_top_jarjestaa_oletusarvoisesti_pisteilla(self):
        pistepaallikot = self.stats.top(1)

        self.assertEqual(str(pistepaallikot[0]), "Gretzky EDM 35 + 89 = 124")

    def test_top_eksplisiittinen_pistejarjestys_toimii(self):
        pistepaallikot = self.stats.top(2,SortBy.POINTS)

        self.assertEqual(str(pistepaallikot[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(str(pistepaallikot[1]), "Lemieux PIT 45 + 54 = 99")

    def test_top_maalijarjestys_jarjestaa_oikein(self):
        maalintekijat = self.stats.top(1,SortBy.GOALS)

        self.assertEqual(str(maalintekijat[0]), "Lemieux PIT 45 + 54 = 99")

    def test_top_avustusjarjestys_jarjestaa_oikein(self):
        avustajat = self.stats.top(2,SortBy.ASSISTS)

        self.assertEqual(str(avustajat[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(str(avustajat[1]), "Yzerman DET 42 + 56 = 98")
