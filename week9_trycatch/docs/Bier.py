class Bier:
    def __init__(self, nummer: str, naam: str, regio: str, kleur: str, percentage: float) -> None:
        super().__init__()
        self.nummer = nummer
        self.naam = naam
        self.regio = regio
        self.kleur = kleur
        self.percentage = percentage

    @property
    def nummer(self):
        return self.__nummer

    @nummer.setter
    def nummer(self, value):
        if isinstance(value, str):
            if value == "":
                self.__nummer = "onbekend"
            else:
                self.__nummer = value
        else:
           raise ValueError("foute value nummer")

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        if isinstance(value, str):
            if value == "":
                self.__naam = "onbekend"
            else:
                self.__naam = value
        else:
            raise ValueError("foute value naam")

    @property
    def regio(self):
        return self.__regio

    @regio.setter
    def regio(self, value):
        if isinstance(value, str):
            self.__regio = value
        else:
            raise ValueError("foute regio")

    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, value = "onbekend"):
        if isinstance(value, str):
            self.__kleur = value
        else:
            raise ValueError("fout kleur")

    @property
    def percentage(self):
        return self.__percentage

    @percentage.setter
    def percentage(self, value):
        if isinstance(value, float):
            self.__percentage = value
        elif value == "":
            self.__percentage = -1
        else:
            raise ValueError("foute value")

    @staticmethod
    def inlezen_bieren(bestandsnaam):
        bieren = []
        try:
            fo = open(bestandsnaam, "r")
            line = fo.readline()
            line = fo.readline()
            while (line != ""):
                line = line.rstrip('\n')
                delen = line.split(";")
                try:
                    bier = Bier(delen[0], delen[1], delen[2], delen[3], float(delen[4].replace(",",".")))
                    bieren.append(bier)
                except ValueError as ex:
                    print(ex)
                line = fo.readline()
            fo.close()
        except FileNotFoundError:
            print("foute naam van bestand")
        return bieren

    @staticmethod
    def zoek_naam(waar, naam):
        a  = []
        for i in waar:
            if naam.lower() in i.naam.lower():
                a.append(i)
        return a

    def __str__(self) -> str:
        return str(self.nummer) + "," + self.naam + "," + self.regio + "," + self.kleur + ", " + str(self.percentage)
