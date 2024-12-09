from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class KPS:
    def __init__(self, eka_pelaaja, toka_pelaaja):
        self._eka_pelaaja = eka_pelaaja
        self._toka_pelaaja = toka_pelaaja

    def pelaa(self):
        tuomari = Tuomari()

        siirra_eka = self._pelaaja_siirto(self._eka_pelaaja)
        siirra_toka = self._pelaaja_siirto(self._toka_pelaaja)
        ekan_siirto = siirra_eka()
        tokan_siirto = siirra_toka()

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = siirra_eka()
            tokan_siirto = siirra_toka()

            self._toka_pelaaja.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)


    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    def _pelaaja_siirto(self, pelaaja):
        def psiirto():
            siirto = pelaaja.anna_siirto()
            if isinstance(pelaaja, (Tekoaly, TekoalyParannettu)):
                print(f"Tietokone valitsi: {siirto}")
            return siirto
        return psiirto
