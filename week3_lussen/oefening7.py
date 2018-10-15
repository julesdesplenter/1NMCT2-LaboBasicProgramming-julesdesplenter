start = int(input("geef een startwaarde op"))
step = int(input("met hoeveel moet hij vooruit springen?"))
long = int(input("hoeveel getallen moet ik tonen"))
i = start

while i < start + (long*step):
    print(i)
    i = i + step
