# def kw(**kwargs):
#     print(kwargs)
#     for i in kwargs:
#         print(i)



# kw(name = "prateek", age = 24)

# def myfunc(my_str):
#     my_new_str = ""
#     for index,value in enumerate(my_str):
#         if index % 2==0:
#             my_new_str += value.upper()
#         else:
#             my_new_str += value.lower()
            
#     return my_new_str

# print(myfunc('Anthropomorphism'))



# import math


# def myfunc(radius):
#     sphere = 4/3*(math.pi*(radius**3))

#     return sphere

# print(myfunc(2))


# Write a function that checks whether a number is in a given range (inclusive of high and low)

# def ran_check(num,low,high):
#     if low < num < high:
#         return f"{num} is in the range between {low} and {high}"


# # Check
# print(ran_check(5,2,7))

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# def count_upper_lower(my_str):
#     upper_count = 0
#     lower_count = 0
#     for i in my_str :
#         if i.isupper():
#             upper_count += 1
#         elif i.islower():
#             lower_count += 1


#     return f"No. of Upper case characters :  {upper_count}\nNo. of Lower case Characters :  {lower_count}"

# print(count_upper_lower('Hello Mr. Rogers, how are you this fine Tuesday?'))

# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# def unique_list(lst):
#     return list(set(lst))


# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


# Write a Python function to multiply all the numbers in a list.
# def multiply(numbers):  
#     value_of_multiplication = 1
#     for i in numbers:
#         value_of_multiplication = value_of_multiplication * i

#     print(value_of_multiplication)


# multiply([1,2,3,-4])



# Write a Python function that checks whether a word or phrase is palindrome or not.

# def palindrome(s):
#     # solution-1
#     # return s== s[::-1]

#     # solution-2
#     my_new_str = ''
#     for i in s:
#         my_new_str = i + my_new_str

#     return s == my_new_str

# print(palindrome('helleh'))



# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

# import string

# def ispangram(str1, alphabet=string.ascii_lowercase):
#     for i in alphabet:
#         if i in str1:
#             continue
#         else:
#             return 'Not Pangram'
        
#     return 'Pangram'

# print(ispangram("The quick brown fox jumps over the lazy dog"))

# print(bool('False'))

# dateString = '2024-12-22'
# a,b,c = map(int,dateString.split('-'))
# print(a,b,c)


# defaultdict(int)

# re = 3 + 5 * 2 - 8 / 4
# print(re)

# mydict = {
#     'a' : 1,
#     'b' : 2
# }

# # print(mydict.get('c'))
# print(mydict['c'])


# scores = [10,20,30,50,100,110]
# my_list = ['Pass' if score >=59 else 'Fail' for score in scores]
# print(my_list)


# file = open('file.txt', 'w')

# file.writelines(['A','B'])

# import cmath
# print(cmath.phase())


# for i in range(1,10):
#     for j in range(1,10):
#         print(j)
#         if i==5 and j==5:
#             break

#     print("I : ", i)


# mys = "Hello, World!"
# new = "Python"
# new_str = mys[:5]+new +mys[12:]
# print(new_str)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

# def animal_crackers(text):
#     return text.split(" ")[0][0] == text.split(" ")[1][0]
# # Check
# print(animal_crackers('Levelheaded Llama'))
# # Check
# print(animal_crackers('Crazy Kangaroo'))


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

# def makes_twenty(n1,n2):
#     if (n1==20) or (n2 ==20) or (n1+n2==20):
#         return True
#     else:
#         return False
# # Check
# print(makes_twenty(20,10))
# # Check
# print(makes_twenty(2,3))



# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
 
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

# def old_macdonald(name):
#     str1,str2 = name[:3].capitalize(), name[3:].capitalize()
    
#     return str1+str2
    
# # Check
# print(old_macdonald('macdonald'))

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'


# def master_yoda(text):
#     my_new_str = text.split(" ")
#     return " ".join(my_new_str[::-1])

# # Check
# print(master_yoda('I am home'))
# # Check
# print(master_yoda('We are ready'))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

# def almost_there(n):
#     if (110 >= n >= 90)  or (190 <= n <= 210):
#         return True
#     else:
#         return False

# # Check
# print(almost_there(104))
# # Check
# print(almost_there(210))
# # Check



# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False


# def has_33(nums):
#     first_three_index = nums.index(3)
#     next_index_of = first_three_index + 1
#     if nums[next_index_of]==3:
#         return True
#     else:
#         return False

# # Check
# print(has_33([1, 3, 3]))
# # Check
# print(has_33([1, 3, 1, 3]))
# # Check
# print(has_33([3, 1, 3]))

# print(has_33([3, 3, 3]))


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

# def paper_doll(text):
#     new_text = ""
#     for i in text:
#         for j in range(3):
#             new_text = new_text + i

#     return new_text

# # Check
# print(paper_doll('Hello'))
# # Check
# print(paper_doll('Mississippi'))

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
# def blackjack(a,b,c):
#     sum_of_number = a+b+c

#     if sum_of_number > 21:
#         if 11 in (a,b,c):
#             return sum_of_number - 10
#         else :
#             return "BUST" 
        
#     return sum_of_number
# # Check
# print(blackjack(5,6,7))
# # Check
# print(blackjack(9,9,9))
# # Check
# print(blackjack(9,9,11))


# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14
# def summer_69(arr):
#     sum_of_number = 0
#     if (6 in arr) and (9 in arr):
#         sixth_index = arr.index(6)
#         ninth_index = arr.index(9)
#         for i in range(len(arr)):
#             # print(i, sixth_index, ninth_index)
#             if i >= sixth_index and i<=ninth_index:
#                 continue
#             else:
#                 sum_of_number = sum_of_number + arr[i]
#     else:
#         sum_of_number = sum(arr)
        
#     return sum_of_number

# # Check
# print(summer_69([1, 3, 5]))
# # Check
# print(summer_69([4, 5, 6, 7, 8, 9]))
# # Check
# print(summer_69([2, 1, 6, 9, 11]))


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

# def spy_game(nums):
#     my_arr =[0,0,7]
#     my_new_arr = []
#     n=0
#     for i in nums:
#         if i == 0 or i==7:
#             if my_arr[n] == i:
#                 my_new_arr.append(i)
#                 n=n+1

#     # print(my_new_arr, my_arr)
#     return my_arr == my_new_arr, 


        

# # Check
# print(spy_game([1,2,4,0,0,7,5]))
# # Check
# print(spy_game([1,0,2,4,0,5,7]))
# # Check
# print(spy_game([1,7,2,0,4,5,0]))



# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# By convention, 0 and 1 are not prime.

# def count_primes(num):
#     to_prime_number = 0
#     for i in range(2, num):
#         for j in range(2, i):
#             if i%j == 0:
#                 break
#         else:
#             to_prime_number = to_prime_number + 1
    
#     return to_prime_number

        
        
                
# # Check
# print(count_primes(100))

# print(len(10))