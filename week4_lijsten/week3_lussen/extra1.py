a = 1
b = 1
print("0")
while a <= 50:
    if b <= 50:
        print(a)
        print(b)
        a = a + b
        b = b + a
    else:
        print(a)
        a = a + b

