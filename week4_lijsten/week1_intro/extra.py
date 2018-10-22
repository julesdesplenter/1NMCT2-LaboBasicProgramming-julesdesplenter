import datetime, math, sys, calendar

print(sys.version)
print(datetime.date.today())
print(math.pi)
jaartal = int(input("geef een jaartal"))
maand = int(input("geef een maand"))
print("dit is de kalender van maand: {0} en jaar {1}".format(maand,jaartal))

print(calendar.month(jaartal, maand))