"""Test for methods applied to requests"""
# from flask import url_for
from tests.base import BaseTestCase
from app.views import app, person, req, not_found, requests, admin

import unittest
import json


class TestRequestsTestCase(BaseTestCase):
    """Tests for Requests"""

    def setUp(self):
        self.person = person
        self.admin = admin
        self.request = req
        self.requests = requests
        self.app = app.test_client()
        self.app.testing = True
        response= self.app.post('/api/v1/requests/',
                                data=json.dumps(self.requests),
                                headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,405)

    def test_user_make_new_request(self):
        """Test for making new request"""

        response = self.app.post('/api/v1/requests/0', data=json.dumps(
            self.request), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'],'Request Added Successfully')

    def test_user_view_all_requests(self):
        """Test for viewing all requests"""

        response = self.app.get('/api/v1/requests/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual( data['message'] , "all requests found successfully")

    def test_user_view_a_users_requests(self):
        """Test for viewing a user's requests """
        response = self.app.get('/api/v1/requests/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual( data['message'] , "all requests found successfully")
        

    def test_user_view_a_request(self):
        """Test for vieving a particular request"""

        response_message = self.app.get('/api/v1/requests/0/0/')
        self.assertEqual(response_message.status_code, 200)
        data = json.loads(response_message.get_data())
        self.assertEqual( data['message'] , "Request successfully retrieved")
    

    def test_user_view_a_request_category_by_category(self):
        """test for viewing a request category by category
            Categories include:
                                -Maintenance
                                -Repair """
        pass
       

    def test_user_view_a_request_category_by_status(self):
        """Test for viewing a request category by status
            Status include:
                            -pending
                            -approved
                            -resolved
                            -rejected"""

        pass


    def test_user_modify_a_request(self):
        """Test for modifying a request"""
        
        response = self.app.put('/api/v1/requests/0/1/',
                                        data=json.dumps(
                                            dict(category="repair")),
                                        headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual( data['message'] , "Request successfully updated")

    def test_user_delete_a_request(self):
        """Test for deleting a request"""

        response = self.app.delete('/api/v1/requests/0/2/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual( data['message'] , "Request successfuly deleted")

    def test_404(self):
        response = not_found(error)
        data =json.loads(response.get_data())
        self.assertEqual(data['error'], 'Not found')

class AdminTestRequestsTestCase(TestRequestsTestCase):

    def setUp(self):
        self.admin = admin
        self.person = person
        self.request = req
        self.requests = requests
        self.app = app.test_client()
        self.app.testing = True
        

    def test_admin_view_a_users_requests(self):
        """Test if Admin can view a user's requests"""
        pass


    def test_admin_view_all_users_request(self):
        """Test if admin can view all requests from all users"""
        pass


    def test_admin_modify_a_users_request_status(self):
        """Test admin modify a user's request status"""

        pass



if __name__ == '__main__':
    unittest.main()
