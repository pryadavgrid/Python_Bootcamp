# Create a recurcive function to calculate the factorial of number

# Factorial of 5 =  5*4*3*2*1 = 120

def factorial_of_number(num):
    if num == 1:
        return 1
    elif num>1:
        return (num * factorial_of_number(num-1))
                # 5 * (factorial_of_number(4))
                #           4 *(factorial_of_number(3))
                #                   3 * (factorial_of_number(2))
                #                           2 * (factorial_of_number(1))
                #                                   1 
                # 5 * 4 * 3 * 2 * 1
    else:
        return 

print(factorial_of_number(5))