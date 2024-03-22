def factorial(n):
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n-1)
number=int(input("enter a number:"))
print(f"The factorial of {number} is {factorial(number)}.")
