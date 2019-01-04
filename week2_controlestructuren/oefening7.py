stra = input("geef mij een string")
strb = input("geef mij een string")

# if (str.upper(stra) == str.upper(strb)):
#     print("gelijk ")
# else:
#     print("niet gelijk ")

if (isinstance(stra,str)and isinstance(strb,str)):
    if stra.lower() == strb.lower():
        print("gelijk")
    else:
        print("niet gelijk")