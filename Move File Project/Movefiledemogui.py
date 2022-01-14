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
import Movefiledemofunc

def load_gui(self):
    self.source_button = tk.Button(self.master,text='Select a Source Folder', command=lambda: Movefiledemofunc.get_source(self))
    self.source_button.grid(row=2, column=1)
    self.src_folder = ttk.Entry(self.master)
    self.src_folder.grid(row=2,column=2,rowspan=1,columnspan=2,padx=(10),pady=(10,0))
    self.dst_button = tk.Button(self.master,text='Select a Destination Folder',command=lambda: Movefiledemofunc.get_destination(self))
    self.dst_button.grid(row=4, column=1)
    self.dst_files = ttk.Entry(self.master)
    self.dst_files.grid(row=4,column=2,rowspan=1,columnspan=2,padx=(10),pady=(10,0))
    self.compare_button = tk.Button(self.master,text='Click here to initiate file transfer',command=lambda: Movefiledemofunc.last_mod_date(self))
    self.compare_button.grid(row=6, column=1)
    
   
if __name__=="__main__":
    pass
