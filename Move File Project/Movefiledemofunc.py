#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.5.1
#
# Author:       Tammy Goodnight
#
# Purpose:      Python Challenge. Move Files and automate process
#              
#
# Tested OS:  This code was written and tested to work with Windows 10.import shutil
import shutil
import os
import time
import datetime
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from pathlib import Path
import Movefiledemomain
import Movefiledemogui

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
SECONDS_IN_DAY = 24 * 60 * 60

#set where the source of the files are


#set the destination path to folderB



now = time.time()
before = now - SECONDS_IN_DAY
source ='C:/Python_projects//'
destination = 'C:/Python_projects//'
files=os.listdir('C:/Python_projects//')


def load_gui():
    center_window()

def get_source(self):  #no need to pass arguments to functions in both cases
    folder = fd.askdirectory(initialdir=os.path.normpath("C:/Python_projects/"), title="Select the Source Folder")
    src_files= os.path.getmtime(folder)
    return(folder)
    
    
def get_destination(self):  #no need to pass arguments to functions in both cases
    folder2 = fd.askdirectory(initialdir=os.path.normpath("C:/Python_projects/"), title="Select the Destination Folder")
    return(folder2)
    

def last_mod_time(self):
    for folder in files:
    #we are saying move the files represented by 'i' to their new destination
        src_files= os.path.getmtime(folder)
    for folder2 in files:
        dst_files= os.path.getmtime(folder2)
        compare_var= src_files > dst_files
        print(compare_var)
        '''if src_files > dst_files:
                shutil.move(src_files, dst_files)
                print("Move Successful")
        else:
            if src_files not in dst_files:
                shutil.move()'''
                             
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)
        

    
if __name__=="__main__":
    pass
