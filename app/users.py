from flask import Flask,jsonify
from flask_restful import Resource, Api, reqparse
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

# from config import conn

import psycopg2


app = Flask(__name__)
api = Api(app)
# cur = conn.cursor()
app.config['JWT_SECRET_KEY'] = 'raise JSONDecodeError("Expecting value", s, err.value) from None'  # Change this!
jwt = JWTManager(app)

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
        args =  self.reqparse.parse_args()
        self.reqparse.add_argument(args["username"],
                                    required=True,
                                    help='Username is required and should be a valid string!',
                                    location='json')
        
        self.reqparse.add_argument('email',
                                    type = str,
                                    required = True,
                                    help = "Email is required!",
                                    location = 'json')
        args =  self.reqparse.parse_args()
        self.reqparse.add_argument(args["email"],
                                    required=True,
                                    help='Email is required!',
                                    location='json')
        self.reqparse.add_argument('password',
                                    type = str,
                                    required = True,
                                    help = "Passord is required!",
                                    location = 'json')
        args =  self.reqparse.parse_args()
        self.reqparse.add_argument(args["password"],
                                    required=True,
                                    help='Password is required!',
                                    location='json')
        username, email, password = args["username"], args["email"], args["password"]
        data = {
            "username" : username,
            "email": email,
            "password": password

        }
        return data
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
        data ={
            "username":username,
            "password":password
        }
        return data


api.add_resource(User_login, '/api/v1/auth/login')
api.add_resource(User, '/api/v1/auth/signup')
