from docs.Bier import Bier

try:
    bier1 = Bier(5,"nmct", "howest", "blond", 5.0)
    print(bier1)
    bier1.naam = "mct"
    print(bier1)
except ValueError as ex:
    print(f"foutmelding: {ex}")

alleBieren = Bier.inlezen_bieren("docs/bieren.csv")
zoekbier = input("geef bier dat je zoekt")
gezochtebieren = Bier.zoek_naam(alleBieren, zoekbier)
for i in gezochtebieren:
    print(i)


