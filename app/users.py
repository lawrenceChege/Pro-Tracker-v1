from flask import Flask, jsonify
from app.validators import check_user, check_email
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash, generate_password_hash
from app.helpers import HelperDb


import config
import psycopg2
import json

conn = psycopg2.connect(
    "dbname='tracker' user='postgres' password='       ' host='localhost'")

cur = conn.cursor()


class User(Resource):
    """This class will define methods for the user"""

    def post(self):
        """
        Registers a new user.
        ---
        tags:
          - Users
        parameters:
          - in: formData
            name: email
            type: string
            required: true
          - in: formData
            name: username
            type: string
            required: true
          - in: formData
            name: password
            type: string
            required: true
        responses:
          201:
            description: New user registered.
        """
        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument("username",
                                   required=True,
                                   help='Username is required!',
                                   location='json')

        self.reqparse.add_argument('email',
                                   type=str,
                                   required=True,
                                   help="Email is required!",
                                   location='json')

        self.reqparse.add_argument('password',
                                   type=str,
                                   required=True,
                                   help="Passord is required!",
                                   location='json')
        args = self.reqparse.parse_args()
        username, email, password = args["username"], args["email"], args["password"]
        if username is None:
            return "Username cannot be empty!"

        hash_password = generate_password_hash(password)
        data = {
            "username": username,
            "email": email,
            "password": hash_password,
            "role": "user"
        }
        print(data)
        user = HelperDb().register_user(username, data)
        return user


class User_login(Resource):

    def post(self):
        """
            Signs in a new user.
            ---
            tags:
              - Users
            parameters:
              - in: formData
                name: username
                type: string
                required: true
              - in: formData
                name: password
                type: string
                required: true
            responses:
              201:
                description: User Successfullly logged in.
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True,
                                   help="Username is required!")
        self.reqparse.add_argument('password', type=str, required=True,
                                   help="Passord is required!", location='json')
        args = self.reqparse.parse_args()
        usernm, pssword = args["username"], args["password"]
        return HelperDb().login_user(usernm, pssword), 201


class Get_user_requests(Resource):

    def get(self, user_id):
        """
            Registers a new user.
            ---
            tags:
              - Users
            responses:
              200:
                description: Requests succcesfully retrieved.
        """
        try:
            cur.execute("""SELECT * FROM requests WHERE user_id = user_id""")
            result = cur.fetchall()
            if user_id in result:
                return jsonify(result)
            else:
                return "User not found!"
        except:
            return ("I could not  select from users")
