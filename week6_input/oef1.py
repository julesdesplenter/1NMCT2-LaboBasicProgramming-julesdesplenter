#oef 1
import os

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

readFile("test.txt")