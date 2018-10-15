

jaartal1 = int(input("geef een jaartal op"))
jaartal2 = int(input("geef nog een jaartal op"))

def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return("is a leap year")
            else:
                return("is not a leap year")
        else:
            if year % 100 != 0:
                return("is a leap year")
    else:
        return("is not a leap year")

for i in range(jaartal1,jaartal2):
    if leapYear(i) == "is a leap year":
        print(i)





