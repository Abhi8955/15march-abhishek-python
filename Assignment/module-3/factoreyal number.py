def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n == 0:
        return 1

    return n * factorial(n - 1)
try:
    n = int(input("Enter a non-negative integer: "))
    result = factorial(n)
    print(f"The factorial of {n} is {result}.")
except ValueError as e:
    print(str(e))
