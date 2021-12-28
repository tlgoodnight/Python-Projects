#import sqlite3 module required to execute file
import sqlite3

#create and connect to database for challenge
conn = sqlite3.connect('pythondatabasechallenge4.db')

#create table with primary and col_fname for file name required by challenge
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE if NOT EXISTS tbl_fname4(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname4 TEXT)")
    conn.commit()

#tuple of file names required by challenge
fileList = ('information.docx','Hello.txt','myImage.png'\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#loop through each object in the tuple to find the files that end in .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            #the value for each row will be one name out of the tuple therefore (x,)
            #will denote one element tuple for each name ending with .txt.
            cur.execute("INSERT INTO tbl_fname4 (col_fname4) Values (?)", (x,))
            
conn.commit()

#query to return all names from col_fname 
with conn:
    cur = conn.cursor()
    cur.execute("Select col_fname4 FROM tbl_fname4")
    varFile = cur.fetchall()
    for x in varFile:
        x = "File Name: {}".format(x[0])
        print(x)
        
conn.close




        
