'''
Cracking the Coding Interview: Arrays and String 1.1
Problem: Check if a string has all unique characters
Author: Jordan Tab
'''

# with a hash table
def isU1(s):
    '''
    checks if a string has all unique characters using additional data structures
    '''
    # create a hash table and add unique characters
    hashT = {}
    for char in s:
        if char not in hashT:
            hashT[char] = 1
        # character already in table = not unique
        else:
            return False
    return True

print(isU1("String"))
print(isU1("Boston"))

def isU2(s):
    '''
    checks if a string has all unique characters without using additional data structures
    '''
