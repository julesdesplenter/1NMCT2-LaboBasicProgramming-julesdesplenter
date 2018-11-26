class Bier:
    def __init__(self, gisting:str, graansoort:str, regio:str, percentage: int) -> None:
        super().__init__()
        self.gisting = gisting
        self.graansoort = graansoort
        self.regio = regio
        self.percentage = percentage

    @property
    def gisting(self):
        return self._gisting

    @gisting.setter
    def gisting(self, value):
        if value == "":
            self._gisting =  "onbekend"
        else:
            self._gisting = value

    @property
    def graansoort(self):
        return self._graansoort

    @graansoort.setter
    def graansoort(self, value):
        if value == "":
            self._graansoort =  "onbekend"
        else:
            self._graansoort = value

    @property
    def regio(self):
        return self._regio

    @regio.setter
    def regio(self, value):
        if value == "":
            self._regio =  "onbekend"
        else:
            self._regio = value

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        if type(value) is float or type(value) is int and value >= 0 and value <= 100:
            self._percentage = value
        else:
            self._percentage = 0

    def __str__(self) -> str:
        return self._gisting + "," + self._graansoort + "," + self._regio + "," + str(self._percentage)

