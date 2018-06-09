from flask import Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from app.app import Request
from app.users import (User_login, User, Admin_approve_request,
 Admin_disapprove_request, Admin_get_user, Admin_get_user, Admin_get_users,
Admin_resolve_request)

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'raise JSONDecodeError("Expecting value", s, err.value) from None' 
jwt = JWTManager(app)


api.add_resource(User_login, '/api/v1/auth/login')
api.add_resource(User, '/api/v1/auth/signup')
api.add_resource(Admin_get_user, '/api/v1/auth/<int:user_id>')
api.add_resource(Request, '/api/v1/request/<int:id>', endpoint = 'request')
api.add_resource(Admin_get_users)
api.add_resource(Admin_approve_request)
api.add_resource(Admin_disapprove_request,)
api.add_resource(Admin_resolve_request,)
