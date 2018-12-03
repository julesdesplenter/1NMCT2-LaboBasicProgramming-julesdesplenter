import random


class Birth:
    aantal = 0

    def __init__(self, day, month, year) -> None:
        super().__init__()
        self._day = day
        self._month = month
        self._year = year
        Birth.aantal += 1

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if value is int and value <= 31:
            self._day = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if value is int and value <= 12:
            self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value is int and value <= 2018:
            self._year = value

    def __del__(self):
        Birth.aantal -= 1

    @staticmethod
    def toonAantal():
        return Birth.aantal

    @staticmethod
    def randomNumber():
        dag = random.randrange(1, 32)
        maand = random.randrange(1, 13)
        jaar = random.randrange(1, 2019)
        return Birth(dag, maand, jaar)

    @staticmethod
    def randomList(aantal):
        list = []
        for i in range(aantal):
            list.append(Birth.randomNumber().__str__())
        return list

    def __eq__(self, other):
        if self._day != other._day:
            return False
        elif self._month != other._month:
            return False
        elif self._year != other._year:
            return False
        else:
            return True

    def sameDay(self, other):
        if self._day != other._day:
            return False
        elif self._month != other._month:
            return False
        else:
            return True



    def __str__(self) -> str:
        return str(self._day) + "/" + str(self._month) + "/" + str(self._year)
