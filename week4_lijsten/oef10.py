list1 = [1,2]
list2 = [6,5,21,25]

def different(name1,name2):
    a = 0
    for i in range(0,len(name1)):
        if name2.count(name1[i]) != 0:
            a = a + 1
    if a > 0:
        print("er zit een zelfde getal in de twee lijsten")
    else:
        print("er zit geen zelfde getal in de twee lijsten")

different(list1,list2)