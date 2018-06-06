from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Request(Resource):
    """This class will define methods for the request"""
    def post(self):
        """This class creates a request"""
        pass

    def get(self, id):
        """This method gets the details of a request"""
        pass

    def put(self, id):
        """This method modifies the details of a request"""
        pass

    def delete(self, id):
        """This method deletes a request"""
        pass

api.add_resource(Request, 'api/v1/request/<int:id>', endpoint = 'request')
