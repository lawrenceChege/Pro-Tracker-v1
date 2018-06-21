from flask_restful import Resource, fields
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
  """ methods for requests"""
  # @jwt_required
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
      if 'category' in request.json and not request.json['category']:
        return {"message": "Please enter category as either repair or maintenance"}, 400
      if 'frequency' in request.json and not request.json['frequency']:
        return {"message": "Frequency must be a string."}, 400
      if 'title' in request.json and not request.json['title']:
        return {"message": "Title should be a string"}, 400
      if 'description' in request.json and not request.json['description']:
        return {"message": "Description is a string"}, 400
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
  
  def get(self):
    """get a users rquests"""
    return {"message":"all requests found successfully"}


class Request_get(Resource):
  """methods for getting requests"""
  # @jwt_required
  def get(self, request_id):
      """"
      Gets a  request.
      ---
      tags:
        - The Requests
      Parameters:
        - in: formData
          name: request_id
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
        - in: formData
          name: request_id
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
      if 'category' in request.json and not isinstance(request.json['category'], str):
          return jsonify({"message": "Please enter category as either repair or maintenance"})
      if 'frequency' in request.json and not isinstance(request.json['frequency'], str):
          return jsonify({"message": "Frequency must be a string. Reccomended;once, daily, weekly, monthly or annually"})
      if 'title' in request.json and not isinstance(request.json['title'], str):
          return jsonify({"message": "Title should be a string"})
      if 'description' in request.json and not isinstance(request.json['description'], str):
          return jsonify({"message": "Description is a string"})
      current_user = get_jwt_identity()
      check_request(resource_fields)
      category, title, frequency, description, = request.json['category'], request.json[
          'frequency'], request.json['title'], request.json.get('description', "")
      req = {
          'category': category,
          'frequency': frequency,
          'title': title,
          'description': description,
          'username':current_user,
      }

      return HelperDb().update_request(request_id, req)

  def delete(self, request_id):
      """
      Creates a new request.
      ---
      tags:
        - The Requests
      parameters:
        - in: formData
          name: request_id
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
      return HelperDb().delete_request(request_id)
