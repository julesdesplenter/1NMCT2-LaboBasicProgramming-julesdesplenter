
seconden = int(input("wat is het aantal seconden? "))

dagen = (seconden - (seconden%86400))/86400

seconden = seconden % 86400

uren = (seconden - (seconden%3600))/3600

seconden = seconden%3600

minuten = (seconden - (seconden%60))/60

seconden = seconden%60

print("dat zijn {0} dagen \n  {1} uren \n  {2} minuten \n en  {3} seconden".format(dagen,uren,minuten,seconden))

