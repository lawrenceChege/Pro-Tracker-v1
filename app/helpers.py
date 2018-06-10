import psycopg2
import json
import unicodedata
from flask import request, jsonify
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash
class HelperDb(object):
    """ Helper methods for connecting to db"""
    def __init__(self):
        """initialize db"""
        self.conn = psycopg2.connect("dbname='tracker' user='postgres' password='       ' host='localhost'")
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        self.cur2= self.conn.cursor()

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
                                                    VALUES (rtrim(%(username)s), %(email)s, %(password)s, %(role)s)
                                """,data)
                self.conn.commit()
                return "User created successfully!"
        except:
            return " Cannot do that"
    
    
    def login_user(self,password, username):
        """helper for confirming user using id"""
        content = request.get_json()
        username = (content['username'])
        password = (content['password'])
        self.cur.execute(""" SELECT username FROM users WHERE username = %s """, (username,))
        user = self.cur.fetchall()
        if user:
            self.cur2.execute(""" SELECT password FROM users WHERE username = %s """, (username,))
            pssword= self.cur2.fetchone()
            pasword = pssword[0]
            if check_password_hash(pasword,password):
                return "user successfully loged in"
            else:
                return "wrong password"
        else:
            return "user not registered" 

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
        
# if __name__ =='__main__':
# print(

