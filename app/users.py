from flask import Flask
from flask_restful import Resource, Api
from passlib.hash import pbkdf2_sha256

import psycopg2


app = Flask(__name__)
api = Api(app)

class User(Resource):
    """This class will define methods for the user"""
    def __init__(self, username, email, password):
        """This method initializes the user"""
        self.username = username
        self.email = email
        self.password = pbkdf2_sha256.hash("password")
        
    def post(self):
        """This class creates a user"""
        pass

    def get(self, id):
        """This method gets the details of a user"""
        pass

    def put(self, id):
        """This method modifies the details of a user"""
        pass

    def delete(self, id):
        """This method deletes a user"""
        pass
