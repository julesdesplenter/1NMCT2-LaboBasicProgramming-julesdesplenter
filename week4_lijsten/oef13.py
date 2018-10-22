list1 = [5,25,6,21,6]
list2 = [6,5,21,25,6]

# def different(name1,name2):
#      b = False
#      a = 0
#      for i in name1:
#          if name2.count(i) == name1.count(i):
#              a = a + name1.count(i)
#      if a == len(name1):
#          b = True
#      print(b)
#
# different(list1,list2)

def same(name1,name2):
    same = False
    name1.sort()
    name2.sort()
    if name1 == name2:
        same = True
    print(same)
same(list1,list2)