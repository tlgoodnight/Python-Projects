import sqlite3


conn = sqlite3.connect('pythondatabasechallenge1.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE if NOT EXISTS tbl_fname1(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname1 TEXT)")
    conn.commit()


with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_fname1(col_fname1) VALUES (?)", \
                ('information.docx',))
    cur.execute("INSERT INTO tbl_fname1(col_fname1) VALUES (?)", \
                ('Hello.txt',))
    cur.execute("INSERT INTO tbl_fname1(col_fname1) VALUES (?)", \
                ('myImage.png',))
    cur.execute("INSERT INTO tbl_fname1(col_fname1) VALUES (?)", \
                ('myMovie.mpg',))
    cur.execute("INSERT INTO tbl_fname1(col_fname1) VALUES (?)", \
                ('World.txt',))
    cur.execute("INSERT INTO tbl_fname1(col_fname1) VALUES (?)", \
                ('data.pdf',))
    cur.execute("INSERT INTO tbl_fname1(col_fname1) VALUES (?)", \
                ('myPhoto.jpg',))
    conn.commit()

with conn:
    cur = conn.cursor()
    cur.execute("Select * FROM tbl_fname1 WHERE col_fname1 like '%.txt'")
    varFile = cur.fetchall()
    for x in varFile:
        x = "File Name: {}".format(x[1])
        print(x)

close.conn




        
