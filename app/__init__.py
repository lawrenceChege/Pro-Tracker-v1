from flask import Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from app.app import Request, Request_get
from app.models import IndexPage
from app.views import (Admin, Admin_approve_request,
 Admin_disapprove_request, Admin_get_user, Admin_get_user, Admin_get_users,
Admin_resolve_request)
from app.users import (User_login, User,)

app = Flask(__name__, static_url_path = "/static")
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'raiseSONDecodeErrorExpectingromNone' 
jwt = JWTManager(app)

api.add_resource(Admin,'/api/v2/auth/admin/login')
api.add_resource(IndexPage,'/')
api.add_resource(User_login, '/api/v2/auth/login')
api.add_resource(User, '/api/v2/auth/signup')
api.add_resource(Admin_get_user, '/api/v2/users/<int:user_id>')
api.add_resource(Request,'/api/v2/requests/')
api.add_resource(Request_get,'/api/v2/request/<int:request_id>')
api.add_resource(Admin_get_users, '/api/v2/users/')
api.add_resource(Admin_approve_request, '/api/v2/requests/<int:request_id>')
api.add_resource(Admin_disapprove_request,'/api/v2/requests/<int:request_id>')
api.add_resource(Admin_resolve_request,'/api/v2/requests/<int:request_id>')
