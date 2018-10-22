l = int(input("wat is de leeftijd van je hond"))

if l < 0:
    print("foutmelding")
elif l == 1:
    print("je hond is 14 mensenjaren oud")
elif l == 2:
    print("je hond is 22 jaar oud")
elif l > 2:
    leeftijd = 22 + ((l - 2) * 5)
    print("je hond is {0} mensenjaren oud".format(leeftijd))
