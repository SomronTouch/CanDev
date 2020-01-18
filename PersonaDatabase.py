
import sqlite3 as sql
from sqlite3 import Error
import os

#Create or connect to database
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



def main():
    db_path = os.getcwd() + "/persona_database.db"
    
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
    # | id | trait1 | trait2 | trait3 | etc... |
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
    else:
        print("Error connecting to database.")


if __name__ == '__main__':
    main()