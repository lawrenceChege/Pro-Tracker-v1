""" class for index route"""

from flask import render_template
from flask_restful import Resource

class IndexPage(Resource):
    """define methods"""
    def get(self):
        return render_template('home.html')

