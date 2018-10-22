import itertools
list1 = ["a", "b","c"]
list2 = ["d","e","f"]
list3 = ["g","h","j"]

def makeSentence(name1, name2, name3):
    list4 = list(itertools.product(name1,name2,name3))
    print(list4)

makeSentence(list1,list2,list3)


