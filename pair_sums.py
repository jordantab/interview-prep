

def numberOfWays(arr, k):
   # Write your code here
    hashT = {}
    count = 0
    for num in arr:
        hashT[num] = 0
    for num in arr:   
        hashT[num] += 1
    print(hashT)
    for num in hashT:
        if (k-num) in hashT:
            if (k-num) == num:
                count += (hashT[k-num]*(hashT[k-num]-1))/2
            else:
                count += (hashT[k-num]*hashT[num])
    return (count/2) 


print(numberOfWays([0,10,12,2,5,7,5],12))
print(numberOfWays([1,2,3,4,3],6))
print(numberOfWays([1, 5, 3, 3, 3],4))