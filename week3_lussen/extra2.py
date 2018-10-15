def isPrime(getal):
    a = 0
    for i in range (2,getal):
        if getal % i != 0:
            a = a + 1
            if a == (getal - 2):
                print("{0} is een priem getal".format(getal))


isPrime(19)
