import timeit

# syntax
# timeit.timeit(stmt, setup, timer, number, globals)
# stmt : statement -> The code you want to measure, Must be given as string
# setup : Code that runs before timing starts, most of use if my stmt use any other module and for run this function, function need some import module otherwise we pass stmt (statement) defination or "from __main__ import my_function"
# timer : Function used for timing, Default: time.perf_counter(), Normally you do NOT change this.
# number : How many times the code will run
# globals : Used to pass global variables, if my function (stmt) take any global variable, globals=globals()


import timeit

def my_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

execution_time = timeit.timeit(
    stmt="my_function()",
    # setup='''def my_function():
    #     total = 0
    #     for i in range(1000000):
    #         total += i
    #     return total
    # ''',
    setup="from __main__ import my_function",
    number=100
)

print("Execution Time:", execution_time)

