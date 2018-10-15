a = input("wat is jouw e mailadres?")

atPlaats = a.find("@")
puntPlaats = a.find(".")

if a[atPlaats:len(a)] == "@student.howest.be":
    if(puntPlaats < atPlaats):
        print("goed e-mailadress")
    else:
        print("slechte e-mail")
else:
    print("slechte e-mail")









