# Adding a post to my database with my GUI  

import tkinter as tk
from tkinter import * 
from datetime import datetime
#import os
import uuid
import markdown
import psycopg2
import sys

import db_vars


class PostingGUI:

    # define gui features
    def __init__(self, master):

        primary = '#fff'
        accent = "#065"
        wd = '20'   

        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.geometry('270x295+900+40')
        self.master.title('write blog post')

        Label(self.master, text='date: ', fg=accent).place(x=15, y=5)
        Label(self.master, text='url: ', fg=accent).place(x=15, y=36)
        Label(self.master, text='TITLE: ', fg=accent).place(x=15, y=67)
        #Label(self.master, text='tags: ', fg=accent).place(x=15, y=98)
        #Label(self.master, text='BODY:\n(MD) ', fg=accent).place(x=15, y=130)

        Label(self.master, text='tags: ', fg=accent).place(x=15, y=220)
        Label(self.master, text='BODY:\n(MD) ', fg=accent).place(x=15, y=98)

        self.dateInput=Entry(self.master, fg=accent, bg=primary, width=wd, insertbackground=accent)
        self.dateInput.place(x=60, y=3)
        self.dateInput.insert(0, datetime.now())

        self.fileInput=Entry(self.master, fg=accent, bg=primary, width=wd, insertbackground=accent)
        self.fileInput.place(x=60, y=34)

        self.titleInput=Entry(self.master, fg=accent, bg=primary, width=wd, insertbackground=accent)
        self.titleInput.place(x=60, y=65)

        self.tagsInput = Entry(self.master, fg=accent, bg=primary, width=wd, insertbackground=accent)
        self.tagsInput.place(x=60, y=220)#y=96)

        self.bodyInput = Text(self.master, fg=accent, bg=primary, width=26, height=9, highlightcolor='#47aae0', insertbackground=accent)
        self.bodyInput.place(x=60, y=96) #y=127)

        self.submitButton = Button(self.master, text='write post', bg=accent, fg=accent,  command=self.btnClickFunction, activebackground=primary, activeforeground=accent, width='10').place(x=70, y=255)


    # Included in button click, but required to enforce the same URL for db and local backup db
    def getURL(self, connectionstring):
        url = self.fileInput.get().strip().replace(" ","-")

        if url:
            # Does the url already exist in the table?
            conn = psycopg2.connect(connectionstring, connect_timeout=3)
            c = conn.cursor()
            c.execute("SELECT EXISTS ( SELECT * FROM posts WHERE url = (%s) )", (url,))
            check = c.fetchall()
            c.close()
            conn.close()

            if check[0][0]:
                # print("file exists")
                url += '-' + str(uuid.uuid4())
        else:
            # Should probably do another check here, but really what are the chances (?)
            url = str(uuid.uuid4())
        
        return url

    # This is the bulk of the button click function
    def doTheStuff(self, connectionstring, url):

        # print('1.) Connect to db')
        try:
            conn = psycopg2.connect(connectionstring, connect_timeout=3)
            print("Database connected successfully")
        except:
            print("Database not connected successfully")
            sys.exit(1)  
        
        
        ## Collect the stuff
        title = self.titleInput.get()
        tags = self.tagsInput.get().lower()
        # I like the enforcement of lowercase better here
        body = markdown.markdown(self.bodyInput.get("1.0",'end-1c'))
        
        date = str(self.dateInput.get()).strip()

        # Open cursor for db ops
        cursor = conn.cursor()

        # print('2.) Add post to posts table')
        cursor.execute("INSERT INTO posts (title, tags, body, url, date) VALUES (%s, %s, %s, %s, %s) RETURNING id;", (title, tags, body, url, date))
        id_of_new_row = cursor.fetchone()[0]

        # Commit the add of post to db
        conn.commit()

        if tags:
        # print('3.) Check the tags and add if missing to tag table')
            tagArray = [tag.strip() for tag in tags.split(',') ]
            # print(tagArray)

            for x in tagArray:
                # try to add the tags to the tag table.  should throw an error if already exists (unique constraint) and if so, undo the execute in exception.
                try:
                    with conn.cursor() as tagcur:
                        tagcur.execute("INSERT INTO tags (name) VALUES (%s)", (x,))
                        conn.commit()
                except:
                    # print(x, "already in tag table")
                    conn.rollback()

        # print('4.) Link post and tag in posttotag table')
        ### NOTE TO SELF: This can be done more elegantly and included in above loop "for x in tagArray" with "RETURNING id" in the insert statement... but also tagArray is like 1 maybe 2 tags sooo
            for t in tagArray:
                cursor.execute("SELECT id FROM tags WHERE name = (%s)", (t,))
                pp = cursor.fetchall()
                cursor.execute("INSERT INTO posttotags (postid, tagid) VALUES (%s, %s)", (id_of_new_row, pp[0][0]))
                conn.commit()         
        
        cursor.close()
        conn.close()

    def btnClickFunction(self):
        # Do this twice: First for the DB that the site reads from, and second for the local copy of the DB.

        # Check prod db for URL
        url = self.getURL(db_vars.string2)

        self.doTheStuff(db_vars.string2, url)
        self.doTheStuff(db_vars.string3, url)

        # And close window
        self.master.destroy()


def main():
    root = tk.Tk()
    app = PostingGUI(root)
    root.mainloop()
    

if __name__ == '__main__':
    main()
    exit()

    