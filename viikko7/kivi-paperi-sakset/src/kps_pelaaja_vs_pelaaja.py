from pelaaja import Pelaaja
from kps import KPS


class KPSPelaajaVsPelaaja(KPS):
    def __init__(self):
        super().__init__(
            Pelaaja("Ensimmäisen pelaajan siirto: "),
            Pelaaja("Toisen pelaajan siirto: ")
        )
