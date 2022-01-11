import shutil
import os
import time
import datetime
import glob

SECONDS_IN_DAY = 24 * 60 * 60

#set where the source of the files are
source ='C:/Users/owner/Desktop/FolderA/'

#set the destination path to folderB
destination = 'C:/Users/owner/Desktop/FolderB/'
files=os.listdir(source)

now = time.time()
before = now - SECONDS_IN_DAY

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in files:
    #we are saying move the files represented by 'i' to their new destination
    src_fname = os.path.join('C:/Users/owner/Desktop/FolderA/', fname)
    if last_mod_time(src_fname) > before:
        dst_fname = os.path.join('C:/Users/owner/Desktop/FolderB/', fname)
        shutil.move(src_fname, dst_fname)
        

if __name__=="__main__":
    pass
