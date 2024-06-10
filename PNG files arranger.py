import os
extention = input('Enter a valid extention name like .png, .pdf : ')
path = input('Enter the path of the files: ')
# extention = '.png'
#path = 'D:\\New folder'
files = os.listdir(path)
i=1
for file in files:
    if file.endswith(extention):
        os.rename(f'D:\\New folder\\{file}',f'D:\\New folder\\{i}{extention}')
        print(f'D:\\New folder\\{file} renamed')
        i+=1
        
#This code will rename your files from 1 to n where n is the number of files 
# in your folder or the type of entered extension.