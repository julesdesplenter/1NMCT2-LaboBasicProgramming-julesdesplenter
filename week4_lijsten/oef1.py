
list1 = [1,2,3,4]
list2 = [1,2,3,4,5]
list3 = ["a", "b", "c", "d"]

def printList(name):
    for i in range(0,len(name)):
        print("op plaats {0} staat er {1}".format(i, name[i]))

printList(list3)