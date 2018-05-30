"""Test for methods applied to requests"""
from base import BaseTestCase

import json

class TestRequestsTestCase(BaseTestCase):
    """Tests for Requests"""

    def test_user_make_new_request(self):
        """Test for making new request"""
        self.register_user()
        response = self.login_user()
        self.assertEqual(response.status_code,200)

        self.new_request()
        response = self.new_request()
        response_message = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 201)
        self.assertIn("Request Added Successfully", response_message["message"]) 

    def test_user_view_all_requests(self):
        """Test for viewing all requests"""
        self.register_user()
        response = self.login_user()
        self.assertEqual(response.status_code,200)

        response = self.load_requests()
        response_message = self.app.get('/api/v1/users-dashboard/0/requests/',
        data=json.dumps(response), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        output = json.loads(response.data)
        self.assertEqual(response_message, 201)
        self.assertIn(output, "Tissue out")      
        


    def test_user_view_a_request(self):
        """Test for vieving a particular request"""
        self.register_user()
        response = self.login_user()
        self.assertEqual(response.status_code,200)

        response = self.new_request()
        response_message = self.app.get('/api/v1/users-dashboard/0/requests/0/',
        data=json.dumps(response), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        output = json.loads(response.data)
        self.assertEqual(response_message, 201)
        self.assertIn(output, "I am Stupid") 

    def test_user_view_a_request_category_by_category(self):
        """test for viewing a request category by category
        Categories include:Maintenance and Repair """
        self.register_user()
        response = self.login_user()
        self.assertEqual(response.status_code,200)

        response = self.load_requests()
        response_message = self.app.get('/api/v1/users-dashboard/0/requests/category/Repair',
        data=json.dumps(response), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        output = json.loads(response.data)
        self.assertEqual(response_message, 201)
        self.assertIn(output, "repair")
        self.assertNotIn(output, "maintenance") 

    def test_user_view_a_request_category_by_status(self):
        """Test for viewing a request category by status"""
        self.register_user()
        response = self.login_user()
        self.assertEqual(response.status_code,200)

        response = self.load_requests()
        response_message = self.app.get('/api/v1/users-dashboard/0/requests/status/pending',
        data=json.dumps(response), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        output = json.loads(response.data)
        self.assertEqual(response_message, 201)
        self.assertIn(output, "Pending") 
        self.assertNotIn(output, "Approved")
        self.assertNotIn(output, "Resolved")
        self.assertNotIn(output, "Rejected")

    def test_user_modify_a_request(self):
        """Test for modifying a request"""
        pass

    def test_user_delete_a_request(self):
        """Test for deleting a request"""
        pass

    def test_admin_view_a_users_requests(self):
        """Test if Admin can view a user's requests"""
        pass

    def test_admin_view_all_users_request(self):
        """Test if admin can view all requests from all users"""
        pass

    def test_admin_modify_a_users_request_status(self):
        """Test admin modify a user's request status"""
        pass

    
