import calendar, datetime

nu = datetime.datetime.now()
jaar = int(nu.year)


m = int(input("welke maand? "))

if m >= 1 and m <= 12:
    print(calendar.month(jaar,m))