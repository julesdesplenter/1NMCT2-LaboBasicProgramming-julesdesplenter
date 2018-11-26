import math

class Meetwiel:
    def __init__(self, straal:int,omwenteling:int) -> None:
        super().__init__()
        self.straal = straal
        self.omwenteling = omwenteling

    def omtrek(self):
        return ((self.straal**2) * math.pi)

    def afstand(self):
        return (((self.straal**2) * math.pi)*self.omwenteling)

    @property
    def omwenteling(self):
        return self._omwenteling

    @omwenteling.setter
    def omwenteling(self, value):
        self._omwenteling = value

    def check(self, _iets):
        try:
            int(self._iets)
            return True
        except TypeError:
            return False


    def rijden(self):
        aantal = input("geef het aantal omwentelingen")
        if self.check(aantal):
            int(aantal)
            self.omwenteling += aantal
        else:
            return "niet geldig"


    def __str__(self) -> str:
        return "de afstand is " + str(((self.straal**2) * math.pi)*self.omwenteling)








