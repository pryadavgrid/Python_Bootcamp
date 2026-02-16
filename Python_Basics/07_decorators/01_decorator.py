# my_decorator takes a function definition
def my_decorator(fun):

    # wrapper takes function arguments
    def wrapper(*args, **kwrgs):

        # Extra logic (age check)
        if args[1] == 25:
            return fun(*args, **kwrgs)
        
        return "You are not eligible"
    
    return wrapper


@my_decorator
def my_functions(name, age):
    print("This Is A Function")
    return f"Hello {name}, Your age is {age}"


print(my_functions("Prateek", 25))


# How Decorator Works Behind the Scene
# same work from line 19-20, We can use using @my_decorator
# my_fun = my_decorator(my_functions)
# print(my_fun("Prateek", 25))



