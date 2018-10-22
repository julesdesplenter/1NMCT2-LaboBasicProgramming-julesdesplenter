list1 = [1,2,6,21]
list2 = [6,5,21,25]

def different(name1,name2):
    for i in range(0,len(name1)):
        if name2.count(name1[i]) != 0:
            print(name1[i])

different(list1,list2)