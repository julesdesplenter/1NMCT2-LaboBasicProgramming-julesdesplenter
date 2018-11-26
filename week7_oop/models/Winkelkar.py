class Winkelkar:
    def __init__(self) -> None:
        super().__init__()
        self._producten = []

    @property
    def producten(self):
        for i in self._producten:
            return i

    @producten.setter
    def producten(self, value):
        pass

    def voegToe(self, product):
        self._producten.append(product)


    def verwijder(self, product):
        self._producten.remove(product)

    def plus(self, w1, w2):
        for i in w1._producten:
            self._producten.append(i)
        for i in w2._producten:
            self._producten.append(i)


    def __str__(self) -> str:
        return str(self._producten)




