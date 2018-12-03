class Player:
    scoreTotaal = 0

    def __init__(self, name: str, familyName: str, score: int, day: int, month: int, year: int) -> None:
        super().__init__()
        self.name = name
        self.familyName = familyName
        self.score = score
        self.day = day
        self.month = month
        self.year = year
        Player.scoreTotaal += self.score

    def __str__(self) -> str:
        return self.name + " " + self.familyName + " " + str(self.score) + " " + str(self.day) + "/" + str(
            self.month) + "/" + str(self.year)

    def __del__(self):
        Player.scoreTotaal -= self.score
