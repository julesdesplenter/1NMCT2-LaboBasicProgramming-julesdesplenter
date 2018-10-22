def schrikkel(a):
    if(a % 4 == 0):
        print("dit is een schrikkeljaar")
    else:
        print("geen schrikkeljaar")

def remafstand(snelheid,reactietijd,remvertraging):
    a = int(snelheid)/3.6
    a = int(a) * int(reactietijd) + (a)**2 / (2 * int(remvertraging))
    print(a)

def middelpunt(x1,y1,x2,y2):
    x = (int(x1)+int(x2))/2
    y = (int(y1)+int(y2))/2
    print("({0},{1})".format(x,y))

# a = int(input("geef een getal"))
def faculteit(n):
    if n == 0:
        return 1
    else:
        return n * faculteit(n - 1)


print(faculteit(5))
