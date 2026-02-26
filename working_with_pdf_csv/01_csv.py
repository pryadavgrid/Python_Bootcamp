import csv

data = open('my_file.csv', encoding='utf-8')
csv_data = csv.reader(data)
# print(csv_data) # <_csv.reader object at 0x102626420>

data_line = list(csv_data) # convert data into list
# print(data_line) # return list of list all row (first list contain column name)
# print(len(data_line)) # how many row in my data

# all_name = []
# make_email = []
# for i in data_line[1:20]:
    # all_name.append(i[0])
    # email = f'{i[0].replace(' ','_').lower()}@gamail.com'
    # make_email.append(email)


# print(all_name)
# print(make_email)


# create a file object open('FILE_NAME', 'MODE', 'NEW_LINE')
new_csv_file_obj = open('updated_csv_file.csv', 'w', newline='')

# write csv file csv.writer('FILE_OBJECT', 'Separated')
csv_witer = csv.writer(new_csv_file_obj, delimiter=',')

# we can write a single row
# csv_witer.writerow([1,2,3,4])

# we can write multiple row using list of list
csv_witer.writerows([[1,2,3,4],[5,6,7,8]])

# at the end we need to close the file
new_csv_file_obj.close()