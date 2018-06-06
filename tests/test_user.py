"""Tests for users"""
from tests.base import BaseTestCase
from app.users import app
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
        
