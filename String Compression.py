def compression(s):
    string = s[0]
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            string += str(count)
            string += s[i+1]
            count = 1
    string += str(count)
    return string

print(compression("abcccccccc"))

