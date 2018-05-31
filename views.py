from flask import Flask, jsonify, abort, request, make_response, url_for
# from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path = "")
# auth = HTTPBasicAuth()

requests = [
    {
        "id": 0,
        "category": "maintenance",
        "title": "fogort password",
        "frequency": "once",
        "description": "i am stupid",
        "status": "Pending"
    },
    {
        "id": 1,
        "category": "repair",
        "title": "fogort hammer",
        "frequency": "once",
        "description": "i am also stupid",
        "status": "Pending"
    },
    {
        "id": 2,
        "category": "maintenance",
        "title": "Tissue out",
        "frequency": "daily",
        "description": "well, not cool",
        "status": "Pending"
    }
]
person = {
    "firstname": "lawrence",
    "lastname": "chege",
    "email": "mbuchez8@gmail.com",
    "password": "noyoudont"

}

req = {
    "category": "repair",
    "frequency": "once",
    "title": "fogort hammer",
    "description": "i am also stupid",
    "status": "Approved"
}
admin = {

    "email": "admin@gmail.com",
    "password": "admin1234"

}

# unicode = str.encode('utf8')

# @auth.get_password
# def get_password(username):
#     if username == 'admin':
#         return 'babayao'
#     elif username == 'user':
#         return 'kamjamaa'
#     return None

# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.errorhandler(400)
def Bad_request(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/v1/users-dashboard/0/requests/', methods = ['GET'])
def get_user_requests():
    return jsonify({'requests': [make_public_request(req) for req in requests]})

@app.route('/api/v1/users-dashboard/0/requests/<int:request_id>/', methods = ['GET'])
def get_user_request(request_id):
    req = [req for req in requests if req['id']== request_id]
    if len(req) == 0:
        abort(404)
    return jsonify({'req': req})

@app.route('/api/v1/users-dashboard/0/requests/<category>/', methods = ['GET'])
def get_user_request_by_category(category):
    req = [req for req in requests if req['category']== category]
    if len(req) == 0:
        abort(404)
    return jsonify({'req': req})


@app.route('/api/v1/users-dashboard/0/requests/<status>/', methods = ['GET'])
def get_user_request_by_status(status):
    req = [req for req in requests if req['status']== status]
    if len(req) == 0:
        abort(404)
    return jsonify({'req': req})

@app.route('/api/v1/users-dashboard/0/requests/', methods = ['POST'])
def user_create_request():
    if not request.json or not 'title' in request.json:
        abort(400)
    req = {
        'id': requests[-1]['id'] + 1,
        'category': request.json['category'],
        'frequency': request.json['frequency'],
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'status': request.json['status']
        
    }
    requests.append(req)
    return jsonify({'req': req, "message": "Request Added Successfully"}), 201


@app.route('/api/v1/users-dashboard/0/requests/<int:request_id>/', methods=['PUT'])
def update_request(request_id):
    req = [req for req in requests if req['id'] == request_id]
    if len(req) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'category' in request.json and type(request.json['category']) != str:
        abort(400)
    if 'frequency' in request.json and type(request.json['frequency']) is not str:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'status' in request.json and type(request.json['status']) is not str:
        abort(400)

    req[0]['category'] = request.json.get('category', req[0]['category']),
    req[0]['frequency'] = request.json.get('frequency', req[0]['frequency']),
    req[0]['title'] = request.json.get('title', req[0]['title']),
    req[0]['description'] = request.json.get('description', req[0]['description']),
    req[0]['status'] = request.json.get('status', req[0]['status']),
    return jsonify({'req': req[0]})

@app.route('/api/v1/users-dashboard/0/requests/<int:request_id>/', methods=['DELETE'])
# @auth.login_required
def delete_request(request_id):
    req = [req for req in requests if req['id'] == request_id]
    if len(req) == 0:
        abort(404)
    requests.remove(req[0])
    return jsonify({'result': True})

def make_public_request(req):
    new_request = {}
    for field in req:
        if field == 'id':
            new_request['uri'] = url_for('get_user_request', request_id=req['id'], _external=True)
        else:
            new_request[field] = req[field]
    return new_request



if __name__ == '__main__':
    app.run(debug  =True)
