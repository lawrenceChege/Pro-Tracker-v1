"""Connect to database."""
import psycopg2


def connectTODB():
    conn_string = "dbname='tracker' user='postgres' password='       ' host='localhost'"
    try:
        print("connecting to database ...")
        return psycopg2.connect(conn_string)
    except:
        print("Connection to database failed!")


def create_tables():
    """"Create tables in the protrackerdb database."""
    commands=(
    """
        CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY,
                            username CHAR(20) NOT NULL unique,
                            email VARCHAR(50) NOT NULL unique,
                            password VARCHAR(255) NOT NULL,
                            role CHAR(10) DEFAULT user
                            )                            
    """,
    """
        CREATE TABLE IF NOT EXISTS requests(request_id SERIAL PRIMARY KEY,
                                category CHAR(10) NOT NULL,
                                title VARCHAR(40) NOT NULL,
                                frequency CHAR(30) NOT NULL,
                                description VARCHAR(220) NOT NULL,
                                status CHAR(10),
                                username CHAR(20)
        )
    """)

    conn=None
    try:
        # connect to PostgreSQL server
        conn=connectTODB()
        cur=conn.cursor()
        # create a table
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
        # close communication with postgreSQL database server.
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# if __name__ == '__main__':
#     create_tables()