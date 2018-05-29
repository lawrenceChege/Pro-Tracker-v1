"""Tests for users"""

from base import BaseTestCase

import json


class TestUsersTestCase(BaseTestCase):
    """Tests for user authentication and authorization"""

    def test_users_signup_empty_firstname(self):
        response = self.app.post('/api/v1/auth/register',
        data=json.dumps(
            dict(username="", email="jim@gamil.com", password="12345")),
        headers={'content-type': "application/json"})
        response_msg = json.loads(response.data.decode())
        self.assertIn("Username is required",response_msg["message"])

    def test_users_signup_empty_lastname(self):
        pass

    def test_users_signup_empty_email(self):
        pass

    def test_users_signup_empty_password(self):
        pass

    def test_users_signup(self):
        pass
    
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
