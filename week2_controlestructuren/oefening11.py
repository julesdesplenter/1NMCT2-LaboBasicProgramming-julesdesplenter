def maximum(a,b,c):
    if int(a)>int(b) and int(a)>int(c):
        print(int(c))
    elif int(b)>int(a) and int(b)>int(c):
        print(b)
    else:
        print(c)

maximum(7,3,9)
