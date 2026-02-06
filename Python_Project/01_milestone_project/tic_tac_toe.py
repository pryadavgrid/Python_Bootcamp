import random
# first_row = [' ', ' ', ' ']
# second_row = [' ', ' ', ' ']
# third_row = [' ', ' ', ' ']

# def system_turn(f1,f2,f3, ins = 'O'):
#     cmp_rw_input = random.randint(1,3)
#     cmp_clm_input = random.randint(1,3)
#     while True:

#         if cmp_rw_input ==1:
#             if f1[cmp_clm_input-1] == ' ':
#                 f1[cmp_clm_input-1] = ins
#                 break
#             else:
#                 cmp_rw_input = random.randint(1,3)
#                 cmp_clm_input = random.randint(1,3)
#                 continue
#         elif cmp_rw_input ==2:
#             if f2[cmp_clm_input-1] == ' ':
#                 f2[cmp_clm_input-1] = ins
#                 break
#             else :
#                 cmp_rw_input = random.randint(1,3)
#                 cmp_clm_input = random.randint(1,3)
#                 continue
#         else:
#             if f3[cmp_clm_input-1] == ' ':
#                 f3[cmp_clm_input-1] = ins
#                 break
#             else :
#                 cmp_rw_input = random.randint(1,3)
#                 cmp_clm_input = random.randint(1,3)
#                 continue
        

#     return f1,f2,f3



# while True:
#     user_input_row = int(input('Enter The Row Number B/W 1-3 and 0 for Exit Game : '))
#     user_input_column = int(input('Enter The Column Number B/W 1-3 and 0 for Exit Game : '))
    
#     if user_input_column > 3:
#         print("You Enter Wrong Column Value!!, Please Enter The Value B/W 1-3")
#         continue
#     elif user_input_row > 3:
#         print("You Enter Wrong Row Value!!, Please Enter The Value B/W 1-3")
#         continue
#     elif user_input_column <=0 or user_input_row<=0:
#         print("You Quit The Game")
#         break
#     else:
#         if user_input_row ==1:
#             first_row[user_input_column-1] = 'X'
#         elif user_input_row == 2:
#             second_row[user_input_column-1] = 'X'
#         else :
#             third_row[user_input_column-1] = 'X'

#         # f1,f2,f3 = system_turn(first_row, second_row, third_row, ins = 'X')
#         f1,f2,f3 = system_turn(first_row, second_row, third_row)
#         first_row = f1
#         second_row = f2
#         third_row = f3
    
#     print(first_row)
#     print(second_row)
#     print(third_row)

#     for i in range(3):
#         if first_row[i] == 'X':
#             continue
#         if second_row[i] == 'X':
#             continue
#         if third_row[i] == 'X':
#             continue
#         else:
#             break
#     else:
#         print('You Win!!')
#         break


        

# # tic_tac_toe(first_row,second_row,third_row)

def update_user(val):
    i=0
    while i<19:
        com_input = random.randint(1,9)
        if val[com_input] == ' ':
            val[com_input] = 'O'
            break
        else:
            i= i+1
            continue

    return val

def check_win(tic_tac, check):
    if check == tic_tac[1]:
        if (tic_tac[2] == check and tic_tac[3]==check) or (tic_tac[4] == check and tic_tac[7]== check) or (tic_tac[5] == check and tic_tac[9]==check):
            # print('You Win')
            return True
    if check == tic_tac[2]:
        if(tic_tac[5] == check and tic_tac[8]==check):
            # print('You Win!!')
            return True
    if check == tic_tac[3]:
        if(tic_tac[5] == check and tic_tac[7]==check) or (tic_tac[6] == check and tic_tac[9]==check):
            # print('You Win!!')
            return True
    if check == tic_tac[4] and check == tic_tac[5] and check == tic_tac[6]:
        return True
    if check == tic_tac[7] and check==tic_tac[8] and check == tic_tac[9]:
        return True
        
    
    return False

tic_tac_toe = ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
who_win  = False
who_win_2 = False
while True:
    user_input = int(input("Enter Your Number : B/W 1-9 : "))
    if tic_tac_toe[user_input] == ' ' : 
        tic_tac_toe[user_input] = 'X'
    else:
        print("You Enter Wrong Number Try Again")
        continue

    who_win = check_win(tic_tac_toe, 'X')
    if not who_win:
        tic_tac_toe = update_user(tic_tac_toe)
        who_win_2 = check_win(tic_tac_toe, 'O')
        
        

    
    print(tic_tac_toe[7] + ' | ' + tic_tac_toe[8] + ' | ' + tic_tac_toe[9] )
    print(tic_tac_toe[4] + ' | ' + tic_tac_toe[5] + ' | ' +  tic_tac_toe[6] )
    print(tic_tac_toe[1] + ' | ' + tic_tac_toe[2] + ' | ' +  tic_tac_toe[3] )


    if who_win:
        print("You Win!!")
        break
    elif who_win_2:
        print("System Win!!")
        break
    elif ' ' not in tic_tac_toe:
        print("!!!Match Draw!!!")
        break

    # 1,4,7 | 2,5,8 | 3,6,9 | 1,2,3| 4,5,6| 7,8,9| 1,5,9| 3,5,7|

    