a = ("1NMCT","2NMCT","3NMCT")

def printList(tuple,naamTuple):
        for i in tuple:
            print("{0} staat in {2} positie {1}".format(i, tuple.index(i), naamTuple))

printList(a, "vliegtuig")
