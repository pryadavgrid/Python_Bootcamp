# first_number = input("Please Enter Number : ") 
first_number = int(input("Please Enter Number : "))
second_number = int(input("Please Enter Number : "))

try:
    total = first_number + second_number
except Exception as e:
    print(e)
else:
    print(f"Sum Is {total}")
finally:
    print("Finnaly block")
