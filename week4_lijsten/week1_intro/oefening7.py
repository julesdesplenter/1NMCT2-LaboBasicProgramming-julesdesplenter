
dagen = int(input("geef het aantal dagen "))
uren = int(input("geef het aantal uren "))
minuten = int(input("geef het aantal minuten "))
seconden = int(input("geef het aantal seconden "))

aantalSeconden = (dagen*24*60*60) + (uren*60*60) + (minuten*60) + seconden

print ("dat is gelijk aan: {0} seconden" .format(aantalSeconden))