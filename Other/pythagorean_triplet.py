#Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2 (Amazon question)

def isTriplet(ar, n): 
    ar.sort() 
    for i in range(n-1, 1, -1): 
        j = 0
        k = i - 1
        while (j < k): 
            if (ar[j]*ar[j] + ar[k]*ar[k] == ar[i]*ar[i]): 
                return [ar[j],ar[k],ar[i]]
            else: 
                if (ar[j]*ar[j] + ar[k]*ar[k] < ar[i]*ar[i]): 
                    j = j + 1
                else: 
                    k = k - 1
    return False

print(isTriplet([3, 1, 4, 6, 5] ,len([3, 1, 4, 6, 5] )))