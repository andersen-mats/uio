class Ulv:
    def __init__(self, navn, posisjon):
        self._navn = navn
        self._posisjon = posisjon
        self._vekt = 20

    def spis_sau(self, sau):
        sau.blir_spist()
        self._vekt += 5

    def hent_vekt(self):
        return self._vekt

    def hent_navn(self):
        return self._navn

    def hent_posisjon(self):
        return self._posisjon
    
    def beveg_hoeyre(self):
        self._posisjon += 1
        if self._posisjon > 10:
            self.posisjon = 1

    def beveg_venstre(self):
        self._posisjon -= 1
        if self._posisjon < 1:
            self.posisjon = 10



