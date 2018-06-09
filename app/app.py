from flask_restful import Resource

class Request(Resource):
    """This class will define methods for the request"""
    def post(self):
        """This class creates a request"""
        pass

    def get(self, request_id):
        """This method gets the details of a request"""
        pass

    def put(self, request_id):
        """This method modifies the details of a request"""
        pass

    def delete(self, request_id):
        """This method deletes a request"""
        pass


