# Problem Statement 
# Develop a program to backing Up a given Folder (Folder in a current working directory) into a ZIP File.

import os
import zipfile
from datetime import datetime

def backup_folder_to_zip(folder_name):
    folder_path= os.path.abspath(folder_name)
    timestamp= datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_filename= f"{folder_name)_(timestamp).zip"

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        for foldername, subfolders, filenames in os.walk(folder_path):
            backup_zip.write(foldername, os.path.relpath(foldername, folder_path))
            for filename in filenames:
                file_pathos.path.join(foldername, filename)
                backup_zip.write(file_path, os.path.relpath(file_path, folder_path))
    print (f"Backup complete! The folder (folder_name) has been backed up into (zip_filename)'.")

folder_name= input("Enter the name of the folder to back up: ")

if os.path.isdir(folder_name):
    backup_folder_to_zip(folder_name)
else:
    print (f"The folder '{folder_name}' does not exist in the current working directory.")

