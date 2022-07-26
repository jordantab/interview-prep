'''
Cracking the Coding Interview: Arrays and String 1.3
Problem: Replace all spaces with %20
Author: Jordan Tab
'''
# convert the string into a list and check each index
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
