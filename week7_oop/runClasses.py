# runClasses
import random
from models.Boek import Boek
from models.Bier import Bier
from models.Auto import Auto
from models.Meetwiel import Meetwiel
from models.Winkelkar import Winkelkar

boek1 = Boek("titel", "auteur", "1995")
boek2 = Boek("rikkert", "ontslagen", "2020")
bier1 = Bier("gisting", "tarwe", "westhoek", 12)
bier2 = Bier("", "", "", 8)
auto1 = Auto("groen", "ferrari", "diesel", "gekkenhuis", 351)
wiel1 = Meetwiel(5,4)
winkelkar1 = Winkelkar()
winkelkar2 = Winkelkar()
winkelkar3 = Winkelkar()


# bier2.naam = "rodenbach"
# bier2.percentage = 5.2
# auto1.rijden(45)
# auto1.rijden(random.randrange(1000000))
# print(wiel1.afstand())
# print(wiel1.omtrek())
# wiel1.rijden()
winkelkar1.voegToe("een liter melk")
winkelkar1.voegToe("een kilo kaas")
winkelkar1.voegToe("een mandarijn")
winkelkar1.verwijder("een mandarijn")
winkelkar2.voegToe("een vliegtuig")
winkelkar3.plus(winkelkar1,winkelkar2)
print(winkelkar3)


