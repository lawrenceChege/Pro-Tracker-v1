from flask_restful import Resource, Api, marshal_with, fields
from helpers import HelperDb
resource_fields = {
    'category': fields.String,
    'frequency': fields.String,
    'title': fields.String,
    'description': fields.String,
    'status': fields.String,
}

class Request(Resource):
    """This class will define methods for the request"""
    @marshal_with(resource_fields, envelope='resource')
    def post(self, **kwargs):
        """This class creates a request"""
        return HelperDb().create_request()
    def get(self, request_id):
        """This method gets the details of a request"""
        return HelperDb().get_user()

    def put(self, request_id, **kwargs):
        """This method modifies the details of a request"""
        return HelperDb().update_request()

    def delete(self, request_id):
        """This method deletes a request"""
        return HelperDb().delete_request()


