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
from datetime import datetime
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


global mod_time_src
global mod_time_dst
global src_list
global dst_list




             

def get_source(self):
    global src_list
    src_path = fd.askdirectory()
    self.src_folder.insert(0,src_path)
    src_list=os.listdir(src_path)
    for i in src_list:
        src_fname = str(i)
        # Code to here prints the file names in order (they are string value) This WORKS
        def last_mod_time(i):
            try:
                return os.path.getmtime(i)    
            except FileNotFoundError:
                print 
        mod_time_src = time.ctime(last_mod_time(i))# returns files with string time
        print(src_fname,mod_time_src)#just print to idle to ensure it is capturing correct data'''
        #This finally works

        


def get_destination(self):
    global mod_time_dst
    global dst_list
    dst_path = fd.askdirectory()
    self.dst_folder.insert(0,dst_path) # path
    dst_list=os.listdir(dst_path) #returns list of filenames
    for i in dst_list:
        dst_fname = str(i) # returns string value of file name
        def last_mod_time(i):
            try:
                return os.path.getmtime(i)    
            except FileNotFoundError:
                print 
        mod_time_dst= time.ctime(last_mod_time(i))# returns string of mtime of file
        print (dst_fname,mod_time_dst) #just print to idle to ensure it is capturing correct data.'''
        


#I know the third compare function has to go here. But i need help
def move_file_func(self):
    day = 24*60*60
    current_time = time.time()
    time_v = current_time - day
    source = self.src_folder.get()
    destination = self.dst_folder.get()
    for file in os.listdir(source):
        src_files = os.path.join(source,file)
        src_mod_time = os.path.getmtime(src_files)
        if src_mod_time > time_v:
            dst_files = os.path.join(destination,file)
            shutil.move(src_files,dst_files)
            print(f"{file}has been moved")
        
                
    
        

            
    
                    
# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close                             
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)
        

    
if __name__=="__main__":
    pass
