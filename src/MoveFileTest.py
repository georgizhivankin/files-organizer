import os
import shutil

def mover(dir):
        parrent_path, name = os.path.split(dir)
        ext = name.split('.')[1]
    
        if os.path.exists('C:\\Users\\djgeorgie\\Desktop\\' + ext):
            shutil.move(dir, 'C:\\Users\\djgeorgie\\Desktop\\' + ext);
        else:
            os.makedirs('C:\\Users\\djgeorgie\\Desktop\\' + ext)
            shutil.move(dir, 'C:\\Users\\djgeorgie\\Desktop\\' + ext)

# print os.path.split("C:\Users\ibotev\Desktop\Oak\141217 Project Oak Steering Group Meeting20.pdf")[1]
mover("C:\\Users\\djgeorgie\\Documents\\asdf.docx")
