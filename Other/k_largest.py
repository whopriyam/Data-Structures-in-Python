#Write an efficient program for printing k largest elements in an array. Elements in array can be in any order (Amazon question)
def largest(arrayList,k):
    arrayList.sort(reverse=True)
    for i in range(k): 
            print (arrayList[i], end =" ")
            
print (largest([1, 23, 12, 9, 30, 2, 50],3 ))