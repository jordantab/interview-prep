'''
Cracking the Coding Interview: Arrays and String 1.5
Problem: There are 3 ways to edit a string: replace a character, insert a character, delete a character. Given a string, write a function
to see if they are one or less edits away
    Example:
        - pale, ple -> True
        - pales, pale -> True
        - pale, bale -> True
        - pale, bake -> False
Author: Jordan Tab
'''

def insert(l,s):
    '''
    checks if the strings are one insertion or deletion away

    logic: insertion and deletion are the same thing. If two strings are one insertion away, you can add the missing character to the shorter
    string or delete it from the longer string
    '''
    count,i,j = 0,0,0
    while i < len(l) and j < len(s):
        if l[i] != s[j]:
            count += 1
            if count > 1:
                return False
            i += 1
        else:
            i += 1
            j += 1
    return True

def replace(s1,s2):
    '''
    checks if the strings of equal length are one replacement away

    logic: compares the corresponding characters of the strings and keeps track of number of unmatching characters
    '''
    count = 0
    for c1, c2 in zip(s1,s2):
        if c1 != c2:
            count += 1
            if count > 1:
                return False
    return True

def one_away(s1,s2):
    '''
    determines what edit is most likely

    logic: same length strings = replacement, 1 char away = insertion/deletion, neither = False
    '''
    if len(s1) == len(s2):
        return replace(s1,s2)
    elif len(s2) + 1 == len(s1):
        return insert(s1,s2)
    elif len(s1) + 1 == len(s2):
        return insert(s2,s1)
    else:
        return False

print(one_away('bale','bake')) # True
print(one_away('bale','bakr')) # False
print(one_away('bal','bale')) # True
print(one_away('bal','bake')) # False
print(one_away('bale','bal')) # True
print(one_away('bale','bak')) # False