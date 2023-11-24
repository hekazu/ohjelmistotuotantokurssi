import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        varasto_mock = Mock()

        # viitenumero on aina 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 10
            else:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "leipä", 6)
            else:
                return Tuote(99, "Muumitikkari", 1)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikein(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla arvoilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_useamman_tuotteen_ostos_kutsuu_tilisiirtoa_oikein(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla arvoilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 11)

    def test_ostoksen_paatyttya_useampi_sama_tuote_toimii_tilisiirron_luonnissa(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla arvoilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 12)

    def test_ostoksen_paatyttya_kun_kaikkia_tuotteita_ei_ole_tilisiirto_tehdaan_oikeilla_arvoilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        # yritetään lisätään tuote jota ei ole saatavilla
        self.kauppa.lisaa_koriin(50)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla arvoilla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_varmista_etta_uuden_ostostapahtuman_aloittaminen_nollaa_edellisen(self):
        # laitetaan muutamia ostoksia pohjalle
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)

        # unohdetaan edelliset
        self.kauppa.aloita_asiointi()
        # ja ostetaan leipä
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että tilisiirto tehdään relevantilla hinnalla
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 6)

    def test_vamista_etta_kauppa_pyytaa_aina_uuden_viitenumeron(self):
        # Käytetään toisistaan eroavia viitenumeroita
        self.viitegeneraattori_mock.uusi.side_effect = [1,2,3]

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # tarkistetaan viitenumero
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 1, ANY, ANY, ANY)

        # uusi ostotapahtuma
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("olavi", "54321")

        # tarkistetaan viitenumero
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 2, ANY, ANY, ANY)

        # vielä yksi
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(77)
        self.kauppa.tilimaksu("ernesti", "1337")

        # tarkistetaan viitenumero
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 3, ANY, ANY, ANY)

    def test_korista_poistettu_tuote_ei_mene_laskulle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("olavi", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 5)

        # Testaa myös eri tuotteilla
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("olavi", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(ANY, ANY, ANY, ANY, 5)
