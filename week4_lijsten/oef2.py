list1 = []
a = 0
while a < 1:
    vriend = input("geef de naam van je vriend ")
    if vriend == "":
        print(list1)
        a = a + 1
    else:
        list1.append(vriend)