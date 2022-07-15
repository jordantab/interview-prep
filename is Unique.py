#HashTable from scratch
def isUnique(s):
    alph_length = 26
    table = [0] * alph_length
    for char in s:
        index = ord(char) % alph_length
        table[index] += 1
        if table[index] > 1:
            return False
    return True

print(isUnique("String"))
print(isUnique("Boston"))
print(isUnique(""))
print(isUnique("abcdefghijklmnopqrstuvwxyza"))

#Dictionary Method
def isU(s):
    hashT = {}

    for char in s:
        if char not in hashT:
            hashT[char] = 1
        else:
            return False
    return True
        

print(isU("String"))
print(isU("Boston"))
