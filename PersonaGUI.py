import tkinter as tk
import sqlite3 as sql
import os
from tkinter import filedialog
from tkinter import ttk
from sqlite3 import Error

#Open dialog window to load the database
def on_db_load_click():
    file_select = filedialog.askopenfilename(initialdir=os.getcwd, title="Select database", filetypes = (("Data Base Files", "*.db"),("All files","*.*")))
    db_path_text.config(state="normal")
    db_path_text.delete(1.0, tk.END)
    db_path_text.insert(tk.END, str(file_select))
    db_path_text.config(state="disabled")

#Verify that a database has been selected and clear the window
def on_db_selection():
    db_path_text.config(state="normal")
    db_path = db_path_text.get(1.0, tk.END)
    if len(db_path) > 1:
        for widget in wn.winfo_children():
            widget.destroy()
        database_window()
    else:
        db_path_text.config(state="disabled")


def database_window():
    conn = generate_or_connect_to_database()
    tasks_label = tk.Label(wn, text="Select a task")
    tasks_label.grid(row=0, column=0)
    if conn is not None:
        c = conn.cursor()
        q = "SELECT DISTINCT description FROM tasks"
        c.execute(q)
        all_tasks = c.fetchall()
        tasks_combo = ttk.Combobox(wn, values=all_tasks)
        tasks_combo.grid(row=1, column=0)
    else:
        err_label = tk.Label(wn, text="Error connecting to database. Please restart the application.")
        err_label.grid(row=1, column=0)



def create_connection(db):
    conn = None

    try:
        conn = sql.connect(db) 
    except Error as error:
        print("Connection error")
        print(error)

    return conn


#Creates tables with statement
def create_table(conn, table_name, statement):
    print(f"Making table {table_name}...")

    try:
        c = conn.cursor()
        c.execute(statement)
    except Error as error:
        print("Creating tables error")
        print(error)

def generate_or_connect_to_database():
    
    #TRAITS
    # +----+------+---------------+
    # | id | text | where_to_find |
    # +----+------+---------------+

    sql_create_traits_table = """CREATE TABLE IF NOT EXISTS traits (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                where_to_find text NOT NULL
                                );"""

    #PERSONA
    # +----+--------+--------+--------+--------+
    # | id | trait0 | trait1 | trait2 | etc... |
    # +----+--------+--------+--------+--------+

    sql_create_persona_table = """CREATE TABLE IF NOT EXISTS personas (
                                id integer PRIMARY KEY,
                                trait0 integer,
                                trait1 integer,
                                trait2 integer,
                                trait3 integer,
                                trait4 integer,
                                trait5 integer,
                                trait6 integer,
                                trait7 integer,
                                trait8 integer,
                                trait9 integer,
                                foreign key (trait0) references traits (id),
                                foreign key (trait1) references traits (id),
                                foreign key (trait2) references traits (id),
                                foreign key (trait3) references traits (id),
                                foreign key (trait4) references traits (id),
                                foreign key (trait5) references traits (id),
                                foreign key (trait6) references traits (id),
                                foreign key (trait7) references traits (id),
                                foreign key (trait8) references traits (id),
                                foreign key (trait9) references traits (id)
                                );"""

    #TASKS
    # +----+-------------+------------+
    # | id | description | persona_id |
    # +----+-------------+------------+

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                id integer PRIMARY KEY,
                                description text NOT NULL,
                                persona_id integer,
                                foreign key(persona_id) references persona(id)
                                );"""

    connection = create_connection(db_path)

    if connection is not None:
        create_table(connection, "traits", sql_create_traits_table)
        create_table(connection, "persona", sql_create_persona_table)
        create_table(connection, "tasks", sql_create_tasks_table)
        return connection
    else:
        print("Error connecting to database.")

db_path = ""

wn = tk.Tk()
wn.title("RCMP Persona Search")
wn.geometry('405x100')

db_path_text = tk.Text(wn, bg="white", height=1, width=50)
db_path_text.config(state="disabled")
db_path_text.grid(column=0, row=0, columnspan=4)

db_select_button = tk.Button(wn, text="Select database", command=on_db_load_click)
db_select_button.grid(column=0, row=2)

db_load = tk.Button(wn, text="Next", command=on_db_selection)
db_load.grid(column=1, row=2)

wn.mainloop()
