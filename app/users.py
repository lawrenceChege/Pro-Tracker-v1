from flask import Flask,jsonify

from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash, generate_password_hash
from app.helpers import HelperDb


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
        
        hash_password = generate_password_hash(password)
        data = {
            "username" : username,
            "email": email,
            "password": hash_password,
            "role": "admin"
        }
        print(data)
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
        usernm, pssword = args["username"], args["password"]
        return HelperDb().login_user(usernm, pssword),201
        
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
