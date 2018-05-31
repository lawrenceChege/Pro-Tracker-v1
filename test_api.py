from api import app

# from flask import Flask, jsonify

import unittest
import json


# app = Flask(__name__)


class BaseTestCase(unittest.TestCase):
    
    def setUp(self):
        """set up app configuration"""
        self.app = app.test_client()
        self.app.testing = True

        self.person = {
            "firstname": "lawrence",
            "lastname": "chege",
            "email": "mbuchez8@gmail.com",
            "password": "noyoudont"
        }
        self.admin = {
            "email": "admin@gmail.com",
            "password": "admin1234"
        }

        self.request = {
            "category": "repair",
            "frequency": "once",
            "title": "fogort hammer",
            "description": "i am also stupid",
            "status": "Approved"
        }
        self.requests = [
            {
                "id": 0,
                "category": "maintenance",
                "title": "fogort password",
                "frequency": "once",
                "description": "i am stupid",
                "status": "Pending"
            },
            {
                "id": 1,
                "category": "repair",
                "title": "fogort hammer",
                "frequency": "once",
                "description": "i am also stupid",
                "status": "Pending"
            },
            {
                "id": 2,
                "category": "maintenance",
                "title": "Tissue out",
                "frequency": "daily",
                "description": "well, not cool",
                "status": "Pending"
            }
        ]

    

    def test_index(self):
        # tester = app.test_client()
        request = self.app.post('/api/v1/users-dashboard/0/requests/',
                            data=json.dumps(self.request),
                            headers={'content-type': "application/json"})
        # request = json.loads(request.data.decode("UTF-8"))
        self.assertEqual(request.status_code, 201)
        # self.assertIn("Request Added Successfully", request["message"]) 
    
    def test_user_view_all_requests(self):
        """Test for viewing all requests"""
        # self.register_user()
        # response = self.login_user()
        # self.assertEqual(response.status_code,200)

        response = self.app.get('/api/v1/users-dashboard/0/requests/',
                            data=json.dumps(self.requests),
                            headers={'content-type': "application/json"})
        # response_message = self.app.get('/api/v1/users-dashboard/0/requests/',
        # data=json.dumps(response), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        # output = json.loads(response.data)
        # self.assertEqual(response, 201)
        self.assertIn(output, "Tissue out")    


class TestRequestsTestCase(BaseTestCase):
    """Tests for Requests"""


if __name__ == '__main__':
    unittest.main()
