from flask import Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from app.users import User_login, User, Get_user

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'raise JSONDecodeError("Expecting value", s, err.value) from None' 
jwt = JWTManager(app)


api.add_resource(User_login, '/api/v1/auth/login')
api.add_resource(User, '/api/v1/auth/signup')
api.add_resource(Get_user, '/api/v1/auth/<int:user_id>')

