"""Connect to database."""
import psycopg2


def connectTODB():
    conn_string = "dbname='maintenancedb' user='postgres' password='       ' host='localhost'"
    # con_string ="postgresql+psycopg2://evahdilycttgas:2fbf6a56272ad23e15f761fb8b7db1592d96f4fedcfa06016fde54791c17ac1c@ec2-50-16-241-91.compute-1.amazonaws.com:5432/d4rk034rpmde2c?sslmode=require"
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
                            username CHAR(50) NOT NULL unique,
                            email VARCHAR(50) NOT NULL unique,
                            password VARCHAR(255) NOT NULL,
                            role CHAR(20) DEFAULT user
                            )                            
    """,
    """
        CREATE TABLE IF NOT EXISTS requests(request_id SERIAL PRIMARY KEY,
                                category CHAR(20) NOT NULL,
                                title VARCHAR(40) NOT NULL,
                                frequency CHAR(30) NOT NULL,
                                description VARCHAR(220) NOT NULL,
                                status CHAR(20),
                                username CHAR(50)REFERENCES users (username)
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

if __name__ == '__main__':
    create_tables()