import re

def my_read_file():
    try:
        with open('sample_log.txt', 'r') as file:
            text = file.read()
        
        return True, text
    except Exception as e:
        return False, e
    
def log_statics(my_data):

    total_clint_error = 0
    total_server_error = 0
    total_success = 0
    for status_code in my_data:
        line_status_code = int(status_code[7])
        # print(status_code)
        if line_status_code == 200:
            total_success = total_success + 1
        elif line_status_code >= 400 and line_status_code < 500:
            total_clint_error = total_clint_error + 1
        else:
            total_server_error = total_server_error + 1

    print(f"Total request      → {total_clint_error+total_server_error+total_success}")
    print(f"Total Success      → {total_success}")
    print(f"Total Clint Error  → {total_clint_error}")
    print(f"Total Server Error → {total_server_error}")


def top_ips(my_dict):
    ip_and_count = sorted(my_dict.items(), key=lambda item : item[1], reverse=True)

    how_many_ip = int(input("How many top IP you want : "))

    print(f"----- Top {how_many_ip} IP are ----- ")
    
    for index, value in enumerate(ip_and_count[:how_many_ip]):
        print(f"{index+1}. {value[0]}       → {value[1]} requests")


def count_endpoints(line_data):
    my_dict = {}
    for i in line_data:
        if i[5] in my_dict.keys():
            my_dict[i[5]] = my_dict[i[5]] + 1
        else:
            my_dict[i[5]] = 1
    
    for key, val in my_dict.items():
        print(key, " → " , val)
    

status, file = my_read_file()
if status == False:
    print("Something went wrong")
else:


    while status == True:
        log_file_data = file.split('\n')
        unique_data = []
        my_ip_dict = {}
        my_line_data = []

        pattern = r'\d+\.\d+\.\d+\.\d+'
        for line in log_file_data:
            if not line:
                continue

            my_line_data.append(line.split())
            data = re.search(pattern, line)
            line_ip = data.group()
            if line_ip not in unique_data:
                unique_data.append(line_ip)
                my_ip_dict[line_ip] = 1
            else:
                my_ip_dict[line_ip] = my_ip_dict[line_ip] + 1
                
        my_input = int(input('1. Log Stattics\n2. Top IP\n3. All Endpoint\nEnter A number : '))

        if my_input == 1:
            print("\n" + "-"*5 +  "Log Stattics" + "-"*5 +  "\n")
            log_statics(my_line_data)
            print("--"*10 + "\n")
        elif my_input == 2:
            print("\n","-"*5, "Top IP", "-"*5, "\n")
            top_ips(my_ip_dict)
            print("--"*10, "\n")
        elif my_input == 3:
            print("\n","-"*5, "All Endpoint", "-"*5, "\n")
            count_endpoints(my_line_data)
            print("--"*10, "\n")
        else:
            print("Wrong Input ")
            status = False
            break

