import pdb

def add_numbers(a, b):
    pdb.set_trace()   # Debugger will stop here
    result = a + b
    return result

print(add_numbers(5, 3))


# (Pdb) p a
# 5

# (Pdb) p b
# 3

# (Pdb) n



# n - Next line
# s - Step inside function
# c - Continue execution
# q - Quit debugger
# l - Show code
# p variable - Print variable value
# h - Help