from flask_restful import Resource, Api, fields
from app.helpers import HelperDb
from flask import jsonify, request
from app.validators import check_request
import json
from flask_jwt_extended import jwt_required, get_jwt_identity

resource_fields = {
    'category': fields.String,
    'frequency': fields.String,
    'title': fields.String,
    'description': fields.String,
    'status': fields.String,
}


class Request(Resource):

    @jwt_required
    def post(self, **kwargs):
        """
      Creates a new request.
      ---
      tags:
          - The Requests
      parameters:
        - in: formData
          name: category
          type: string
          required: true
        - in: formData
          name: frequency
          type: string
          required: true
        - in: formData
          name: title
          type: string
          required: true
        - in: formData
          name: description
          type: string
          required: true

      responses:
        201:
          description: New request created.
    """
        current_user = get_jwt_identity()
        check_request(resource_fields)
        category, title, frequency, description, = request.json['category'], request.json[
            'frequency'], request.json['title'], request.json.get('description', "")
        req = {
            'category': category,
            'frequency': frequency,
            'title': title,
            'description': description,
            'status': "pending",
            'username': current_user,
        }
        return HelperDb().create_request(title, req)


class Request_get(Resource):

    @jwt_required
    def get(self, request_id):
        """"
       Gets a  request.
       ---
       tags:
            - The Requests

       responses:
         200:
           description: request found.
        """
        # current_user = get_jwt_identity()
        return HelperDb().get_request(request_id)

    def put(self, request_id, **kwargs):
        """
       Modifies a request.
       ---
       tags:
         - The Requests
       parameters:
         - in: formData
           name: category
           type: string
           required: true
         - in: formData
           name: frequency
           type: string
           required: true
         - in: formData
           name: title
           type: string
           required: true
         - in: formData
           name: description
           type: string
           required: true

       responses:
         201:
           description: Request updated.
        """
        current_user = get_jwt_identity()
        check_request(resource_fields)
        category, title, frequency, description, = request.json['category'], request.json[
            'frequency'], request.json['title'], request.json.get('description', "")
        req = {
            'category': category,
            'frequency': frequency,
            'title': title,
            'description': description,
        }

        return jsonify(logged_in_as=current_user), HelperDb().update_request(request_id, req)

    def delete(self, request_id):
        """
       Creates a new request.
       ---
       tags:
            - The Requests
       responses:
         200:
           description: request deleted.
        """
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), HelperDb().delete_request(request_id)
