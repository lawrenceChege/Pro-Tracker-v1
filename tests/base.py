""" This is the base class for all the tests"""
from app import app, REQUESTS,USERS
from unittest import TestCase

import os
import json

class BaseTestCase(TestCase):
    """ set up configurations for the test environment"""
    def setUp(self):
        """set up app configuration"""
        app.testing = True
        self.app = app.test_client()

        self.person = {
            "firstname":"lawrence",
            "lastname":"chege",
            "email":"mbuchez8@gmail.com",
            "password":"noyoudont"
        }
        self.admin ={
            "email":"admin@gmail.com",
            "password":"admin1234"
        }

        self.new_request={
            "category":"maintenance",
            "title":"fogort password",
            "frequency":"once",
            "description":"i am stupid"
        }

    def register_user(self):
        """Registration helper"""
        ret = self.app.post('/api/v1/auth/signup',
        data = json.dumps(self.person),
        headers = {'content-type':"appliction/json"})
        return ret
        
    def login_user(self):
        """sign in helper"""
        ret = self.app.post('/api/v1/auth/signin',
        data = json.dumps(self.person),
        headers = {'content-type':"appliction/json"})
        return ret
    
    def login_admin(self):
        """sign in helper for admin"""
        ret = self.app.post('/api/v1/auth/signin',
        data = json.dumps(self.admin),
        headers = {'content-type':"appliction/json"})
        return ret

    def logout(self):
        """Logout helper function."""
        return self.app.get('/api/v1/auth/logout', follow_redirects=True)


    def new_request(self):
        """ New w request helper"""
        ret = self.app.post('/api/v1/dashboard/user<id>/new-request/',
        data = json.dumps(self.new_request),
        headers = {'content-type':"appliction/json"})
        return ret
    
    
    def tearDown(self):
        USERS.clear()
        REQUESTS.clear()
        Requests.count = 0


