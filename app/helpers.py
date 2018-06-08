import psycopg2
from psycopg2.extras import RealDictCursor
from passlib.hash import pbkdf2_sha256

class HelperDb(object):
    """ Helper methods for connecting to db"""
    def __init__(self):
        """initialize db"""
        self.conn = psycopg2.connect("dbname='tracker' user='postgres' password='       ' host='localhost'")
        self.cur = self.conn.RealDictCursor()

    def get_item_users(self, item):
        self.cur.execute("""SELECT %(item)s FROM users """)
        result = self.cur.fetchall()
        return result

    def add_user(self, data):
        """ helper for user registration"""
        self.cur.execute(""" INSERT INTO users (username, email, password, role) VALUES (%(username)s, %(email)s, %(password)s, %(role)s)""",data)
        self.conn.commit()
        return "User created successfully!"
    def register_user(self, item, data):
        """helper for registering a user"""
        try:
            result= HelperDb().get_item_users(item) 
            if item in result:
                return "User already exists!"
            else:
                add = HelperDb().add_user(data)
                return add
        except (Exception, psycopg2.DatabaseError) as error:
            return error
    
    def login_user(self, item,data):
        """helper for confirming user using id"""
        result= HelperDb().get_item_users(item)
        if item in result :
            pass


