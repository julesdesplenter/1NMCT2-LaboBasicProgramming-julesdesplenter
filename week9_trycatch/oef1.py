#oef1

som = 0
try:
    bestand = input("tel de getallen op van een bestand..")
    fo = open(bestand)
    line = fo.readline()
    while(line):
        try:
            som = som + int(line)
        except ValueError  as ve:
            print("foutieve lijn")
        finally:
            line = fo.readline().strip()
    fo.close()
except FileNotFoundError as fe:
    print("bestand niet gevonden")

print(som)

