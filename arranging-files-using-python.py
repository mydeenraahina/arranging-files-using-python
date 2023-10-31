#arranging files
import os
from os import path
def Arranging_files(path_used):
    files_listed=os.listdir(path_used)#listing the files & folders in the given path
    ext=[]
    for files in files_listed:
        fileext_path=path.join(path_used,path.splitext(files)[1][1:])
        if fileext_path in ext:
            pass
        else:
            ext.append(fileext_path)#add the unique files along with their path in ext[](list)for creating a folder
    for folder in ext:
        try:
            os.mkdir(folder)#creating folder
        except FileExistsError:
            print("file already exists")
        for files in files_listed:
            if path.split(folder)[1]==path.splitext(files)[1][1:]:
                os.rename(path.join(path_used,files),path.join(folder,files))#moving files in the folder
Arranging_files(r"C:\Program Files (x86)\Java\jdk1.5.0_06\bin")



