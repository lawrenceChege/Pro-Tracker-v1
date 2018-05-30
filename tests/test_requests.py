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
        pass

    def test_user_view_a_request(self):
        """Test for vieving a particular request"""
        pass

    def test_user_view_a_request_category_by_category(self):
        """test for viewing a request category by category
        Categories include:Maintenance and Repair """
        pass

    def test_user_view_a_request_category_by_status(self):
        """Test for viewing a request category by status"""
        pass

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

    
