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

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 3
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "piimä", 2)
        
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_pankin_tilisiirtoa_kutsutaan_tilimaksua_kutsuttaessa(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("meitsi", "15")
        
        self.pankki_mock.tilisiirto.assert_called_with("meitsi", 42, "15", "33333-44455", 5)

    def test_pankin_tilisiirtoa_kutsutaan_tilimaksua_kutsuttaessa_oikealla_summalla_kun_kahsi_eri_tuotetta_ostoskorissa(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("meitsi", "15")
        
        self.pankki_mock.tilisiirto.assert_called_with("meitsi", 42, "15", "33333-44455", 7)

    def test_pankin_tilisiirtoa_kutsutaan_tilimaksua_kutsuttaessa_oikealla_summalla_kun_kaksi_samaa_tuotetta_ostoskorissa(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("meitsi", "15")
        
        self.pankki_mock.tilisiirto.assert_called_with("meitsi", 42, "15", "33333-44455", 10)


    def test_pankin_tilisiirtoa_kutsutaan_tilimaksua_kutsuttaessa_oikealla_summalla_kun_kaksi_eri_tuotetta_lisatty_ostoskoriin_joista_toinen_loppu(self):
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 0
        
        self.varasto_mock.saldo.side_effect = varasto_saldo

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("meitsi", "15")
        
        self.pankki_mock.tilisiirto.assert_called_with("meitsi", 42, "15", "33333-44455", 5)


    def test_kaupan_metodi_aloita_asiointi_nollaa_kaupan_tilan(self):
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 0
        
        self.varasto_mock.saldo.side_effect = varasto_saldo

        def generaattori():
            for i in range(10):
                yield i
            return 10

        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.side_effect = generaattori()

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("meitsi", "15")
        self.pankki_mock.tilisiirto.assert_called_with("meitsi", 0, "15", "33333-44455", 5)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("meitsi", "15")
        self.pankki_mock.tilisiirto.assert_called_with("meitsi", 1, "15", "33333-44455", 5)

    def test_kaupan_metodi_poista_korista_poistaa_tuotteen_ostoskorista(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.poista_korista(2)
        kauppa.tilimaksu("meitsi", "15")
        self.varasto_mock.palauta_varastoon.assert_called_with(Tuote(2, "piimä", 2))
        self.pankki_mock.tilisiirto.assert_called_with("meitsi", 42, "15", "33333-44455", 5)
        