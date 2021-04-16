#https://www.sqlitetutorial.net/sqlite-python/create-tables/
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
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
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "academi.db"

    sql_create_reviews_table = """ CREATE TABLE IF NOT EXISTS reviews (
                                        id integer PRIMARY KEY,
                                        listing_id integer NOT NULL,
                                        date date,
                                        reviewer_id integer,
                                        reviewer_name text,
                                        comments text
                                    ); """

    sql_create_file1000_table = """CREATE TABLE IF NOT EXISTS file1000 (
                                    id integer PRIMARY KEY,
                                    first_name text,
                                    last_name text,
                                    gender text,
                                    country text,
                                    age integer,
                                    date date
                                );"""
                                
    sql_create_disaster_table = """CREATE TABLE IF NOT EXISTS disaster (
                                    id integer PRIMARY KEY,
                                    keyword text,
                                    location text,
                                    text text,
                                    target integer
                                );"""
                                
    sql_create_albums_table = """CREATE TABLE IF NOT EXISTS albums (
                                    id integer PRIMARY KEY,
                                    title text,
                                    artist_id integer
                                );"""
                                
    sql_create_artists_table = """CREATE TABLE IF NOT EXISTS artists (
                                    id integer PRIMARY KEY,
                                    name text
                                );"""
                                
    sql_create_customers_table = """CREATE TABLE IF NOT EXISTS customers (
                                    id integer PRIMARY KEY,
                                    first_name text,
                                    last_name text,
                                    company text,
                                    address text,
                                    city text,
                                    state text,
                                    country text,
                                    postal_code text,
                                    phone text,
                                    fax text,
                                    email text,
                                    support_rep_id integer
                                );"""

    sql_create_employees_table = """CREATE TABLE IF NOT EXISTS employees (
                                    id integer PRIMARY KEY,
                                    last_name text,
                                    first_name text,
                                    title text,
                                    reports_to integer, 
                                    birth_date date,
                                    hire_date date
                                    address text,
                                    city text,
                                    state text,
                                    country text,
                                    postal_code text,
                                    phone text,
                                    fax text,
                                    email text
                                );"""
                                
    sql_create_genres_table = """CREATE TABLE IF NOT EXISTS genres (
                                    id integer PRIMARY KEY,
                                    name text
                                );"""
                                   
    sql_create_invoice_items_table = """CREATE TABLE IF NOT EXISTS invoice_items (
                                    id integer PRIMARY KEY,
                                    invoice_id integer,
                                    track_id integer,
                                    unit_price float,
                                    quantity integer
                                );"""
                                
    sql_create_invoices_table = """CREATE TABLE IF NOT EXISTS invoices (
                                    id integer PRIMARY KEY,
                                    customer_id integer,
                                    invoice_date datetime,
                                    billing_address text,
                                    billing_state text,
                                    billing_country text,
                                    billing_postal_code text,
                                    total float
                                );"""
                                
    sql_create_media_types_table = """CREATE TABLE IF NOT EXISTS media_types (
                                    id integer PRIMARY KEY,
                                    name text
                                );"""
                                
    sql_create_playlist_track_table = """CREATE TABLE IF NOT EXISTS playlist_track (
                                    id integer PRIMARY KEY,
                                    track_id integer
                                );"""
                                
    sql_create_playlists_table = """CREATE TABLE IF NOT EXISTS playlists (
                                    id integer PRIMARY KEY,
                                    track_id integer
                                );"""
                                
    sql_create_tracks_table = """CREATE TABLE IF NOT EXISTS tracks (
                                    id integer PRIMARY KEY,
                                    name text,
                                    album_id integer,
                                    media_type_id integer,
                                    genre_id integer,
                                    composer text,
                                    millisecond integer,
                                    bytes integer,
                                    unit_price float
                                );"""
                                
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create reviews table
        create_table(conn, sql_create_reviews_table)

        # create file1000 table
        create_table(conn, sql_create_file1000_table)
        
        # create disaster table
        create_table(conn, sql_create_disaster_table)
        
         # create albums table
        create_table(conn, sql_create_albums_table)
        
         # create artists table
        create_table(conn, sql_create_artists_table)
        
         # create customers table
        create_table(conn, sql_create_customers_table)
        
        # create employees table
        create_table(conn, sql_create_employees_table)
        
        # create genres table
        create_table(conn, sql_create_genres_table)
        
        # create invoice_items table
        create_table(conn, sql_create_invoice_items_table)
        
        # create invoices table
        create_table(conn, sql_create_invoices_table)
        
        # create media_types table
        create_table(conn, sql_create_media_types_table)
        
        # create playlist_track table
        create_table(conn, sql_create_playlist_track_table)
        
        # create playlists table
        create_table(conn, sql_create_playlists_table)
        
         # create tracks table
        create_table(conn, sql_create_tracks_table)
        
        print("DB succes")
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()