def factorial(n):
    """Calculate the factorial of n."""
    if n < 0:
        raise ValueError("Factorial is defined")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)