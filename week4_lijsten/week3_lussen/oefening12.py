naam = input("geef je naam")
voornaam = input("geef je voornaam")
datum = input("geef je datum in dd-mm-jjjj")

a = naam[0:3]
b = voornaam[0:2].upper()
c = datum[0:2] + datum[3:5]

print(a+b+c)
