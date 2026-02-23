import shutil
import os
my_file_for_zip = f"{os.getcwd()}/my_extract_files"
print(my_file_for_zip)
my_new_zip_file_name = 'using_shutil_module'

# shutil.make_archive(my_new_zip_file_name, 'zip' , my_file_for_zip)


shutil.unpack_archive('using_shutil_module.zip','unzip_using_shutil')