import psycopg2
from psycopg2.extras import RealDictCursor
from passlib.hash import pbkdf2_sha256
class HelperDb(object):
    """ Helper methods for connecting to db"""
    def __init__(self):
        """initialize db"""
        self.conn = psycopg2.connect("dbname='tracker' user='postgres' password='       ' host='localhost'")
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        # self.cur2= self.conn.cursor()
    def get_item_users(self, username):
        self.cur.execute("SELECT * FROM users WHERE username = %s", (username))
        result = self.cur.fetchall()
        return dict(result)

    def add_user(self, data):
        """ helper for user registration"""
        self.cur.execute(""" INSERT INTO users (username, email, password, role) VALUES (%(username)s, %(email)s, %(password)s, %(role)s)""",data)
        self.conn.commit()
        return "User created successfully!"
    def register_user(self, username,data ):
        """helper for registering a user"""
        try:
            self.cur.execute("SELECT * FROM users")
            result = self.cur.fetchall() 
            if username in result:
                return "User already exists!"
            else:
                self.cur.execute(""" 
                                    INSERT INTO users (username, email, password, role) 
                                                    VALUES (%(username)s, %(email)s, %(password)s, %(role)s)
                                """,data)
                self.conn.commit()
                return "User created successfully!"
        except:
            return "dingehota"
    
    def login_user(self,password, username):
        """helper for confirming user using id"""
        try:
            self.cur.execute("SELECT username FROM users")
            result = self.cur.fetchall() 
            if username in result and pbkdf2_sha256.verify(password, hash):
                self.cur.execute("""SELECT user_id FROM users WHERE username = %s """, (username))
                user_id = self.cur.fetchall()
                return (user_id), "User successfully logged in"
            else:
                return "please check your credentials!"
        except:
            print ("I could not  select from user")

    def create_request(self, title, data):
        try:
            self.cur.execute("SELECT title FROM requests")
            result = self.cur.fetchall()
            if title not in result:
                self.cur.execute(
                    """ 
                        INSERT INTO requests (category, frequency, title, description, status )
                                                VALUES ( %(category)s, %(frequency)s, %(title)s, %(desctiption)s, %(status)s)
                    """,data)
                self.conn.commit()
                return  "Request created successfully!"
            else:
                return "Request with similar title exists"
        except:
            return "I could not select from requests"

    def update_request(self, request_id, data):
        try:
            self.cur.execute("SELECT request_id FROM requests")
            result = self.cur.fetchall()
            if request_id in result:
                self.cur.execute(
                    """ 
                        UPADTE requests SET (category, frequency, title, description, status )
                                                VALUES ( %(category)s, %(frequency)s, %(title)s, %(desctiption)s, %(status)s)
                    """,data)
                self.conn.commit()
                return  "Request created successfully!"
            else:
                return "Request does not exist"
        except:
            return "I could not select from requests"

    def delete_request(self, request_id):
        try:
            self.cur.execute(""" SELECT request_id FROM requests""")
            result = self.cur.fetchall()
            if request_id in result:
                self.cur.execute(""" DELETE FROM requests WHERE request_id = %s""", request_id)
                self.conn.commit()
            else:
                return "Request does not exitst!"
        except:
            return "I could not read from requests"

    def get_request(self, request_id):
        try:
            self.cur.execute(""" SELECT request_id FROM requests""")
            result = self.cur.fetchall()
            if request_id in result:
                self.cur.execute(""" SELECT * FROM requests WHERE request_id = %s""", request_id)
                return self.cur.fetchall()
            else:
                return "Request does not exitst!"
        except:
            return "I could not read from requests"

    def get_user(self,username):
        try:
            self.cur.execute(""" SELECT username FROM users""")
            result = self.cur.fetchall()
            if username in result:
                self.cur.execute(""" SELECT * FROM users WHERE username = %s""", username)
                return self.cur.fetchall()
            else:
                return "username does not exitst!"
        except:
            return "I could not read from users"

    def get_all_users(self):
        self.cur.execute(""" SELECT * FROM users""")
        return self.cur.fetchall()
    
    def change_status(self, status, request_id):
        try:
            self.cur.execute(""" SELECT request_id FROM users""")
            result = self.cur.fetchall()
            if request_id in result:
                self.cur.execute(""" UPADTE requests SET (status) VALUES (%(status)s)""")
                self.conn.commit()
                return "Request status updated !"
            else:
                return "username does not exitst!"
        except:
            return "I could not read from users"
        


