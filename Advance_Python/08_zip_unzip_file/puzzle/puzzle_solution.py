import shutil
import os
import re

# my_zip_file_location = f'{os.getcwd()}/using_shutil_module.zip'
# my_unzip_file_name = 'unzip_shutil_zip_file'

# shutil.unpack_archive(my_zip_file_location, my_unzip_file_name)

# with open('unzip_shutil_zip_file') as f:
#     print(f.read())


for folder, sub_folder, files in os.walk(f'{os.getcwd()}/unzip_shutil_zip_file'):
    for file in files:
        with open(f'{folder}/{file}', 'r') as f:
            my_text = f.read()
            # print(my_text)
            result  = re.findall(r'\d+-\d+-\d+', my_text)
            if result :
                print(result)