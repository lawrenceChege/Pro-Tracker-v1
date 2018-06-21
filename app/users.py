from flask import Flask, jsonify, request
from app.validators import check_user,check_blank,check_password, check_email
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
        name: username
        type: string
        required: true
      - in: formData
        name: email
        type: string
        required: true
      - in: formData
        name: password
        type: string
        required: true
    responses:
      200:
        description: The request was successful.
      201:
        description: New request created.
      400:
        description: Bad request made.
      401:
        description: Unauthorised access.
      404:
        description: Page not found.
    """
    self.reqparse = reqparse.RequestParser()

    self.reqparse.add_argument("username",location='json')

    self.reqparse.add_argument('email', location='json')

    self.reqparse.add_argument('password', location='json')
    args = self.reqparse.parse_args()
    if not request.json:
      return jsonify({"message" : "check your request type"})
    if 'username' not in request.json or not request.json['username']:
      return {"message" : "Username is required"}, 400
    if 'email' not in request.json or not request.json['email']:
      return {"message" : "Email is required!"}, 400
    if 'password' not in request.json or not request.json['password']:
      return {"message" : "Passord is required!"}, 400
    username, email, password = args["username"], args["email"], args["password"]
    hash_password = generate_password_hash(password)
    data = {
        "username": username,
        "email": email,
        "password": hash_password,
        "role": "user"
    }
    print(data)
    user = HelperDb().register_user(username,email, data)
    return user


class User_login(Resource):
  """"""
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
      200:
        description: The request was successful.
      201:
        description: New request created.
      400:
        description: Bad request made.
      401:
        description: Unauthorised access.
      404:
        description: Page not found.
    """
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('username', location='json')
    self.reqparse.add_argument('password',location='json')
    if not request.json:
      return jsonify({"message" : "check your request type"})
    if 'username' in request.json and not request.json['username']:
      return {"message" : "Username is required"},400
    if 'password' in request.json and not request.json['password']:
      return {"message" : "Password is required"},400
    
    args = self.reqparse.parse_args()
    usernm, pssword = args["username"], args["password"]
    return HelperDb().login_user(usernm, pssword), 201


class Get_user_requests(Resource):
  """"""
  def get(self, user_id):
    """
    Registers a new user.
    ---
    tags:
      - Users
    Parameters:
      - in: formData
        name: user_id
        type: integer
        required: true
    responses:
      200:
        description: The request was successful.
      201:
        description: New request created.
      400:
        description: Bad request made.
      401:
        description: Unauthorised access.
      404:
        description: Page not found.
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
