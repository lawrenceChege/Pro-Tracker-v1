"""Tests for users"""

from base import BaseTestCase
from app import app 

import json
import os


class TestUsersTestCase(BaseTestCase):
    """Tests for user authentication and authorization"""

    def test_users_signup_empty_firstname(self):
        """ tests for missing firstname"""
        response = self.app.post('/api/v1/auth/signup',
        data=json.dumps(
            dict(firstname="", lastname="chege", email="mbuchez8@gamil.com", password="noyoudont")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Firstname is required", response_msg["message"])

    def test_users_signup_empty_lastname(self):
        """ tests for missing lastname"""
        response = self.app.post('/api/v1/auth/signup',
            data=json.dumps(
            dict(firstname="lawrence",lastname="", email="mbuchez8@gamil.com", password="noyoudont")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Lastname is required",response_msg["message"])

    def test_users_signup_empty_email(self):
        """ tests for missing email"""
        response = self.app.post('/api/v1/auth/signup',
        data=json.dumps(
            dict(firstname="lawrence",lastname="chege", email="", password="noyoudont")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("email is required",response_msg["message"])

    def test_users_signup_empty_password(self):
        """ tests for missing password"""
        response = self.app.post('/api/v1/auth/signup',
        data=json.dumps(
            dict(firstname="lawrence",lastname="chege", email="mbuchez8@gamil.com", password="")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Password is required",response_msg["message"])

    def test_users_signup_registered_email(self):
        """ tests for registered email"""
        response = self.app.post('/api/v1/auth/signup',
        data=json.dumps(
            dict(firstname="lawrence",lastname="chege", email="mbuchez8@gamil.com", password="")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Email already Registered",response_msg["message"])

    def test_users_signup(self):
        """ tests for good sign up"""
        response = self.app.post('/api/v1/auth/signup'),
        response = self.register_user()    
        response_msg = json.loads(response.data.decode())
        self.assertIn("User successfully registered", response_msg["message"])
    
    def test_users_signin(self):
        """returns correct login"""
        self.register_user()
        ret = self.login_user()
        data = json.loads(ret.get_data())
        self.assertIn('token', data)

    def test_users_signin_wrong_email(self):
        """ tests for wrong email"""
        response = self.app.post('/api/v1/auth/signin',
        data=json.dumps(
            dict(email="mbuchez99998@gamil.com", password="noyoudont")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Wrong Credentials!",response_msg["message"])
    
    def test_users_signin_wrong_password(self):
        """ tests for wrong Password"""
        response = self.app.post('/api/v1/auth/signin',
        data=json.dumps(
            dict(email="mbuchez8@gamil.com", password="noyoudonthow")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Wrong Credentials!",response_msg["message"])

    def test_users_signin_empty_email(self):
        """ tests for empty email"""
        response = self.app.post('/api/v1/auth/signin',
        data=json.dumps(
            dict(email="", password="noyoudont")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Email is Required!",response_msg["message"])

    def test_users_signin_empty_password(self):
        """ tests for empty password"""
        response = self.app.post('/api/v1/auth/signin',
        data=json.dumps(
            dict(email="mbuchez8@gamil.com", password="")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Password required!",response_msg["message"])

    def test_users_signin_not_registered_email(self):
        """ tests for not registered user email"""
        response = self.app.post('/api/v1/auth/signin',
        data=json.dumps(
            dict(email="somenewguy@gamil.com", password="noyoudont")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Wrong email or user not registered",response_msg["message"])
    
    def test_admin_signin(self):
        """returns correct login"""
        self.register_user()
        ret = self.login_admin()
        data = json.loads(ret.get_data())
        self.assertIn('token', data)

    def test_admin_signin_wrong_password(self):
        """ tests for wrong Password"""
        response = self.app.post('/api/v1/auth/signin',
        data=json.dumps(
            dict(email="admin@gamil.com", password="noyoudonthow")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Wrong Credentials!",response_msg["message"])

    def test_logout(self):
        """Test for successful logout"""
        response = self.logout()
        self.assertIn("You have successfylly logged out", response["message"])
