"""Test for methods applied to requests"""

from tests.base import BaseTestCase
from app.views import app, person, req, requests, admin

from app import views
import unittest

import json


all_requests  = dict([(key,d[key]) for d in requests for key in d])

class TestRequestsTestCase(BaseTestCase):
    """Tests for Requests"""

    def setUp(self):
        self.person = person
        self.admin = admin
        self.request = req
        self.requests = all_requests
        self.app = app.test_client()
        self.app.testing = True
        # self.register_user()
        # response = self.login_user()
        # self.assertEqual(response.status_code,200)
        response= self.app.post('/api/v1/users-dashboard/0/requests/',
                                data=json.dumps(self.requests), 
                                headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,201)

    def test_user_make_new_request(self):
        """Test for making new request"""

        response= self.app.post('/api/v1/users-dashboard/0/requests/',
                                data=json.dumps(self.request), 
                                headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 201)
        # self.assertIn("Request Added Successfully",
        #               response["message"])

    def test_user_view_all_requests(self):
        """Test for viewing all requests"""

        response = self.app.get('/api/v1/users-dashboard/0/requests')
        self.assertEqual(response.status_code, 200)
        

    def test_user_view_a_request(self):
        """Test for vieving a particular request"""

        response_message = self.app.get('/api/v1/users-dashboard/0/requests/0/')
        self.assertEqual(response_message.status_code, 200)
        response = json.dumps(response_message)
        self.assertIn("title", response)

    def test_user_view_a_request_category_by_category(self):
        """test for viewing a request category by category
            Categories include:
                                -Maintenance 
                                -Repair """

        response_message = self.app.get('/api/v1/users-dashboard/0/requests/repair/')
        self.assertEqual(response_message.status_code, 200)
       

    def test_user_view_a_request_category_by_status(self):
        """Test for viewing a request category by status
            Status include:
                            -pending
                            -approved
                            -resolved
                            -rejected"""

        response_message = self.app.get('/api/v1/users-dashboard/0/requests/repair/')
        self.assertEqual(response_message.status_code, 200)


    def test_user_modify_a_request(self):
        """Test for modifying a request"""
        
        response = self.app.put('/api/v1/users-dashboard/0/requests/3/',
                                        data=json.dumps(
                                            dict(category="repair")),
                                        headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 200)

    def test_user_delete_a_request(self):
        """Test for deleting a request"""

        response = self.app.delete('/api/v1/users-dashboard/0/requests/3/')
        self.assertEqual(response.status_code, 200)


# class AdminTestRequestsTestCase(TestRequestsTestCase):

#     def setUp(self):
#         self.admin = admin
#         self.person = person
#         self.request = req
#         self.requests = all_requests
#         self.app = app.test_client()
#         self.app.testing = True
#         # self.register_user()
#         # response = self.login_user()
#         # self.assertEqual(response.status_code,200)
#         response= self.app.post('/api/v1/users-dashboard/0/requests/',
#                                 data=json.dumps(self.requests), 
#                                 headers={'content-type': "application/json"})
#         self.assertEqual(response.status_code,201)

#     def test_admin_view_a_users_requests(self):
#         """Test if Admin can view a user's requests"""

#         response = self.app.get('/api/v1/admin-dashboard/users/0/requests/')
#         self.assertEqual(response.status_code, 200)

#     def test_admin_view_all_users_request(self):
#         """Test if admin can view all requests from all users"""

#         response = self.app.get('/api/v1/admin-dashboard/requests/')
#         self.assertEqual(response.status_code, 404)

#     def test_admin_modify_a_users_request_status(self):
#         """Test admin modify a user's request status"""

#         response = self.new_request()
#         response_message = json.loads(response.data.decode("UTF-8"))
#         self.assertIn("Request Added Successfully",
#                       response_message["message"])

#         response = self.logout()
#         self.assertEqual(response.status_code, 200)

#         response_message = self.app.put('/api/v1/admin-dashboard/0/requests/0',
#                                         data=json.dumps(
#                                             dict(status="Approved")),
#                                         headers={'content-type': "application/json"})
#         self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
