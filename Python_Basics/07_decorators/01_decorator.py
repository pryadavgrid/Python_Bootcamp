import time


def timer(func):
    def wrapper(*args, **kwrgs):
        start_time = time.time()
        result = func(*args, **kwrgs)
        end_time = time.time()
        print(f"The Function {func.__name__}, ran in {end_time-start_time}")
        return result
    
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)