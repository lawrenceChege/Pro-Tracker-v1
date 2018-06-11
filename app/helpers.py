import psycopg2
import json
import unicodedata
from flask import request, jsonify
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash


class HelperDb(object):
    """ Helper methods for connecting to db"""

    def __init__(self):
        """initialize db"""
        self.conn = psycopg2.connect(
            "dbname='maintenancedb' user='postgres' password='       ' host='localhost'")
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        self.cur2 = self.conn.cursor()

    def register_user(self, username,email, data):
        """helper for registering a user"""
        try:
            self.cur.execute("SELECT TRIM(username) FROM users WHERE username=%s",(username,))
            user_username = self.cur.fetchall()
            self.cur.execute("SELECT TRIM(email) FROM users WHERE email=%s",(email,))
            email_user = self.cur.fetchall()
            if len(user_username)!=0 and len(email_user):
                return "User already exists!"
            else:
                self.cur.execute(""" 
                                    INSERT INTO users (username, email, password, role) 
                                                    VALUES ((%(username)s), %(email)s, %(password)s, %(role)s)
                                """, data)
                self.conn.commit()
                return "User created successfully!"
        except:
            return "culd not see"

    def login_user(self, password, username):
        """helper for confirming user using id"""
        content = request.get_json()
        username = (content['username'])
        password = (content['password'])
        self.cur.execute(
            """ SELECT TRIM(username) FROM users WHERE username = %s """, (username,))
        user = self.cur.fetchall()
        logged_in_user_dict = user[0]
        logged_in_user = (logged_in_user_dict['btrim'])
        if user:
            self.cur2.execute(
                """ SELECT password FROM users WHERE username = %s """, (username,))
            pssword = self.cur2.fetchone()
            pasword = pssword[0]
            if check_password_hash(pasword, password):
                access_token = create_access_token(identity=logged_in_user)
                token = access_token
                return (token)
            else:
                return "wrong password"
        else:
            return "user not registered"

    def create_request(self, title, req):
        content = request.get_json()
        Title = (content['title'])
        try:
            self.cur.execute(
                "SELECT * FROM requests WHERE title = %s", (Title,))
            request_i = self.cur.fetchall()
            if len(request_i)!=0:
                return "Request with similar title exists"
            else:
                self.cur.execute(""" 
                                    INSERT INTO requests (category, title, frequency, description, status ,username)
                                                            VALUES ( %(category)s, %(title)s, %(frequency)s,  %(description)s, %(status)s, %(username)s)
                                """, req)
                self.conn.commit()
                return "Request created successfully!"

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "I could not red from requests"

    def update_request(self, request_id, data):
        try:
            self.cur.execute(
                "SELECT * FROM requests WHERE request_id = %s", (request_id,))
            request_i = self.cur.fetchone()
            if request_i:
                self.cur.execute(
                    "UPDATE requests SET category=%(category)s, frequency=%(frequency)s, title=%(title)s, description=%(description)s", data)
                self.conn.commit()
                return "Request updated successfully!"
            else:
                return "Request does not exist"
        except:
            return "I could not select from requests"

    def delete_request(self,request_id):
        try:
            self.cur.execute(
                "SELECT * FROM requests WHERE request_id = %s", (request_id,))
            request_details = self.cur.fetchall()
            if len(request_details)!=0:
                self.cur.execute(
                    """ DELETE FROM requests WHERE request_id = %s""", (request_id,))
                self.conn.commit()
                return "Request deleted successfully!"
            else:
                return "Request does not exitst!"
        except:
            return "I could not see inside"

    def get_request(self, request_id):
        try:
            self.cur.execute(
                "SELECT * FROM requests WHERE request_id = %s", (request_id,))
            request_i = self.cur.fetchall()
            if len(request_i) > 0:
                return request_i
            else:
                return "Request does not exitst!"
        except:
            return "I could not read from requests"


class HelpAdmin(HelperDb):
    """helper methods for Admin"""

    def get_user(self, user_id):
        try:
            self.cur.execute(
                """ SELECT * FROM users where user_id=%s""", (user_id,))
            user = self.cur.fetchall()
            if user:
                return user
            else:
                return "user does not exitst!"
        except:
            return "I could not read from users"

    def get_all_users(self):
        self.cur.execute(""" SELECT * FROM users""")
        result = self.cur.fetchall()
        return result

    def change_status(self, request_id, data):
        try:
            self.cur.execute(
                """ SELECT TRIM(status) FROM requests WHERE request_id=%s""", (request_id,))
            result = self.cur.fetchall()
            if len(result) > 0:
                self.cur.execute("UPDATE requests SET status=%(status)s", data)
                self.conn.commit()
                return "Request status updated !"
            else:
                return "username does not exitst!"
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return "I could not read from users"

    def login_admin(self, username, password):
        """logs in admin"""
        content = request.get_json()
        username = (content['username'])
        password = (content['password'])
        user = "Admin"
        if username == user:
            self.cur2.execute(
                """ SELECT password FROM users WHERE username = %s """, (user,))
            pssword = self.cur2.fetchone()
            pasword = pssword[0]
            if check_password_hash(pasword, password):
                access_token = create_access_token(identity=user)
                token = access_token
                return "You know What to do !", token
            else:
                return "wrong password"
        else:
            return "You are not admin ...shu shu!"

    def delete_user(self, user_id):
        """delete a user"""
        try:
            self.cur.execute(
                "SELECT * FROM users WHERE user_id = %s", (user_id,))
            request_i = self.cur.fetchall()
            if len(request_i) > 0:
                self.cur.execute(
                    """ DELETE FROM users WHERE user_id = %s""", (user_id,))
                self.conn.commit()
                return "Request deleted successfully!"
            else:
                return "Request does not exitst!"
        except:
            return "I could not see inside"
