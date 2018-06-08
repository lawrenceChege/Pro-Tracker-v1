from flask import Flask,jsonify
from flask_restful import Resource, Api, reqparse
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import config
import psycopg2
import json

conn= psycopg2.connect("dbname='tracker' user='postgres' password='       ' host='localhost'")
app = Flask(__name__)
api = Api(app)
cur = conn.cursor()
app.config['JWT_SECRET_KEY'] = 'raise JSONDecodeError("Expecting value", s, err.value) from None' 
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
        try:
            cur.execute("""SELECT * FROM users""")
            result = cur.fetchall()
            if username in result:
                return "User already exists!"
            else:
                cur.execute(""" INSERT INTO users (username, email, password, role) VALUES (%(username)s, %(email)s, %(password)s, %(role)s)""",data)
                conn.commit()
                return "User created successfully!"
        except:
            print ("I could not  select from user")
        return 201

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
        try:
            cur.execute("""SELECT * FROM users""")
            result = cur.fetchall()
            if username in result and pbkdf2_sha256.verify(password, hash):
                return "User successfully logged in"
            else:
                return "please check your credentials!"
        except:
            print ("I could not  select from user")
        
        access_token = create_access_token(identity=username)
        token = str(access_token)
        return (token), 201
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




api.add_resource(User_login, '/api/v1/auth/login')
api.add_resource(User, '/api/v1/auth/signup')
