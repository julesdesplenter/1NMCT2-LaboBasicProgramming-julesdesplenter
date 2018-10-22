list1 = [1,2,6,21,2]


def different(name):
    for i in name:
        if name.count(i) > 1:
            name.remove(i)
    print(list1)


different(list1)



