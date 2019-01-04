def maximum(a,b,c):
    if int(a)>int(b) and int(a)>int(c):
        print(int(c))
    elif int(b)>int(a) and int(b)>int(c):
        print(b)
    else:
        print(c)

def maxi(a,b,c):
    if isinstance(a,int) and isinstance(b,int) and isinstance(c,int):
        lijst = [a,b,c]
        print(max(lijst))



maximum(7,3,9)
maxi(1,2,3)
