from numbers import Integral


def typesafe_fib(n):
    """Return the n-th Fibonacci number, raising an exception if a
    non-integer is passed as n."""
    if not isinstance(n, Integral):
        raise TypeError(
            f"fib expects an integer, not a {type(n).__name__}"
        )
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return typesafe_fib(n-2) + typesafe_fib(n-1)
