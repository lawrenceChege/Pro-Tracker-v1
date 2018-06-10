import re
from flask import request, jsonify


def blank(**data):
    for key in data:
        name = re.sub(r'\s+', '', data[key])
        if not name:
            return {'message': key + ' is required'}


def check_email(data):
    vemail = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", data)
    if not vemail:
        return {'message': 'Email is invalid'}


def key_blank(**data):
    for key in data:
        if data[key] is None:
            return {'message': key + ' is missing'}


def key_password(password):
    password = re.match(r'[a-zA-Z_]+[\d\w]{8,}', password)
    if password is None:
        return {'message': 'password should contain atleast (a-z), (0-4), (-), characters(8)'}

def check_request(data):
    if not request.json or not 'title' in request.json:
        return jsonify({"message" : "check your request type"})
    if 'category' in request.json and not isinstance(request.json['category'], str):
        return jsonify({"message" : "Please enter category as either repair or maintenance"})
    if 'frequency' in request.json and not isinstance(request.json['frequency'], str):
        return jsonify({"message" : "Frequency must be a string. Reccomended;once, daily, weekly, monthly or annually"})
    if 'title' in request.json and not isinstance(request.json['title'], str):
        return jsonify({"message" : "Title should be a string"})
    if 'description' in request.json and not isinstance(request.json['description'], str):
        return jsonify({"message" : "Description is a string"})