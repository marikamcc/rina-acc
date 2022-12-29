import tkinter as tk
from tkinter import ttk
from tkinter import * 
from datetime import datetime
import os
import uuid


class PostingGUI:
    def __init__(self, master, location):

        self.location = location

        primary = '#fff'
        accent = "#000"
        wd = '20'   

        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.geometry('270x295+900+40')
        self.master.title('write plaintext blog post')

        Label(self.master, text='date: ', fg=accent).place(x=15, y=5)
        Label(self.master, text='file: ', fg=accent).place(x=15, y=36)
        Label(self.master, text='title: ', fg=accent).place(x=15, y=67)
        Label(self.master, text='tags: ', fg=accent).place(x=15, y=98)
        Label(self.master, text='body: ', fg=accent).place(x=15, y=130)

        self.dateInput=Entry(self.master, fg=accent, bg=primary, width=wd)
        self.dateInput.place(x=60, y=3)
        self.dateInput.insert(0, datetime.now())

        self.fileInput=Entry(self.master, fg=accent, bg=primary, width=wd)
        self.fileInput.place(x=60, y=34)

        self.titleInput=Entry(self.master, fg=accent, bg=primary, width=wd)
        self.titleInput.place(x=60, y=65)

        self.tagsInput = Entry(self.master, fg=accent, bg=primary, width=wd)
        self.tagsInput.place(x=60, y=96)

        self.bodyInput = Text(self.master, fg=accent, bg=primary, width=26, height=9, highlightcolor='#47aae0')
        self.bodyInput.place(x=60, y=127)

        self.submitButton = Button(self.master, text='write post', bg=accent, fg=accent,  command=self.btnClickFunction, activebackground=primary, activeforeground=accent, width='10').place(x=70, y=255)

    def uniquefilecheck(self, title, location):
        check_file = os.path.exists(location + title)
        if not check_file:
            return True
        else:
            return False

    def doTheStuff(self):
        result = [self.dateInput.get(), self.fileInput.get(), self.titleInput.get(), self.tagsInput.get(), self.bodyInput.get("1.0",'end-1c')]

        #DATE
        if result[0]:
            postDate = result[0].strip()
        else:
            postDate = datetime.now()

        #FILENAME
        if not result[1]:
            filename = str(uuid.uuid4())+".md"
        else:
            # remove leading and trailing spaces then make the name
            filenameCleaned = result[1].strip()
            filenameCheck = filenameCleaned.replace(" ","-")

            # check if file exists
            if not self.uniquefilecheck(filenameCheck+ ".md", self.location):
                # if the filename is not unique
                filename = filenameCheck + '-' + str(uuid.uuid4()) + ".md"
            else:
                filename = filenameCheck + ".md"
        
        #TITLE
        title = result[2].strip()
        #TAGS
        tags = result[3]
        #BODY
        body = result[4]
        contentSplit = body.split('\\n')

        f = open(self.location + filename, "a")
        f.write("---\n")
        f.write('title: "' + title + '"\n')
        f.write('tags: \n')
        if tags:
            tagArray = [tag.strip() for tag in tags.split(',') ]
            [f.write('   - ' + tag +'\n') for tag in tagArray]
        f.write("date: '" + str(postDate) + "'\n")
        f.write("---\n\n")
        [f.write(line + '\n\n') for line in contentSplit]
        f.close()
        # print(filename + " written to " + self.location)

        return filename

    def btnClickFunction(self):
        global file
        file = self.doTheStuff()
        self.master.destroy()


def main():
    location = '/Users/marika/Documents/babynet/rina/posts/'

    root = tk.Tk()
    app = PostingGUI(root, location)
    root.mainloop()
    

if __name__ == '__main__':
    main()
    if file:
        exit(file)

    