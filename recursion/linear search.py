
def linear_search(arr, i, key):
    if i == -1:
        return -1
    if arr[i] == key:
        return i
    else:
        return linear_search(arr, i - 1, key)
arr = [10,20,80,30,50]
x = 11
result = linear_search(arr, len(arr) - 1, x)
if result != -1:
    print(f"Element {x} is present at index {result}.")
else:
    print(f"Element {x} is not present in the array.")
