"""Tests for users"""
from tests.base import BaseTestCase
from app import app 
from passlib.hash import pbkdf2_sha256

import unittest
import psycopg2
import json

class TestRequestTestCase(BaseTestCase):
    """ Test for normal user"""
    def setUp(self):
        """class initializations"""
        self.person_no_username = self.person_no_username
        # self.username = username
        # self.email = email
        # self.password = pbkdf2_sha256.hash("password")
        # self.app = app.test_client()

    def test_user_signup(self):
        """Test for user signup"""
        #no username
        response = self.app.post('/api/v1/auth/',
                                 data=json.dumps(self.person_no_username),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Username is required')

        #no email
        response = self.app.post('api/v1/auth/',
                                 data=json.dumps(self.person_no_email),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,201)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Email is required!')

        #invalid email
        response = self.app.post('api/v1/auth/',
                                 data=json.dumps(self.person_invalid_email),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,201)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'User created successfully!')
        #no password
        response = self.app.post('api/v1/auth/',
                                 data=json.dumps(self.person_no_password),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,201)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Passord is required!')
        #correct details
        response = self.app.post('api/v1/auth/',
                                 data=json.dumps(self.person),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,201)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'User created successfully!')
        #existing user
        response = self.app.post('api/v1/auth/',
                                 data=json.dumps(self.person_existing_user),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,201)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'User already exists')

    def test_login(self):
        """Test for login"""
        # response = self.app.post('/api/v1/requests/0', data=json.dumps(
        #     self.request)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'],'Request Added Successfully')
        #correct
        #incorrect
        #empty
        #