def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index  
    return -1 
arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
target = 110
result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} is present at index {result}.")
else:
    print(f"Element {target} is not present in the array.")
