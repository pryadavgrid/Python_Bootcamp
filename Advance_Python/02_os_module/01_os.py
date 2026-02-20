# my_file = open('my_text_file.txt', 'w+')
# my_file.write("This Is My Text File")
# print(my_file.readline())

import os

# Return 'Current Working Directory'
# print(os.getcwd())

# Return a list of all folders and file which is present in current working directory
# print(os.listdir())

# Also We can give a path and it return the list of file and folder
# print(os.listdir(f'/Users/pryadav/Desktop/Grid_Dynamic_Internship_Programm/Python_Bootcamp'))

# Delete the File Permanent 
# os.unlink('PATH_WITH_FILE_NAME')

# Delete the whole folder permanennt
# os.rmdir('PATH_OF_DIR')

# Note : os.unlink() and os.rmdir()  -> remove permanent file/folder but when we want to move file into trash bin


# Purpose: os.walk() is used to go through all folders and files inside a directory, including subfolders.

# It is like a robot walking through a folder, checking every folder and file inside it.
# What it gives you: For each folder, os.walk() returns 3 things:
# folder path – the current folder’s address
# folder names – a list of all subfolders inside that folder
# file names – a list of all files inside that folder

# for folder, sub_folder, directory in os.walk(os.getcwd()):
for folder, sub_folder, directory in os.walk("/Users/pryadav/Desktop/Grid_Dynamic_Internship_Programm/Python_Bootcamp/Advance_Python"):
    print(f"Folder {folder}" )
    print("sub_folder")
    for sub_f in sub_folder:
        print(f"\t{sub_f}")
    
    print("directory")
    for dirc in directory:
        print(f"\t{dirc}")

    print("\n")