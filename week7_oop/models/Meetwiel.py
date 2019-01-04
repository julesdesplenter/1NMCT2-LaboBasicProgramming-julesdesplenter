import math


class Meetwiel:
    def __init__(self, straal: int, omwenteling: int) -> None:
        super().__init__()
        self.straal = straal
        self.omwenteling = omwenteling

    @property
    def straal(self):
        return self.__straal

    @straal.setter
    def straal(self, value):
        if isinstance(value, int):
            self.__straal = value
        else:
            raise ValueError("straal")

    @property
    def omwenteling(self):
        return self.__omwenteling

    @omwenteling.setter
    def omwenteling(self, value):
        if isinstance(value, int):
            self.__omwenteling = value
        else:
            raise ValueError("omwenteling")

    def omtrek(self):
        return (self.straal ** 2) * math.pi

    def afstand(self):
        return self.omtrek() * self.omwenteling

    def rijden(self):
        while True:
            omwen = input("geef hoeveel omwentelingen stop met c")
            if omwen == "c":
                return False
            else:
                try:
                    a  = int(omwen)
                    self.omwenteling = self.omwenteling + a
                except ValueError:
                    print("geen int")

