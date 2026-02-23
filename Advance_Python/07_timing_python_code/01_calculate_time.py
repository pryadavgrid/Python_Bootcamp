import time

def function_one(n):
    return [str(i) for i in range(n)]

def function_two(n):
    return list(map(str, range(n)))

current_time = time.time()
print(function_one(10))
print(f"Function Timing Is : {time.time()-current_time}")

current_time = time.time()
print(function_two(10))
print(f"Function Timing Is : {time.time()-current_time}")