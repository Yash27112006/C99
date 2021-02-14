import os
import shutil

source = input("Enter the source folder name: ")
destination = input("Enter the destination folder name: ")

source+='/'
destination+='/'

listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)
