import random
def random(min,max):
    list = []
    i = 0
    while i < 5:
        a = random.randrange(min,max)
        if list.count(a) == 0:
            list.append(a)
            i += 1
    print(list)


random(1,56)