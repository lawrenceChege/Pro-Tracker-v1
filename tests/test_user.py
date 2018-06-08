"""Tests for users"""
from tests.base import BaseTestCase
from app import app 
from passlib.hash import pbkdf2_sha256

import unittest
import psycopg2
import json

class TestUserTestCase(BaseTestCase):
    """ Test for normal user"""
       
    def test_user_signup(self):
        """Test for user signup"""
        #no username
        response = self.app.post('/api/v1/auth/signup',
                                 data=json.dumps(self.person_no_username),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,404)
        print(response)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Username is required')

        #no email
        response = self.app.post('api/v1/auth/signup',
                                 data=json.dumps(self.person_no_email),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Email is required!')

        #invalid email
        response = self.app.post('api/v1/auth/signup',
                                 data=json.dumps(self.person_invalid_email),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'User created successfully!')
        #no password
        response = self.app.post('api/v1/auth/signup',
                                 data=json.dumps(self.person_no_password),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Passord is required!')
        #correct details
        response = self.app.post('api/v1/auth/signup',
                                 data=json.dumps(self.person),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,201)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'User created successfully!')
        #existing user
        response = self.app.post('api/v1/auth/signup',
                                 data=json.dumps(self.person_existing_user),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'User already exists')

    def test_login(self):
        """Test for login"""
        #nopassword
        response = self.app.post('api/v1/auth/login',
                                 data=json.dumps(self.no_password),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Password is required')
        #no username
        response = self.app.post('api/v1/auth/login',
                                 data=json.dumps(self.no_username),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Password is required!')
        #incorrect
        response = self.app.post('api/v1/auth/login',
                                 data=json.dumps(self.wrong_login),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,401)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'please check your credentials')
        #empty
        response = self.app.post('api/v1/auth/signup',
                                 data=json.dumps(self.correct_login),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,200)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'User successfully logged in')

    def test_get_user(self, user_id):
        """Test for get user"""
        response = self.app.get('api/v1/auth/<int:user_id>')
        self.assertEqual(response.status_code,200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "user not found!")
        self.assertIn(data['message'], "username")
        
            
        