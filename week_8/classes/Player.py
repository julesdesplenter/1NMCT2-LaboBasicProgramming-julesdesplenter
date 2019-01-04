from classes.Birth import Birth

class Player:
    scoreTotaal = 0

    def __init__(self, name: str, familyName: str, score: int, birth) -> None:
        super().__init__()
        self.name = name
        self.familyName = familyName
        self.score = score
        self.birth = birth
        Player.scoreTotaal += self.score

    def __str__(self) -> str:
        return self.name + " " + self.familyName + " " + str(self.score) + " " + str(self.birth)

    def __del__(self):
        Player.scoreTotaal -= self.score
