"""Tests for users"""
from tests.base import BaseTestCase
from app.users import app

import unittest
import psycopg2
import json

class TestRequestTestCase(BaseTestCase):
    """ Test for normal user"""
    def setUp(self):
        """class initializations"""
        self.app = app.test_client()

    def test_user_signup(self):
        """Test for user signup"""
        pass
