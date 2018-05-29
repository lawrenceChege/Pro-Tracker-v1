"""Tests for users"""

from base import BaseTestCase

import json


class TestUsersTestCase(BaseTestCase):
    """Tests for user authentication and authorization"""

    def test_users_signup_empty_firstname(self):
        """ tests for missing firstname"""
        response = self.app.post('/api/v1/auth/signup',
        data=json.dumps(
            dict(firstname="",lastname="chege" email="mbuchez8@gamil.com", password="noyoudont")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Firstname is required",response_msg["message"])

    def test_users_signup_empty_lastname(self):
         """ tests for missing lastname"""
        response = self.app.post('/api/v1/auth/signup',
        data=json.dumps(
            dict(firstname="lawrence",lastname="" email="mbuchez8@gamil.com", password="noyoudont")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Lastname is required",response_msg["message"])

    def test_users_signup_empty_email(self):
         """ tests for missing email"""
        response = self.app.post('/api/v1/auth/signup',
        data=json.dumps(
            dict(firstname="lawrence",lastname="chege" email="", password="noyoudont")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("email is required",response_msg["message"])

    def test_users_signup_empty_password(self):
         """ tests for missing password"""
        response = self.app.post('/api/v1/auth/signup',
        data=json.dumps(
            dict(firstname="lawrence",lastname="chege" email="mbuchez8@gamil.com", password="")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Password is required",response_msg["message"])

    def test_users_signup(self):
         """ tests for good sign up"""
        response = self.app.post('/api/v1/auth/signup',
        response = self.register_user()    
        response_msg = json.loads(response.data.decode())
        self.assertIn("User successfully registered", response_msg["message"])
    
    def test_users_signin(self):
        pass

    def test_users_signin_wrong_email(self):
        pass
    
    def test_users_signin_wrong_password(self):
        pass

    def test_users_signin_empty_email(self):
        pass

    def test_users_signin_empty_password(self):
        pass

     def test_users_signin_wrong_password(self):
        pass

    def test_users_signin_not_registered_email(self):
        pass
    
    def test_admin_signin(self):
        pass

    def test_admin_signin_wrong_password(self):
        pass
