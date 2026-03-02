import re

# Read File

with open('sample_log.txt', 'r') as file:
    text = file.read()

log_file_data = text.split('\n')

def most_use_api(my_dict):
    ip_and_count = sorted(my_dict.items(), key=lambda item : item[1], reverse=True)
    how_many_ip = int(input("How many top IP you want : "))
    print(f"----- Top {how_many_ip} IP are ----- ")
    for i in ip_and_count[:how_many_ip]:
        print(f"{ip_and_count.index(i)}. {i[0]} → {i[1]} requests")


def count_endpoints(line_data):
    my_dict = {}
    for i in line_data:
        if i[5] in my_dict.keys():
            my_dict[i[5]] = my_dict[i[5]] + 1
        else:
            my_dict[i[5]] = 1
    
    for key, val in my_dict.items():
        print(key, "   → " , val)


        


# 192.168.1.2 - - [01/Jan/2026:10:00:00] “GET /products HTTP/1.1” 200

unique_data = []
my_ip_dict = {}
my_line_data = []

pattern = r'\d+.\d+.\d+.\d+'
for line in log_file_data:
    my_line_data.append(line.split())
    data = re.search(pattern, line)
    line_ip = data.group()
    if line_ip not in unique_data:
        unique_data.append(line_ip)
        my_ip_dict[line_ip] = 1
    else:
        my_ip_dict[line_ip] = my_ip_dict[line_ip] + 1


# most_use_api(my_ip_dict)

# print(len(my_line_data[0]))

total_clint_error = 0
total_server_error = 0
total_success = 0
for status_code in my_line_data:
    # print(status_code)
    if int(status_code[7]) == 200:
        total_success = total_success + 1
    elif int(status_code[7]) == 400 :
        total_clint_error = total_clint_error + 1
    else:
        total_server_error = total_server_error + 1

print(f"Total Success → {total_success}")
print(f"Total Clint Error → {total_clint_error}")
print(f"Total Server Error → {total_server_error}")


count_endpoints(my_line_data)