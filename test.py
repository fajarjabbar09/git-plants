def factorial(n):
    """Calculate the factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers and will raise an error.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)