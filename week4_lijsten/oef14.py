list1 = [1,2,2,21,2]

def countElements(name, min, max):
    counter = 0
    for i in name:
        if isinstance(i,int):
            counter = counter + 1
    if(counter == len(name)):
        if (isinstance(min, int) and isinstance(max,int)):
            if(min < max):
                a = 0
                for i in range(min,max):
                    a = a + name.count(i)
            print(a)

countElements(list1,2,7)