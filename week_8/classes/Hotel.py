from classes.Hotelkamer import Hotelkamer

class Hotel:
    def __init__(self, kamers = {}) -> None:
        super().__init__()
        self._kamers = kamers
        for kamer in kamers:
            self._kamers[kamer] = Hotelkamer(kamer)

    def __str__(self) -> str:
        return super().__str__()

    def geefKamer(self,kamernummer):
        if kamernummer in self._kamers.keys():
            return self._kamers[kamernummer]
        else:
            return None



