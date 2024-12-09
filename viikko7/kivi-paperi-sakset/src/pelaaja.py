class Pelaaja:
    def __init__(self, siirto_kysymys):
        self._siirto_kysymys = siirto_kysymys

    def anna_siirto(self):
        return input(self._siirto_kysymys)

    def aseta_siirto(self, siirto):
        # ei tehdä mitään
        pass
