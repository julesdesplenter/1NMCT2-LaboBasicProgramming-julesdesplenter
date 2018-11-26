class Boek:
    def __init__(self, titel :str, auteur:str, jaar:str) -> None:
        super().__init__()
        self._titel = titel
        self._auteur = auteur
        self._jaar = jaar

    #properties
    @property
    def titel(self):
        return self._titel

    @titel.setter
    def titel(self, value):
        self._titel = value

    @property
    def auteur(self):
        return self._auteur

    @auteur.setter
    def auteur(self, value):
        self._auteur = value

    @property
    def jaar(self):
        return self._jaar

    @jaar.setter
    def jaar(self, value):
        self._jaar = value

    def __str__(self) -> str:
        return self._jaar



