def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
               temp=arr[j]
               arr[j]=arr[j+1]
               arr[j+1]=temp
arr = [6,5,4,3,2,1]
bubble_sort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i], end=" ")
