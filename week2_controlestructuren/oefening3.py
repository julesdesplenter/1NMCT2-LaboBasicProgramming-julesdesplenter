import datetime

a = int(input("geef uw geboortejaar"))
nu = datetime.datetime.now()
jaar = int(nu.year)
maand = int(nu.month)
day = int(nu.day)

if a >= jaar - 17:
     print("u bent nog geen 18 \n nog geen alcohol voor jouw")
elif a == jaar - 18:
    m = int(input("geef uw geboortemaand"))
    if m == maand:
        d = int(input("geef uw geboortedag"))
        if d <= day:
            print("u mag alcohol drinken")
        else:
            print("nog geen 18")
    elif m <= maand:
        print("u mag alcohol drinken")
    else:
        print("nog geen 18")

else:
     print("u mag alcohol drinken")
