"""API endpoints for the maintenance tracker app"""
from flask import jsonify, request
from app.helpers import HelpAdmin
from app.validators import check_user
import psycopg2
from flask_restful import Resource, reqparse


conn= psycopg2.connect("dbname='tracker' user='postgres' password='       ' host='localhost'")
cur = conn.cursor()

class Admin(Resource):
    """defines Admin methods"""
    def post(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required = True,
        help ="Username is required!")
        self.reqparse.add_argument('password', type = str, required = True,
        help = "Passord is required!", location = 'json')
        args =  self.reqparse.parse_args()
        check_user(args)
        usernm, pssword = args["username"], args["password"]
        return HelpAdmin().login_admin(usernm,pssword)
class Admin_get_all(Resource):
    def get(self):
        return HelpAdmin().get_all_users()


class Admin_get_user(Resource):
    """ gets a user"""
    def get(self, user_id):
        return HelpAdmin().get_user(user_id)
    def delete(self,user_id):
        return HelpAdmin().delete_user(user_id)

class Admin_approve_request(Resource):
    """change the status of the request to approved"""
    def put(self, status, request_id):
        HelpAdmin().change_status(status, request_id)

class Admin_disapprove_request(Resource):
    """change the status of the request to rejected"""
    def put(self,status, request_id):
        HelpAdmin().change_status(status, request_id)
class Admin_resolve_request(Resource):
    """change the status of the request to resolved"""
    def put(self, status,request_id):
        HelpAdmin().change_status(status, request_id)

