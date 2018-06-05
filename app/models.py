import psycopg2

#Try connecting to the database
try:
    con = psycopg2.connect("dbname='protrackerdb' user='lawrence' host='localhost' password='       '")
except:
    print ("I am unable to connect to the database")


cur = con.cursor()

cur.execute("CREATE TABLE User(id serial PRIMARY KEY, username varchar, email varchar, password varchar)")

namedict = ({"username": "Joshua", "email": "Drake@gmail.com", "password": "something"},
            {"username": "Steven", "email": "stephen@gmail.com",
                "password": "somethingnew"},
            {"username": "David", "email": "devi@gmail.com", "password": "somethingelse"})

cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur.executemany(
    """INSERT INTO User(username,email, password) VALUES (%(username)s, %(email)s, %(password)s)""", namedict)
con.commit()
try:
    cur.execute("""SELECT * from User""")
except:
    print ("I can't select from user")

con.set_isolation_level(0)
try:
    cur.execute("""DROP DATABASE protraxkerdb""")
except:
    print ("I can't drop our database!")

cur.close()
con.close()
