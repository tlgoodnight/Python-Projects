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
# Tested OS:  This code was written and tested to work with Windows 10.
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

import Movefiledemogui
import Movefiledemofunc

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        # This CenterWindow method will center our app on the user's screen
        Movefiledemofunc.center_window(self,300,300)
        self.master.title("Move File Window")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW",lambda: Movefiledemofunc.ask_quit(self)) 
        arg = self.master
        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        Movefiledemogui.load_gui(self)


        

if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
