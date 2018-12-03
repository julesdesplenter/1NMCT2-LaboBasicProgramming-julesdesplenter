
from classes.Player import Player
from classes.Birth import Birth
from classes.Hotel import Hotel
from classes.Hotelgast import Hotelgast
from classes.Hotelkamer import Hotelkamer

p1 = Player("bob","jos",15,12,12,12)
p2 = Player("h","ij",48,13,13,13)
bob = Birth(12,2,1996)
bob2 = Birth.randomNumber()
bob3 = Birth(12,2,1996)
bob4 = Birth(12,2,200)
kamer1 = Hotelkamer("a1",["kjhb","kjgh"])
kamer2 = Hotelkamer("a2", [])
hotel1 = Hotel({"kamer1":"a1","kamer2":"a2"})

# print(Birth.toonAantal())
# print(bob)
# print(bob2)
# print(Birth.randomList(5))
# print(bob == bob2)
# print(bob == bob3)
# print(bob.sameDay(bob4))
# print(bob.sameDay(bob2))
# for i in hotel1.dic().keys():


if kamer1.free():
    print(kamer1)
if kamer2.free():
    print(kamer2)

