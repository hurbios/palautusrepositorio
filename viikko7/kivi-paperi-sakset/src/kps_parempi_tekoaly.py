from tekoaly_parannettu import TekoalyParannettu
from pelaaja import Pelaaja
from kps import KPS

class KPSParempiTekoaly(KPS):
    def __init__(self):
        super().__init__(
            Pelaaja("Ensimmäisen pelaajan siirto: "),
            TekoalyParannettu(10)
        )
