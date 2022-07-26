def remove(string):
    return string.replace(" ","")
def palindrome_permutation(s):
    str = remove(s)
    hashT = {}
    for char in str:
        hashT[char] = 0
    for char in str:
        hashT[char] += 1
    even_count = 0
    for char in hashT:
        if hashT[char] % 2 == 0:
            even_count += 1
    print(even_count)
    if (even_count == len(hashT)) or (even_count == (len(hashT) - 1)):
        return True
    else:
        return False
print(palindrome_permutation("ajbdfj"))
print(palindrome_permutation("tact coa"))
print(palindrome_permutation("racecar"))
