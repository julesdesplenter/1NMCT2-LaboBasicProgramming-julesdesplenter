def swap(a,b):
    new_a = b[0:2] + a[2:]
    new_b = a[:2] + b[2:]
    return(new_a + " " + new_b)
print(swap("rezjr","ozrr"))