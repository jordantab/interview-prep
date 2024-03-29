'''
Cracking the Coding Interview: Arrays and String 1.4
Problem: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is 
the same forwards and backwards
Author: Jordan Tab
'''

def palindrome_permutation(string):
    '''
    A palindrome can have at most one letter with an odd number of occurence. Since order doesn't matter for permutation, check total odd_count
    '''
    s = string.lower()
    s = s.replace(" ","")
    d = {}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    odd_count = 0
    for char in d:
        if d[char] % 2 == 1:
            odd_count += 1
    if odd_count > 1:
        return False
    else:
        return True

# print(palindrome_permutation("ajbdfj"))
# print(palindrome_permutation("tact coa"))
# print(palindrome_permutation("racecar"))

def pp(s):
    clean_s = s.replace(" ","")
    hashT = {}

    for letter in clean_s:
        if letter not in hashT:
            hashT[letter] = 1
        else:
            hashT[letter] += 1

    odd_counter = 0
    for letter in hashT:
        count = hashT[letter]
        if count % 2 == 1:
            odd_counter += 1
    
    if odd_counter > 1:
        return False
    else:
        return True

print(pp("ajbdfj"))
print(pp("tact coa"))
print(pp("racecar"))