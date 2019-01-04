#oef 1
import os

# def readFile(file):
#     f = open(file, "r", encoding="utf8")
#     line = f.readline()
#     index = 1
#     while line:
#         line = line.rstrip("\n")
#         print("{0}:{1}".format(index,line))
#         index += 1
#         line = f.readline()
#     f.close()


def readFile(bestand):
    i = 0
    fo = open(bestand)
    line = fo.readline()
    line = line.rstrip("\n")
    while line:
        print(f"{i} , {line}")
        line = fo.readline()
        line = line.rstrip("\n")
        i += 1
    fo.close()

readFile("test.txt")