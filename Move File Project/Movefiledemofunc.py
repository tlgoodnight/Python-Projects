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




def load_gui(self):
    center_window()

SECONDS_IN_DAY = 24 * 60 * 60
now = time.time()
before = now - SECONDS_IN_DAY



def get_source(self):
    src_folder = tk.StringVar()
    src_folder = fd.askdirectory(initialdir=os.path.normpath("C:/Python_projects/"))
    print (src_folder)
       
    
def get_destination(self):
    src_destination = tk.StringVar()
    src_destination = fd.askdirectory(initialdir=os.path.normpath("C:/Python_projects/"))
    print (src_destination) 
    

def last_mod_time(self):
    for folder in files:
    #we are saying move the files represented by 'i' to their new destination
        src_files= os.path.getmtime(folder)
    for folder2 in files:
        dst_files= os.path.getmtime(folder2)
        compare_var= src_files > dst_files
        print(compare_var)
        if src_files > dst_files:
                shutil.move(src_files, dst_files)
                print("Move Successful")
        else:
            if src_files not in dst_files:
                shutil.move()
                
# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close                             
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)
        

    
if __name__=="__main__":
    pass
