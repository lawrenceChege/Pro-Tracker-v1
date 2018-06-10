"""API endpoints for the maintenance tracker app"""
from flask import jsonify, request
from app.helpers import HelpAdmin
from app.validators import check_user
import psycopg2
from flask_restful import Resource, reqparse,fields
from app.validators import check_request
from flask_jwt_extended import jwt_required, get_jwt_identity


conn= psycopg2.connect("dbname='tracker' user='postgres' password='       ' host='localhost'")
cur = conn.cursor()
resource_fields = {
    'status': fields.String,
}
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
    """get ll users"""
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), HelpAdmin().get_all_users()


class Admin_get_user(Resource):
    """ gets a user"""
    @jwt_required
    def get(self, user_id):
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), HelpAdmin().get_user(user_id)
    def delete(self,user_id):
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), HelpAdmin().delete_user(user_id)

class Admin_approve_request(Resource):
    """change the status of the request to approved"""
    @jwt_required
    def put(self, request_id, **kwargs):
        check_request(resource_fields)
        current_user = get_jwt_identity()
        status =resource_fields['status']
        req = {
            'status': status
        }
        return jsonify(logged_in_as=current_user),HelpAdmin().change_status(request_id, req)


