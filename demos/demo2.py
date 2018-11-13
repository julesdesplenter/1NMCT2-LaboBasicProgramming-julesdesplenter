# openen van een file
def testje(bestandsnaam):
    fo = open(bestandsnaam, "r")  # open geeft een File-object terug

    # van het object kunnen we een aantal eigenschappen opvragen
    print("gesloten? %s " % fo.closed)
    print("bestandsnaam: %s" % fo.name)
    print("Access-mode: %s" % fo.mode)
    fo.close()
    print("Nu gesloten? %s \n" % fo.closed)


testje("NMCT.txt")


# open a file ==> file-object
# voorbeeld 1a
def print_inhoud_bestand_1(bestandsnaam):
    fo = open(bestandsnaam, "r")  # opgelet: r+
    data = fo.read()  # alle lijnen worden in 1 keer inlezen en terug gegeven als één string
    print(data)
    fo.close()

print("**Demo met read()**")
print_inhoud_bestand_1("NMCT.txt")


# voorbeeld 2
def print_inhoud_bestand_2(bestandsnaam):
    fo = open(bestandsnaam, "r")  # opgelet: r+
    line = fo.readline().rstrip("\n")  # Eerste lijn inlezen        -> new-line karakter verwijderenn
    while (line != ""):
        print(line)
        line = fo.readline()  # Volgende lijn inlezen
    fo.close()

print("**Demo met readline()**")
print_inhoud_bestand_2("NMCT.txt")


# voorbeeld 3
def print_inhoud_bestand_3(bestandsnaam):
    fo = open(bestandsnaam, "r")  # opgelet: r+
    lines = fo.readlines()  # alle lijnen worden in 1 keer inlezen en teruggegeven als een list van strings
    print(lines)
    fo.close()

print("**Demo met readlines()**")
print_inhoud_bestand_3("NMCT.txt")


# voorbeeld 3
def geef_jaren(bestandsnaam):
    # lees alle jaartallen in, en geef deze in een list terug
    # let op: eerste lijn overslaan (is geen jaartal)
    jaren = []
    file_bestandsnaam = open(bestandsnaam, "r")
    jaren = file_bestandsnaam.read().splitlines()[1:]  # eerste lijn overslaan
    file_bestandsnaam.close()
    return jaren

print("\n**Demo met read & splitlines**")
schrikkeljaren = geef_jaren("jaren.txt")
print(schrikkeljaren)