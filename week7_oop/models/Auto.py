class Auto:
    def __init__(self, kleur:str, merk:str,brandstof:str, model:str, kmstand:int) -> None:
        super().__init__()
        self.kleur = kleur
        self.merk = merk
        self.brandstof = brandstof
        self.model = model
        self.kmstand = kmstand
        
        @property
        def kmstand(self):
            return self._kmstand
        
        @kmstand.setter
        def kmstand(self, value):
            self._kmstand = value
            
        @property
        def kleur(self):
            return self.kleur 
        
        @kleur.setter
        def kleur(self, value):
            self.kleur = value

        @property
        def kmstand(self):
            return self._kmstand

        @kmstand.setter
        def kmstand(self, value):
            pass

    def rijden(self, aantal_km):
            self.kmstand += aantal_km
            return self.kmstand

    def __str__(self) -> str:
        return str(self.kmstand)

