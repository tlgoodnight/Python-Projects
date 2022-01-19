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
import glob

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

global src_mod_files
global dst_mod_files
global src_path
global dst_path

def get_source(self):
    global src_mod_files
    global src_path
    src_path = fd.askdirectory()
    self.src_folder.insert(0,src_path)
    src_list=os.listdir(src_path)
    for i in src_list:
        src_fname=os.path.join(str(src_list),i)
        mod_time_src = time.strftime('%y-%m-%d %H:%M:%S',time.localtime(last_mod_time(i)))
        src_mod_files = (i + "." + mod_time_src)
        print (src_mod_files)
       
        #this works now returning the mtime. and it prints the file not present in Idle.
      
    


def get_destination(self):
    global dst_mod_files
    global dst_path
    dst_path = fd.askdirectory()
    self.dst_folder.insert(0,dst_path)
    dst_list=os.listdir(dst_path)
    for i in dst_list:
        dst_fname=os.path.join(str(dst_list),i)
        mod_time_dst= time.strftime('%y-%m-%d %H:%M:%S',time.localtime(last_mod_time(i)))
        dst_mod_files = (i + "." + mod_time_dst)
        print (dst_mod_files)
    
    
         

def last_mod_time(i):
    try:
        return os.path.getmtime(i)
    except FileNotFoundError:
        print (i)
       
       
        


#I know the third compare function has to go here. But i need help
def move_file_func(self):
    global src_path
    global dst_path
    global src_mod_files
    global dst_mod_files
    if src_mod_files != dst_mod_files:
        shutil.move(src_path,dst_path)

        #i am able to move the files now that are not in the other file.
        #I need to figure out how to compare mtime at the end of the string in the global variable
        
    
    
                    
# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close                             
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)
        

    
if __name__=="__main__":
    pass
