
"""
    The following decorator function decorates the function and
    calculates the secs it has taken to complete.

"""

import time

current_time = time.time()
print(current_time)


# Uses as a decorator function
def speed_calc_decorator(func):
    def wrapper_function():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__} have taken {end_time - start_time} secs to complete.")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000):
        i * i


fast_function()
slow_function()
