
def even(min = 0,max = 0, i = 0):
    min = int(input("geef het kleinste getal met twee cijfers"))
    max = int(input("geef het grootste getal met twee cijfers"))
    result =  ""
    for i in range(min,max):
        c = str(i)
        a = str(c[0])
        b = str(c[1])
        if a == "2" or a == "0" or a == "4" or a == "6" or a == "8":
            result += c + ", "
        elif b == "2" or b == "0" or b == "4" or b == "6" or b == "8":
           result += c + ", "
    return result

print(even())