def printDictionary(dictionary):
    for key, value in dictionary.items():
        print("key: {0} value:{1}".format(key, value))


def telWoorden(a):
    list = a.split()
    dic = {}
    for i in list:
        if list.count(i) > 0:
            dic.update({i: list.count(i)})
    printDictionary(dic)


telWoorden("ik ben een vliegtuig enal ben een ik ik een ene ene eneeen elezihfre string string string in")
