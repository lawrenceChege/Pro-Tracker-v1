"""Tests for users"""
from tests.base import BaseTestCase
from app import app 
from passlib.hash import pbkdf2_sha256

import unittest
import psycopg2
import json

class TestRequestTestCase(BaseTestCase):
    """ Test for normal user"""
    def setUp(self, username, email, password):
        """class initializations"""
        self.username = username
        self.email = email
        self.password = pbkdf2_sha256.hash("password")
        self.app = app.test_client()

    def test_user_signup(self):
        """Test for user signup"""
        data = {"username": "lawrence",
                "email": "mbchez8@gmail,com",
                "password": "maembembili"}

        response = self.app.post('api/v1/auth',
                                 data=data,
                                 content_type="application/json")
        self.assertEqual(response.status_code,201)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'User created successfully!')

    def test_login(self):
        """Test for login"""
        correct_cred = {"username": "lawrence",
                        "password": "maembembili"}
        wrong_cred = {"username": "lawrence",
                      "password": "mistubishi"}
        response = self.app.post('api/v1/auth',
        data = correct_cred)
