
nmct = {"1NMCT": 131, "2NMCT": 88, "3NMCT": 77}
devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}

print(nmct)
print(nmct["1NMCT"])
nmct["4NMCT"] = "yolo"
print(nmct)
nmct["4NMCT"] = "yolo2"
if "4NMCT" in nmct:
    print("hij zit erin")
else:
    print("bestaat niet")
del(nmct["4NMCT"])
nmct.pop("3NMCT", "none")
print(nmct)