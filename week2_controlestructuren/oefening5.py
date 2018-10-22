s = float(input("geef uw score "))
if s >= 10:
    print("je bent geslaagd!")
elif s >= 9 and s < 10:
    s2 = s % 1
    if s2 >= 0.5:
        print("je bent geslaagd")
    else:
        print("je bent niet geslaagd")
else:
    print("je bent niet geslaagd")