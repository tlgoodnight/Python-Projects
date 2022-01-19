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

src_files = str(0)
dst_files = str(0)
src_list =  str(0)
dst_list =  str(0)

def get_source(self):
    global src_files
    global src_list
    src_path = fd.askdirectory()
    self.src_folder.insert(0,src_path)
    src_list=os.listdir(src_path)
    for i in src_list:
        src_fname=os.path.join(str(src_list),i)
        print (i)
# I am having a hard time getting the mtime from this output.
    


def get_destination(self):
    global dst_files
    global dst_list
    dst_path = fd.askdirectory()
    self.dst_folder.insert(0,dst_path)
    dst_list=os.listdir(dst_path)
    for i in dst_files:
        dst_fname=os.path.join(str(dst_files),i)
        print (i)
# I am having a hard time getting the mtime from this output.
         
# I know the third compare functionhas to go here. But i need help
#def compare_files_move(fname):
    



                    
# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close                             
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)
        

    
if __name__=="__main__":
    pass
