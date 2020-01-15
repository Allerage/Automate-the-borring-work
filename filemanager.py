import os
from os import path
import shutil
from progressbar import ProgressBar
os.chdir(r'C:\Users\Allerage\Desktop\jkart\pictures')
directory=os.getcwd()
print(directory)
# path_images='F:\\images' #add your own path where you want to move images
# path_videos='F:\\Videos'# add Your own path where you want to move videos
# path_documents='F:\\D'# add Your own path where you want to move documents
# path_software='F:\software'
# pbr=ProgressBar()
path_images=directory+'\\Shorted_Images'
path_documents=directory+"\\Shorted_documents"
def Create_Empty_Folder():
    if not (path.exists('Shorted_Images')):

        os.mkdir(path_images, 0o777)
    if not(path.exists('Shorted_Documents')):
        os.mkdir(path_documents, 0o777)




def sort_images():
    # Extension for documents file feel free to add if missed
    for i in os.scandir(directory):
        if (i.path.endswith(".jpg") or i.path.endswith(".png") or i.path.endswith(".JPG") ) and i.is_file():
            print(i.path)
            try:
                shutil.move(i.path, path_images)
            except:
                pass



def sort_videos():
    for v in os.scandir(directory):
        if (v.path.endswith(".mkv") or v.path.endswith(".avi")) and v.is_file():
            print(v.path)
            shutil.move(v.path,path_videos)
def sort_document():
    # Extension for documents file feel free to add if missed
    doc_exte=[".doc",".pdf",".docx",".odt",".rtf",".tex",".txt",".wks",".wps",".wpd"]
    for d in os.scandir(directory):
        for m in doc_exte:
            if(d.path.endswith(m)):
                try:
                    shutil.move(d.path, path_documents)
                except:
                    pass


def sort_software():
    # Extension for documents file feel free to add if missed
    soft_exte=[".exe",".iso",".rar"]
    for s in os.scandir(directory):
        for so in soft_exte:
            if(s.path.endswith(so)):
                try:
                    shutil.move(s.path, path_software)
                except:
                    pass








Create_Empty_Folder()
sort_document()
sort_images()
sort_software()
