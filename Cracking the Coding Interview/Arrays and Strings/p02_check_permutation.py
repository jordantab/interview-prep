'''
Cracking the Coding Interview: Arrays and String 1.2
Problem: Check if two strings are permutations of each other
Author: Jordan Tab
'''

#sort the strings and check if they're equal

def checkperm(s1,s2):
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    if s1_sorted == s2_sorted:
        return True
    else:
        return False

print(checkperm("abcced","deccba"))
print(checkperm("abccefeed","deccba"))


def check_permutation(s1,s2):
    '''uses hash tables and not built in functions'''
    hashT1 = {}
    hashT2 = {}

    for letter in s1:
        if letter not in hashT1:
            hashT1[letter] = 1
        else:
            hashT1[letter] += 1

    for letter in s2:
        if letter not in hashT2:
            hashT2[letter] = 1
        else:
            hashT2[letter] += 1

    len1 = len(hashT1)
    len2 = len(hashT2)

    if len1 != len2:
        return False
    else:
        for letter in hashT1:
            if letter not in hashT2:
                return False
            else:
                if hashT1[letter] != hashT2[letter]:
                    return False
    return True

print(check_permutation('awasd', 'dasaw'))
print(check_permutation('awasd', 'dasawf'))
print(check_permutation('awasd', 'dasac'))
print(check_permutation('awasd', 'daaaw'))

