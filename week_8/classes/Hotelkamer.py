class Hotelkamer:
    def __init__(self, number, guests:list) -> None:
        super().__init__()
        self.number = number
        self.guests = guests

    def free(self):
        if self.guests == []:
            return(self.number)
        else:
            pass


    def __str__(self):
        return self.number

