import random

def read(file):
    player = []
    f = open(file, "r", encoding="utf-8")
    # while line != "":
    #     player.append(line)
    for speler in f.readlines():
        spelers = speler.rstrip("\n")
        player.append(spelers)
    return player


def print2(list):
    i = 1
    while i < len(list):
        print("{0} : {1}".format(i, list[i]))
        i = i + 1

def randomSelect(list):
    group = []
    i = 0
    while i <= 11:
        r = random.randrange(0,len(list))
        if not(list[r] in group):
            group.append(list[r])
            i += 1
    return group

print2(randomSelect(read("tekstbestanden/Spelers.txt")))

