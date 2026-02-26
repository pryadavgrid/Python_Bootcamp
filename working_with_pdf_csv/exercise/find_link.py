import csv

data = open('find_the_link.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_line = list(csv_data) # convert data into list

my_link = ''
my_index = 0

# print(data_line)
for i in data_line:
    my_link = my_link + i[my_index]
    my_index = my_index +1

print(my_link)
