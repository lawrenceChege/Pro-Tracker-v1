import psycopg2

#Try connecting to the database
try:
    conn = psycopg2.connect(" dbname='protrackerdb' user='postgres' host='localhost' password='       '")
except:
    print ("I am unable to connect to the database")


cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, username varchar, email varchar, password varchar)")

namedict = {"username": "Joshua", "email": "Drake@gmail.com", "password": "something"}
            # {"username": "Steven", "email": "stephen@gmail.com",
            #     "password": "somethingnew"},
            # {"username": "David", "email": "devi@gmail.com", "password": "somethingelse"})


cur.execute(
    """INSERT INTO users (username,email, password) VALUES (%s, %s, %s)""", (namedict["username"], namedict["email"], namedict["password"]))


try:
    cur.execute("""SELECT * from users""")
    items = cur.fetchall()
    print (items)
except:
    print ("I can't select from user")

# conn.set_isolation_level(1)
# try:
#     cur.execute("""DROP DATABASE protrackerdb""")
# except:
#     print ("I can't drop our database!")
conn.commit()
cur.close()
conn.close()
