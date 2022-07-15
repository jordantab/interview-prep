def One_Away(s1,s2):
    shorter = s1
    if len(s1) <= len(s2):
        shorter = s1
        longer = s2
    else:
        shorter = s2
        longer = s1

    if add_one(shorter,longer) and (len(shorter) + 1 == len(longer)):
        return True
    #if contains(shorter,longer)

def add_one(s1,s2):
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            print(i)
            continue
        else:
            return False
    return True

#def contains(s1,s2):


print(add_one("pal","pele"))
#print(One_Away("pele","pla"))

    
    