from tekoaly import Tekoaly
from pelaaja import Pelaaja
from kps import KPS


class KPSTekoaly(KPS):
    def __init__(self):
        super().__init__(
            Pelaaja("Ensimmäisen pelaajan siirto: "),
            Tekoaly()
        )
