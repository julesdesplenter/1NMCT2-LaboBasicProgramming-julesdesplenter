import random

a = random.randrange(1,21)

i = 0

for i in range(5):
    guess = int(input("raad het nummer "))
    if a > guess:
        print("je gok is te laag je hebt nog {0} kansen".format(5 - i))
    elif a < guess:
        print("je gok is te laag je hebt nog {0} kansen".format(5 - i))
    elif a == guess:
        print("je hebt het juist geraden in {0} beurten".format(5 - i))
        exit()
print("jammer je hebt het niet geraden het juiste getal was {0}".format(a))


