import zipfile

comp_file = zipfile.ZipFile("my_compress_file.zip", 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()


# create a zipfile object and open in readmode
zip_obj = zipfile.ZipFile("my_compress_file.zip", 'r')

# when we want to extraxt all file in a single folder then we give only new name inside the ZIP_FILE_OBJECT.extractaall('ZIP_FILE_NAME')
# zip_obj.extractall('my_extract_files')

# when we wanrt give me a single file fron zip folder then we give new_file_name and file_name which we want to extract from zip file
# ZIP_FILE_OBJECT.extract('FILE_NAME_WHICH_WE_WANT_TO_ACCESS', 'FOLDER_NAME_WHERE_WE_WANT_TO_UNZIP')
# zip_obj.extract('fileone.txt', 'my_one_file')
