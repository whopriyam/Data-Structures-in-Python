# partition function
def partition(ar, low, high):
  # making pivot the last element
  pivot = ar[high]
  i = low-1

  # putting all element smalller than pivot on one side
  for j in range(low, high):
    # element is smaller than pivot
    if (ar[j]<=pivot):
      # swap the element to put
      # all element smaller than
      # pivot on one side
      i=i+1
      ar[i], ar[j] = ar[j], ar[i]
  
  ar[i+1], ar[high] = ar[high], ar[i+1]
  return i+1


def quicksort(ar, low, high):
  if (low<high): #array can be further divide into subarrays
    q = partition(ar, low, high)
    # dividing the function into subarrays
    quicksort(ar, low, q-1)
    quicksort(ar, q+1, high)



a = [23, 2, 11, 51 ,13]
quicksort(a, 0, 4)
print(a)