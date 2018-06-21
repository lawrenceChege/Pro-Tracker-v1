""" This is the base class for all the tests"""
from unittest import TestCase
from app import app
import unittest
import json


class BaseTestCase(TestCase):
    """ set up configurations for the test environment"""
    @classmethod
    def setUpClass(self):
        """set up app configuration"""
        self.app = app.test_client()
        self.app.testing = True

        self.person = {
            "username": "lau lau",
            "email": "mbuchez9@gmail.com",
            "password": "maembembili"
        }
        self.person_no_username ={
            "email": "mbuchez8@gmail.com",
            "password": "maembembili"
        }
        self.person_no_email = {
            "username": "lawrence",
            "password": "maembembili"
        }
        self.person_no_password = {
            "username": "lawrence",
            "email": "mbuchez8@gmail.com",
        }
        self.person_invalid_email = {
            "username": "lawrence",
            "email": "mbuchez.com",
            "password": "maembembili"
        }
        self.person_existing_user ={
            "username": "test",
            "email": "test@gmail.com",
            "password": "password"
        }
        self.correct_login = {"username": "lau lau",
                              "password": "maembembili"}
        self.wrong_login = {"username": "lawrence",
                            "password": "mistubishi"}
        self.no_username = {"username": "",
                            "password": "maembembili"}
        self.no_password = {"username": "lawrence",
                            "password": ""}
        self.admin = {
            "username": "admin",
            "email": "admin@gmail.com",
            "password": "admin1234"
        }
        self.admin_correct = {"username": "admin",
                              "password": "admn1234"}
        self.admin_wrong = {"username": "lawrence",
                            "password": "mimi"}

        self.request = {
            "category": "repair",
            "frequency": "once",
            "title": "fogort hammer",
            "description": "i am also stupid",
            "status": "Pending"
        }
        self.request_no_category= {
            "frequency": "once",
            "title": "fogort hammer",
            "description": "i am also stupid",
            "status": "pending"
        }
        self.request_no_frequency={
            "category": "repair",
            "title": "fogort hammer",
            "description": "i am also stupid",
            "status": "Pending"
        }
        self.request_no_description={
            "category": "repair",
            "frequency": "once",
            "title": "fogort hammer",
            "status": "pending"
        }
        self.request_no_title={
            "category": "repair",
            "frequency": "once",
            "description": "fogort hammer",
            "status": "pending"
        }
        self.request_approve={
            "status": "Approve"
        }
        self.request_reject={
            "status": "Rejected"
        }
        self.request_resolve={
            "status": "Resolved"
        }

    @classmethod
    def tearDownClass(cls):
        pass
        
if __name__ == '__main__':
    unittest.main()
