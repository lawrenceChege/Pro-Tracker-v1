from flask import Flask
from flask_restful import Resource, Api, reqparse
from passlib.hash import pbkdf2_sha256
from config import conn

import psycopg2


app = Flask(__name__)
api = Api(app)
cur = conn.cursor()
def check_email(email):
    pass

class User(Resource):
    """This class will define methods for the user"""
    def __init__(self, username, email, password):
        """This method initializes the user"""
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type = str, required = True,
        help = 'Username is required!', location = 'json')
        self.reqparse.add_argument('email', type = str,required = True,
        help = "Email is required!", location = 'json')
        check_email(email)
        self.reqparse.add_argument('password', type = str, required = True,
        help = "Passord is required!", location = 'json')
        self.username = username
        self.email = email
        self.password = pbkdf2_sha256.hash("password")
        
    def post_signup(self, username, email, password):
        """This class creates a user"""
        cur.execute("SELECT username FROM users")
        data = cur.fetchall()
        if username in data:
            return "User already exists"
        else:
            cur.execute("INSERT (self.username, self.email, self.password) VALUES(%s, %s, %s)")
        return "User created successful!"

    def post_login(self, id):
        """This method logs in a user"""
        pass

    def put(self, id):
        """This method modifies the details of a user"""
        pass

    def delete(self, id):
        """This method deletes a user"""
        pass
api.add_resource(User, 'api/v1/auth/')