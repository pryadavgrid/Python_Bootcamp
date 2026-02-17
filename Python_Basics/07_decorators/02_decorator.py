
def debug(func):
    def wrapper(*args, **kwrgs):
        args_value = ', '.join(str(arg) for arg in args)
        kwrgs_value = ', '.join(f"{key},{value}" for key, value in kwrgs.items())
        print(f"Calling {func.__name__}, With args {args_value}, With kwrgs {kwrgs_value}")
        result = func(*args, **kwrgs)
        return result

    return wrapper






@debug
def greet(name, greeting='Hello'):
    print(f"{greeting}, {name}")


greet("Prateek", greeting="Hanji")


@debug
def hello():
    print("Hello")

hello()