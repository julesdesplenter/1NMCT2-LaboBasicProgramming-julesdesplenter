nmct = {"1NMCT": 131, "2NMCT": 88, "3NMCT": 77}

def printDictionary(dictionary, naam):
    for key,value in dictionary.items():
        print("in {2} key: {0} value:{1}".format(key,value,naam))

printDictionary(nmct,"wakataka")
