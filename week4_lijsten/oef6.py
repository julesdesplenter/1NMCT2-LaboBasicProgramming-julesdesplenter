import random

list1 = [5,6,1,56,21,51,51,3,13,1,1]

def kiesElement(name):
    print(name[random.randrange(0,len(name))])

kiesElement(list1)