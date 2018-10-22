nieuweListGetallen = []
a = 1
while a <= 282:
    nieuweListGetallen.append(a)
    a = a+13

print(nieuweListGetallen)
nieuweListGetallen.reverse()
print(nieuweListGetallen)
nieuweListGetallen.reverse()
del nieuweListGetallen[0]
print(nieuweListGetallen)
nieuweListGetallen.remove(53)
print(nieuweListGetallen)
print(nieuweListGetallen[-1])
