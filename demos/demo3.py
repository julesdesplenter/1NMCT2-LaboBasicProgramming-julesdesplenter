# open a file ==> file-object
fo = open("Temp.txt", "w+")
# file-object attributes
print("Name of the file: " + fo.name)
print("Closed?: " + str(fo.closed))
print("Access mode : " + fo.mode)
# write()-methode
fo.write("Python is a great language.\nYeah it's great!!\n");
fo.close()


# wegschrijven van alle schrikkeljaren naar een file
def is_schrikkeljaar(jaartal):
    # deze functie controleert of het doorgegeven jaartal een schrikkeljaar is
    test = False
    # controle 1: deelbaar door 4? -> schrikkeljaar
    if ((jaartal % 4) == 0): test = True
    # controle 2: deelbaar door 100? -> geen schrikkeljaar
    if ((jaartal % 100) == 0): test = False
    # controle 3: deelbaar door 100 en deelbaar door 400 -> wel schrikkeljaar
    if ((jaartal % 400) == 0): test = True
    return test


def opslaan_schrikkeljaren(startjaar, stopjaar, bestandsnaam):
    file_jaren = open(bestandsnaam, "w+")
    file_jaren.write("De schrikkeljaren tussen %s en %s zijn:\n" % (startjaar, stopjaar))
    for jaartal in range(startjaar, stopjaar + 1):
        if (is_schrikkeljaar(jaartal)):
            file_jaren.write(str(jaartal) + "\n")  # opgelet: vergeet niet str en \n te gebruiken
    file_jaren.close()


opslaan_schrikkeljaren(1000, 210000, "jaren.txt")
