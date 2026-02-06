# my_dict = {
#     1 : "A",
#     2 : "B",
#     3 : "C"
# }

# # print(my_dict.keys())
# # print(my_dict.values())

# for key, val in my_dict.items():
#     print(f"Key {key}, Value {val}")

# my_set = {'a','b', 'c',1,2, 'a'}
# print(my_set)


# a = 4 * (6 + 5) 
# # 44
# b = 4 * 6 + 5
# # 29
# c = 4 + 6 * 5
# # 34

# print(a,b,c)

# result = 3 + 1.5 + 4
# print(result, type(result))

# Getting a little tricker
# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# print(d['k1'][0]['nest_key'][1][0])

#Grab hello
# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# print(d['k1'][2]['k2'][1]['tough'][2][0])

# list5 = [1,2,2,33,4,4,11,22,3,3,2]
# print(set(list5))

# print(4**0.5 != 2)
# my_list1 = [1,2,3,4]
# my_list2 = ['a','b','c','d']
# my_list3 = ['w','x','y']

# for i in zip(my_list1,my_list2,my_list3):
#     print(i)


import random

# my_list = [1,2,3,4,5,6,7,8,9,0]
# # random.choice is return a item from list
# print(random.choice(my_list))

# # random.shuffle return entire list after change the order of elements
# random.shuffle(my_list)
# print(my_list)

# my_list = ['O',' ', ' ']

# while True:
#     user_choice = int(input('Choose a number : '))
#     if user_choice < 0 or user_choice>2:
#         print("You Choose Wrong Number!!")
#         break
#     else:
#         random.shuffle(my_list)
#         # if user_choice == my_list.index('O'):
#         if my_list[user_choice]== 'O':
#             print("You Win !!", my_list)
#             break
#         else:
#             print("Sorry!!", my_list)


