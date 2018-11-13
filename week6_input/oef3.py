
def fill(file):
    f = open(file, "a")
    f.write("\n")
    while True:
        i = str(input("nieuwe lijn s is stop"))
        if i == "s":
            return False
        else:
            f.write(i + "\n")

fill("test.txt")