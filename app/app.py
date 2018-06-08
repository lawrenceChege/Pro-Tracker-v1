from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

<<<<<<< HEAD
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

api.add_resource(Request, '/api/v1/request/<int:id>', endpoint = 'request')
=======
class User(Resource):
    """This class will define methods for the user"""
    def post(self):
        """This class creates a user"""
        pass

    def get(self, id):
        """This method gets the details of a user"""
        pass

    def put(self, id):
        """This method modifies the details of a user"""
        pass

    def delete(self, id):
        """This method deletes a user"""
        pass

api.add_resource(User, 'api/v1/user-dashboard/<int:id>', endpoint = 'user')
>>>>>>> b0bc8c371eb3cc4c8d8a613ec5c5e49eca35a9d8
