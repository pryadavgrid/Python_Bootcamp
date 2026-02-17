# Implement a decorator that caches the return value of a function, so that when it's called with the same arguments, the cached value is return instead of re-executing the function.
import time


def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args, **kwrgs):
        if args in cache_value:
            return cache_value[args]
        else:
            result = func(*args, **kwrgs)
            cache_value[args] = result
            return result

    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a + b

print(long_running_function(1,2))
print(long_running_function(1,2))
print(long_running_function(1,2))
print(long_running_function(1,2))


