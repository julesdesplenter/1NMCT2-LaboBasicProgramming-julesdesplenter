i = 0
dic = {}
list = []

while i < 1:
    a = input("geef een feedbackscore tussen 5 en 0 ")
    if a.isdigit():
        a = int(a)
        if a >= 0 and a <= 5:
            list.append(a)
    else:
        i += 1

for i in list:
    dic.update({i: list.count(i)})


def printDictionary(dictionary):
    for key, value in dictionary.items():
        print("score: {0} aantal:{1}".format(key, value))


printDictionary(dic)
