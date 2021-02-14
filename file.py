import os
import shutil

#display the date
#print(os.system("date"))

#make dir
#os.mkdir('yash')

#check the current working dir
#print(os.getcwd())

#check that the path exists or not
# path = 'C:\ExampleWHJ'
# isExist = os.path.exists(path)
# print(isExist)

#split the path
path2 = 'file.py'
root_ext = os.path.splitext(path2)
print(root_ext)

list the dir
print(os.listdir())

#copy the contents
# path = 'yash'
# print("Before copying file")
# print(os.listdir(path))

# source = 'yash/yash1.py'

# destination = 'sample1/sample1.py'
# dest = shutil.copy(source,destination)

#move the files
# path = 'yash'
# print("Before moving files")
# print(os.listdir(path))

# source = 'yash/mp3'

# destination = 'sample1/mp4'
# dest = shutil.move(source,destination)