'''
Cracking the Coding Interview: Arrays and String 1.6
Problem: Basic string compression using the countrs of repeated characters
    Example:
        aabcccccaaa -> a2b1c5a3
Author: Jordan Tab
'''

def compression(s):
    d = {}
    result = ""
    for i, char in enumerate(s):
        if i == 0:
            d[char] = 1
        else:
            if char in d and char != s[i-1]:
                d[char] += 1
                result += f'{s[i-1]}{d[s[i-1]]}'              
            elif char in d and char == s[i-1]:
                d[char] += 1  
            else:
                d[char] = 1
                result += f'{s[i-1]}{d[s[i-1]]}'
                d[s[i-1]] = 0
    result += f'{s[len(s)-1]}{d[s[len(s)-1]]}'
    return result
# print(compression("abccaa"))
# print(compression("abccccccc"))

def compress(s):
    output = ""
    table = {}

    for i,letter in enumerate(s):
        if i == 0:
            table[letter] = 1
        else:    
            if letter == s[i-1]:
                table[letter] += 1
            else:
                table[letter] = 1
                prev = s[i-1]
                output += prev
                output += str(table[prev])
                table[prev] = 0
        
    output += s[len(s)-1]
    output += str(table[s[len(s)-1]])
    return output


print(compress("abccaa"))
print(compress("abccccccc"))
