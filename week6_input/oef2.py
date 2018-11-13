#oef2
import os

def checkFile(file):
    if os.path.isfile(file):
        return True
    else:
        return False

def readFile(file):
    f = open(file, "r", encoding="utf8")
    line = f.readline()
    index = 1
    while line:
        line = line.rstrip("\n")
        print("{0}:{1}".format(index,line))
        index += 1
        line = f.readline()
    f.close()

def write(file):
    f = open(file, "w+")
    while True:
        i = str(input("geef hier je lijn in, bij s stopt het"))
        if i == "s":
            return False
        else:
            f.write(i + "\n")


def read(file):
    if checkFile(file):
        readFile(file)
    else:
        write(file)
        readFile(file)

read("test.txt")
read("test4.txt")