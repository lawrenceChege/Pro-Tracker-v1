from flask_restful import Resource, Api, fields
from app.helpers import HelperDb
from flask import jsonify, request
from app.validators import check_request 
import json
from flask_jwt_extended import jwt_required,get_jwt_identity

resource_fields = {
    'category': fields.String,
    'frequency': fields.String,
    'title': fields.String,
    'description': fields.String,
    'status': fields.String,
}

class Request(Resource):
    """This class will define methods for the request"""
    @jwt_required
    def post(self, **kwargs):
        """This class creates a request"""
        current_user = get_jwt_identity()
        check_request(resource_fields)
        category, title, frequency, description, = request.json['category'],request.json['frequency'],request.json['title'],request.json.get('description', "")
        req = {
            'category': category,
            'frequency': frequency,
            'title': title,
            'description': description,
            'status': "pending",
            'user_id': "1",
        }
        
        return jsonify(logged_in_as=current_user), HelperDb().create_request(title, req)
class Request_get(Resource):
    """defines methods requiring request_id"""
    @jwt_required
    def get(self, request_id):
        """This method gets the details of a request"""
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), HelperDb().get_request(request_id)

    def put(self, request_id, **kwargs):
        """This method modifies the details of a request"""
        current_user = get_jwt_identity()
        check_request(resource_fields)
        category, title, frequency, description, = request.json['category'],request.json['frequency'],request.json['title'],request.json.get('description', "")
        req = {
            'category': category,
            'frequency': frequency,
            'title': title,
            'description': description,
        }
        
        return jsonify(logged_in_as=current_user), HelperDb().update_request(request_id, req)

    def delete(self, request_id):
        """This method deletes a request"""
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), HelperDb().delete_request(request_id)


