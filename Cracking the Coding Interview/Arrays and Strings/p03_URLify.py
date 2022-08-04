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
    return "".join(str)

print(URLify("Mr John Smith"))
print(URLify("Mr John     Smith"))
print(URLify("     Mr John     Smith"))
print(URLify("     Mr John     Smi  th  "))

# using built-in replace function
def URLify2(s):
    s = s.replace(" ","%20")
    return s
    
print(URLify2("Mr John Smith"))
print(URLify2("Mr John     Smith"))
print(URLify2("     Mr John     Smith"))
print(URLify2("     Mr John     Smi  th  "))