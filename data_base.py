"""This file will handle all relations with the data base"""

import sqlite3
from sqlite3 import Error

from selenium.webdriver.chrome import service


def create_connection(db_file):
    """
    create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def add_download(conn, film):
    """
    add a new film to the download table
    :param conn:
    :param film:
    :return: film id
    """

    sql = """ INSERT INTO downloads(title,year)
              VALUES(?,?);"""
    cur = conn.cursor()
    cur.execute(sql, film)
    conn.commit()
    return cur.lastrowid


def delete_download(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """

    sql = "DELETE FROM downloads WHERE id=?"
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def search_film(conn, title):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM downloads WHERE title =? GROUP BY title", (title,))

    rows = cur.fetchall()

    return rows


def is_movie_downloaded(conn, title):
    rows = search_film(conn, title)
    if rows != []:
        return True
    else:
        return False


def main():
    """
    This function initialise the database we need for the project
    return the connection
    """

    sql_create_downloads_table = """ CREATE TABLE IF NOT EXISTS downloads (
                                            id integer PRIMARY KEY,
                                            title text NOT NULL,
                                            year integer NOT NULL
                                        ); """

    conn = create_connection("data_base.db")
    create_table(conn, sql_create_downloads_table)
    return conn


if __name__ == "__main__":
    conn = main()
    print(is_movie_downloaded(conn, "finch"))
