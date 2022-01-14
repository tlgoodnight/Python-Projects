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
    self.lbl_insert = tk.Label(self.master,text='Folders Selected: ')
    self.lbl_insert.grid(row=1,column=0,padx=(5,0),pady=(10,0),sticky=N+W)
    self.source_label = tk.Button(self.master,text='Select a Source Folder', command=Movefiledemofunc.get_source(self))
    self.source_label.grid(row=2, column=0)
    '''self.source_insert = tk.Label(self.master,text='Select a Folder')
    self.source_insert.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(10),pady=(10,0),sticky=N+E+W)'''
    self.dst_label = tk.Button(self.master,text='Select a Folder',command=Movefiledemofunc.get_destination(self))
    self.dst_label.grid(row=4, column=0)
    self.mve_btn = tk.Button(self.master,text='Click here to initiate file transfer', command=Movefiledemofunc.last_mod_time(self))
    self.mve_btn.grid(row=5, column=0)
    self.compare_txt=tk.Label(self.master, text=Movefiledemofunc.last_mod_time(self))
    '''self.dst_insert = tk.Label(self.master,text=Movefiledemofunc.get_destination)
    self.dst_insert.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(10),pady=(10,0),sticky=N+E+W)
    self.trsfr_succes = tk.Label(self.master,text=Movefiledemofunc.move_folder)
    self.trsfr_succes.grid(row=6,column=0,padx=(5,0),pady=(10,0),sticky=N+W)'''
    """
    self.btn1 = tk.Button(self.master, text="Click here to initiate file check", command=Movefiledemofunc.get)
    self.btn1.grid(row=3,column=0,padx=(5,0),pady=(10,0),sticky=N+W)
    self.btn2 = tk.Button(self.master, text="Get Method", command=PythonHTMLChallengeFunc.get_entry)
    self.btn2.grid(row=4,column=0,padx=(5,0),pady=(10,0),sticky=N+W)"""
        

if __name__=="__main__":
    pass
