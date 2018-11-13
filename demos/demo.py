import os

# huidige dir opvragen
print("Huidige dir is %s " % os.getcwd())
print("De inhoud is: %s" % os.listdir("."))

# aanwezigheid van dir controleren en indien afwezig dir aanmaken
if (not os.path.exists("testDir")):
    os.mkdir("testDir")         # opm: kan slechts éénmaal aangemaakt worden
    # verplaatsen naar nieuwe Dir, nadien positie opvragen
    os.chdir("testDir")
    print("Na verplaatsing is de huidige dir: %s " % os.getcwd())
    for teller in range(1, 1000):
        filename = "file" +str(teller) +".txt"
        new_file = open(filename, "w")
        new_file.write("Ik ben bestand %d" % teller)
        new_file.close()
    #terugspringen naar parent dir
    os.chdir("..")


# directory verwijderen
import shutil
print("Huidige dir is %s " % os.getcwd())
if (input("Wenst u de directory testDir te verwijderen?(Y/N)") == "Y"):
    shutil.rmtree("testDir")    #dir samen met inhoud wissen
    # os.rmdir("testDir")     #verwijderen enkel als die leeg is