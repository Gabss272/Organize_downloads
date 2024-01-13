import os
import shutil

from_dir = "C:/Users/DELL/Downloads"
to_dir = "C:/Users/DELL/Downloads/Documents_files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == ' ':
        continue
    if extension in ['.jpg', '.jpeg', '.png', '.gif', '.jfif']:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "Document_files"
        path3 = to_dir + "/" + "Document_files" + "/" + file_name

        if os.path.exists(path2):
            print("moviendo " + file_name + ".....")
            shutil.move(path1, path3)

        else: 
            os.makedirs(path2)
            print("moviendo " + file_name + ".....")
            shutil.move(path1, path3)
    
    