from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

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

api.add_resource(User, '/api/v1/user-dashboard/<int:id>', endpoint = 'user')

requests = [
    {
        "id": "0",
        "category": "maintenance",
        "title": "fogort password",
        "frequency": "once",
        "description": "i am stupid",
        "status": "Pending"
    },
    {
        "id": "1",
        "category": "repair",
        "title": "fogort hammer",
        "frequency": "once",
        "description": "i am also stupid",
        "status": "Pending"
    },
    {
        "id": "2",
        "category": "maintenance",
        "title": "Tissue out",
        "frequency": "daily",
        "description": "well, not cool",
        "status": "Pending"
    }
]

request_fields = {
    'category': fields.String,
    'title':fields.String,
    'frequence':fields.String,
    'description':fields.String,
    'status':fields.String,
    'uri': fields.Url('request')
}

class RequestList(Resource):
    """Holds methods for giving all requests"""

    def __init__(self):
        """set validation for fields and initialize"""
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('category', type=str, required=True,
                                   help='No task category provided',
                                   location='json')
        self.reqparse.add_argument('frequency', type=str, required=True,
                                   help='No task frequency provided',
                                   location='json')
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('description', type=str, required=True,
                                   help='No task description provided',
                                   location='json')
        self.reqparse.add_argument('status', type=str,
                                   default= "Pending",
                                   location='json')
        super(RequestList, self).__init__()
    @classmethod
    def get(self):
        return {'requests':[ marshal(request, request_fields) for request in requests]}

    def post(self):
        args = self.reqparse.parse_args()
        request = {
            'id': requests[-1]['id'] +1,
            'category': args['category'],
            'frequency': args['frequency'],
            'title': args['title'],
            'description': args['description'],
            'status': args['status']
        }
        requests.append(request)
        return {'request': marshal(request, request_fields)}, 201 ,{'Etag': 'Request successfuly created'}

class Request(Resource):
    """ has methods for a single request"""
    def __init__(self):
        """set validation for fields and initialize"""
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('category', type=str, required=True,
                                   help='No task category provided',
                                   location='json')
        self.reqparse.add_argument('frequency', type=str, required=True,
                                   help='No task frequency provided',
                                   location='json')
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('description', type=str, required=True,
                                   help='No task description provided',
                                   location='json')
        self.reqparse.add_argument('status', type=str,
                                   default= "Pending",
                                   location='json')
        super(Request, self).__init__()
    @classmethod
    def get(self, id):
        request = [request for request in requests if request['id']==id]
        if len(request) == 0:
            abort(404)
        return {'request': marshal(request[0], request_fields)}

    def put(self, id):
        request = [request for request in requests if request['id']==id]
        if len(request) ==0:
            abort(404)
        request = request[0]
        args = self.reqparse.parse_args()
        for key, value in args.items():
            if value is not None:
                request[key] = value
        return {'task': marshal(request, request_fields)}
    @classmethod
    def delete(self, id):
        request = [request for request in requests if request['id'] == id]
        if len(request) == 0:
            abort(404)
        request.remove(request[0])
        return {'result': True}

api.add_resource(RequestList,'/', '/api/v1/users-dashboard/0/requests/', endpoint="requests")
api.add_resource(Request, '/<int:id>', '/api/v1/users-dashboard/0/requests/<int:id>')

if __name__ == '__main__':
    app.run()
