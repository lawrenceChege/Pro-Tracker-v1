"""Connect to database."""
import psycopg2


def connectTODB():
    conn_string = "dbname='protrackerdb' user='postgres' password='       ' host='localhost'"
    try:
        print("connecting to database ...")
        return psycopg2.connect(conn_string)
    except:
        print("Connection to database failed!")


def create_tables():
    """"Create tables in the protrackerdb database."""
    commands= (
        """
        (CREATE TABLE users (user_id SERIAL PRIMARY KEY,
        username CHAR(150) NOT NULL unique,
        email VARCHAR(100) NOT NULL unique,
        password VARCHAR(255) NOT NULL,
        role CHAR(50) DEFAULT user)
        """,
        """
        (CREATE TABLE requests(request_id SERIAL PRIMARY KEY,
        category CHAR(100) NOT NULL,
        title VARCHAR(100) NOT NULL,
        frequency CHAR(100) NOT NULL,
        description VARCHAR(255) NOT NULL,
        status CHAR(50) DEFAULT pending,
        user_id integer REFERENCES users (user_id) ON DELETE RESTRICT)
        """)

    conn=None
    try:
        # connect to PostgreSQL server
        conn=connectTODB()
        cur=conn.cursor()
        # create a table
        cur.execute(commands)
        # close communication with postgreSQL database server.
        cur.close()
        # commit changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
