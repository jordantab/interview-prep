def URLify(s):
    str = list(s)
    for i in range(len(str)):
        if str[i] == " ":
            str[i] = "%20"
        else:
            continue
    return "".join(str)
print(URLify("Mr John Smith"))
print(URLify("Mr John     Smith"))
print(URLify("     Mr John     Smith"))
print(URLify("     Mr John     Smi  th  "))