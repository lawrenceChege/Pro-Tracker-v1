from flask import Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from app.app import Request, Request_get
from app.models import IndexPage
from app.views import (Admin,Admin_approve_request,Admin_get_all, Admin_get_user)
from app.users import (User_login, User,)
from flasgger import Swagger

app = Flask(__name__, static_url_path = "/static")
api = Api(app)
swagger = Swagger(app)

app.config['JWT_SECRET_KEY'] = 'raiseSONDecodeErrorExpectingromNone' 
jwt = JWTManager(app)


api.add_resource(IndexPage,'/')
api.add_resource(User, '/api/v2/auth/signup')
api.add_resource(User_login, '/api/v2/auth/login')
api.add_resource(Request,'/api/v2/requests/')
# api.add_resource(Get_request,'/api/v2/requests/')
api.add_resource(Request_get,'/api/v2/request/<int:request_id>')
api.add_resource(Admin,'/api/v2/admin/auth/login')
api.add_resource(Admin_get_all, '/api/v2/admin/users/')
api.add_resource(Admin_get_user, '/api/v2/admin/users/<int:user_id>')
api.add_resource(Admin_approve_request, '/api/v2/admin/requests/<int:request_id>')
