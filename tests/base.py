""" This is the base class for all the tests"""
from app.app import app
from unittest import TestCase
import unittest
import os
import json

class BaseTestCase(TestCase):
    """ set up configurations for the test environment"""
    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 
    def setUp(self):
        """set up app configuration"""
        self.app = app.test_client()
        self.app.testing = True

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

        self.request={
            "category":"maintenance",
            "title":"fogort password",
            "frequency":"once",
            "description":"i am stupid",
            "status":"Pending"
        }
        self.requests = [
            {
            "id":"0",
            "category":"maintenance",
            "title":"fogort password",
            "frequency":"once",
            "description":"i am stupid",
            "status":"Pending"
            },
            {
            "id":"1",
            "category":"repair",
            "title":"fogort hammer",
            "frequency":"once",
            "description":"i am also stupid",
            "status":"Pending"
            },
            {
            "id":"2",
            "category":"maintenance",
            "title":"Tissue out",
            "frequency":"daily",
            "description":"well, not cool",
            "status":"Pending"
            }
            ]
            
    def register_user(self):
        """Registration helper"""
        ret = self.app.post('/api/v1/auth/signup',
        data = json.dumps(self.person),
        headers = {'content-type':"appliction/json"})
        return ret

    def register_admin(self):
        """Registration helper"""
        ret = self.app.post('/api/v1/auth/signup',
        data = json.dumps(self.admin),
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
        """ New  request helper"""
        ret = self.app.post('/api/v1/users-dashboard/0/requests/0/',
        data = json.dumps(self.request),
        headers = {'content-type':"appliction/json"})
        return ret

    def load_requests(self):
        ret = self.app.post('/api/v1/users-dashboard/0/requests/',
        data = json.dumps(self.requests),
        headers = {'content-type':"appliction/json"})
        return ret

    # def tearDown(self):
    #     USERS.clear()
    #     REQUESTS.clear()
    #     Requests.count = 0
if __name__ == '__main__':
    unittest.main()

