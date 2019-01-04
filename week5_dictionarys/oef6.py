howest = {'1NMCT': 131, '2NMCT': 88, '3NMCT': 77, '1Devine': 123, '2Devine': 98, '3Devine': 55}

def addElements(dic,val,key):
    if val in dic:
        print("element zit al in de lijst")
    else:
        # dic.update({val: key})
        dic[val] = key

def printDictionary(dictionary):
    for key,value in dictionary.items():
        print("key: {0} value:{1}".format(key,value))

addElements(howest,"IPO1",51)
addElements(howest,"IPO1", 1)
printDictionary(howest)
