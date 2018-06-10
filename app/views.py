"""API endpoints for the maintenance tracker app"""
from flask import jsonify, request
from app.helpers import HelpAdmin
import psycopg2
from flask_restful import Resource


conn= psycopg2.connect("dbname='tracker' user='postgres' password='       ' host='localhost'")
cur = conn.cursor()

class Admin(Resource):
    """defines Admin methods"""
    def post(self):
        HelpAdmin().login_admin()

    def get(self):
        HelpAdmin().get_all_users()


class Admin_get_user(Resource):
    """ gets a user"""
    def get(self, user_id):
        HelpAdmin().get_user(user_id)
    def delete(self):
        HelpAdmin().delete_user()

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

