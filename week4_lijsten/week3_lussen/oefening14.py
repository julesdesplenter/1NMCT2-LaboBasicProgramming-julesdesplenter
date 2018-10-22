import random
import string

def password(min,max):
    i = 0
    password = ""
    length = random.randrange(int(min), int(max) + 1)
    print("gekozen lengte {0}".format(length))
    while i <= length:
     password += random.choice(string.ascii_letters)
     i = i + 1
    return password


print(password(5,7))



