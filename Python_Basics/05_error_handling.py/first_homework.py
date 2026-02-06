
# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except Exception as e:
#     print(f"Error : {e}")
# finally:
#     print("It's Done!!")


# Problem 2
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

# x = 5
# y = 0

# try:
#     z = x/y
#     print(f"Z : {z}")
# except Exception as e:
#     print(f"Error : {e}")
# finally:
#     print("All Done!!")


# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            user_input = int(input("Enter an integer : "))
        except Exception as e:
            print(f"You Enter Wrong Value, Please Enter Correct Value\nError : {e}")
            continue
        else:
            print(f"You Enter : {user_input}")
            break
        finally:
            print("All Is Done!!")



ask()
