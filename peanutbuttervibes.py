# Get it, it's a GUI -> gooey -> song by Glass Animals -> "you just wanna know those ${filename}"


import tkinter as tk
from tkinter import ttk
from tkinter import * 
from datetime import datetime
import os
import uuid

location = '/Users/marika/Documents/babynet/rina/posts/'

def uniquefilecheck(title, location):
    check_file = os.path.exists(location + title)
    if not check_file:
        return True
    else:
        return False

def Close():
    root.destroy()

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = [dateInput.get(), fileInput.get(), titleInput.get(), tagsInput.get(), bodyInput.get("1.0",'end-1c')]
	return userInput


# this is the function called when the button is clicked
def btnClickFunction():
    #get info
    #do the program
    #push to github
    #exit

    result = getInputBoxValue()

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
        if not uniquefilecheck(filenameCheck+ ".md", location):
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

    f = open(location + filename, "a")
    f.write("---\n")
    f.write("title: " + title + "\n")
    f.write('tags: \n')
    if tags:
        tagArray = [tag.strip() for tag in tags.split(',') ]
        [f.write('   - ' + tag +'\n') for tag in tagArray]
    f.write("date: '" + str(postDate) + "'\n")
    f.write("---\n\n")
    [f.write(line + '\n\n') for line in contentSplit]
    f.close()
    # print(filename + " written to " + location)

    ##DO THE GITHUB STUFF HERE!!!!!!
    
    Close()




root = Tk()

primary = '#fff'
accent = "#000"
wd = '20'
ft = ('helvetica', 16, 'normal')

# # This is the section of code which creates the main window
root.geometry('270x295')
#root.configure(background=primary)#'#F0F8FF')
root.title('write plaintext blog post')

# This is the section of code which creates the a label
Label(root, text='date: ', fg=accent).place(x=15, y=5)
Label(root, text='file: ', fg=accent).place(x=15, y=36)
Label(root, text='title: ', fg=accent).place(x=15, y=67)
Label(root, text='tags: ', fg=accent).place(x=15, y=98)
Label(root, text='body: ', fg=accent).place(x=15, y=130)

# This is the section of code which creates a text input box
dateInput=Entry(root, fg=accent, bg=primary, width=wd)
dateInput.place(x=60, y=3)

fileInput=Entry(root, fg=accent, bg=primary, width=wd)
fileInput.place(x=60, y=34)

titleInput=Entry(root, fg=accent, bg=primary, width=wd)
titleInput.place(x=60, y=65)

tagsInput = Entry(root, fg=accent, bg=primary, width=wd)
tagsInput.place(x=60, y=96)

bodyInput = Text(root, fg=accent, bg=primary, width=26, height=9, highlightcolor='#47aae0')
bodyInput.place(x=60, y=127)


# # This is the section of code which creates a button
submitButton = Button(root, text='write post', bg=accent, fg=accent,  command=btnClickFunction, activebackground=primary, activeforeground=accent, width='10').place(x=70, y=255)


root.mainloop()

# if __name__ == '__main__':
#     main()