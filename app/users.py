from flask import Flask,jsonify

from flask_restful import Resource, Api, reqparse
from passlib.hash import pbkdf2_sha256
from app.helpers import HelperDb
from flask_jwt_extended import  create_access_token

import config
import psycopg2
import json

conn= psycopg2.connect("dbname='tracker' user='postgres' password='       ' host='localhost'")

cur = conn.cursor()

def check_email(email):
    pass

class User(Resource):
    """This class will define methods for the user"""
    
    def post(self):
        """This class creates a user"""
        self.reqparse = reqparse.RequestParser()
        
        self.reqparse.add_argument("username",
                                    required=True,
                                    help='Username is required!',
                                    location='json')
    
        self.reqparse.add_argument('email',
                                    type = str,
                                    required = True,
                                    help = "Email is required!",
                                    location = 'json')
        
        self.reqparse.add_argument('password',
                                    type = str,
                                    required = True,
                                    help = "Passord is required!",
                                    location = 'json')
        args =  self.reqparse.parse_args()
        username, email, password = args["username"], args["email"], args["password"]
        if username is None:
            return "Username cannot be empty!"

        hash_password = pbkdf2_sha256.hash(password)
        data = {
            "username" : username,
            "email": email,
            "password": hash_password,
            "role": "user"
        }
        user = HelperDb().register_user(username, data)
        return user
class User_login(Resource):
    """This user logs in the user"""
    def post(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required = True,
        help ="Username is required!")
        self.reqparse.add_argument('password', type = str, required = True,
        help = "Passord is required!", location = 'json')
        args =  self.reqparse.parse_args()
        username, password = args["username"], args["password"]
        # HelperDb().login_user(username, password)
        # access_token = create_access_token(identity=username)
        # token = {
        #     # "user_id": user_id,
        #     "token": access_token
        # }
        # return (token), 201
        try:
            cur.execute("SELECT username FROM users")
            result = cur.fetchall() 
            if username in result and pbkdf2_sha256.verify(password, hash):
                cur.execute("""SELECT user_id FROM users WHERE username = %s """, (username))
                user_id = cur.fetchall()
                print (user_id)
                return (user_id), "User successfully logged in"
            else:
                return "please check your credentials!"
        except:
            print ("I could not  select from user")
class Get_user(Resource):
    """Gets user details"""
    def get(self, user_id):
        try:
            cur.execute("""SELECT FROM users WHERE user_id = user_id""")
            result = cur.fetchall()
            if user_id in result:
                return jsonify(result)
            else:
                return "User not found!"
        except:
            print ("I could not  select from users")
class admin_get_users(Resource):
    """gets all users"""
    def get(self):
        pass

class admin_get_user(Resource):
    """ gets a user"""
    def get(self, user_id):
        pass

class admin_approve_request(Resource):
    """change the status of the request to approved"""
    def put(self, request_id):
        pass

class admin_disapprove_request(Resource):
    """change the status of the request to rejected"""
    def put(self, request_id):
        pass
class admin_resolve_request(Resource):
    """change the status of the request to resolved"""
    def put(self, request_id):
        pass

