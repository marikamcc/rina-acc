import sys
import psycopg2
import ast
import gtb #GTB is a Generic TextBox I wrote
import tkinter as tk

import db_vars

def add(tuple, connectionstring):
    try:
        conn = psycopg2.connect(connectionstring, connect_timeout=3)
        # print(connectionstring)
        # print("Database connected successfully")
    except:
        # print(connectionstring)
        print("Database not connected successfully")
        sys.exit(1)

    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (url, date, title) VALUES (%s, %s, %s);", (tuple[1], tuple[2], tuple[3]))

    # Commit the add of post to db
    conn.commit()

    cursor.close()
    conn.close()

def main():
    root = tk.Tk()
    app = gtb.TextBox(root)
    root.mainloop()
    #a = ast.literal_eval(input('enter tuple: '))
    a = ast.literal_eval(app.returntext)
    add(a, db_vars.string3)


if __name__ == '__main__':
    main()