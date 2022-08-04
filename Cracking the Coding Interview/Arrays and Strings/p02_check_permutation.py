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
