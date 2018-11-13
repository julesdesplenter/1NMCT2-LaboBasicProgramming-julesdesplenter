dic = {}

def read(file):
    f =  open(file, "r")
    for i in f.readlines():
        a = i.split(":")
        b = str(a[0])
        c = a[1:len(a)]
        c[len(c)-1] = c[len(c)-1].rstrip("\n")
        dic.update({b:c})
    return dic

def search(name,dict):
    sum = 0
    for i in dict.keys():
        if name in i:
            for a in dict[i]:
                sum += int(a)
            return("{0}: {1} \n {2}".format(i, dict[i], sum/len(dict[i])))




read("tekstbestanden/Scores.txt")
print(search("b",dic))