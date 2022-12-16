# Peanut butter that comes in a pouch is *mobile*.  Har har har.

import os
import uuid 
from datetime import datetime

def uniquefilecheck(title, location):
    check_file = os.path.exists(location + title)
    if not check_file:
        return True
    else:
        return False

def main(location, lgInputString):
    print(lgInputString)

    filenameU = str(uuid.uuid4())+".md"
    postDate = datetime.now()

    f = open(location + filenameU, "a")

    # Write .md frontmatter
    f.write("---\n")
    #front matter has to be there for my indexing, but they can be blank
    f.write("title: \n")
    f.write('tags: \n')
    f.write("date: '" + str(postDate) + "'\n")
    f.write("---\n\n")
    f.close()

    print(filenameU + " written to " + location)

    return filenameU 



if __name__ == '__main__':
    #requires absolute path
    location = '/Users/marika/Documents/babynet/rina/posts/'

    lgInputString = input()
    
    main(location, lgInputString)
