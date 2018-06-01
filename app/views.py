from flask import Flask, jsonify, abort, request, make_response, url_for
# from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path = "")
# auth = HTTPBasicAuth()

requests = {
    0: [

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

    ],
    1: [

        {
            "id": 0,
            "category": "maintenance",
            "title": "sad",
            "frequency": "once",
            "description": "just sad",
            "status": "Pending"
        },
        {
            "id": 1,
            "category": "repair",
            "title": "toilet broken",
            "frequency": "once",
            "description": "shit happens",
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

    ],
    2: [
        {
            "id": 0,
            "category": "maintenance",
            "title": "laptop battery dead",
            "frequency": "annually",
            "description": "they should really work on battery life",
            "status": "Pending"
        },
        {
            "id": 1,
            "category": "repair",
            "title": "heart broken",
            "frequency": "once",
            "description": "i miss her",
            "status": "Pending"
        },
        {
            "id": 2,
            "category": "maintenance",
            "title": "bulb blown up",
            "frequency": "once",
            "description": "well, ligts out",
            "status": "Pending"
        }

    ]
}

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


def make_public_request(requests):

    new_request = {}
    for field in req:
        if field == 'id':
            new_request['uri'] = url_for('get_user_request', request_id=req['id'], _external=True)
        else:
            new_request[field] = req[field]
    return new_request

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


@app.route('/api/v1/users-dashboard/', methods = ['GET'])
def get_users_requests():
    return jsonify({"requests": requests})

@app.route('/api/v1/users-dashboard/<int:user_id>', methods = ['GET'])
def get_user_requests(user_id):
    req = requests[user_id]
    return jsonify({'req' : req})


@app.route('/api/v1/users-dashboard/<int:user_id>/<int:request_id>/', methods = ['GET'])
def get_user_request(user_id, request_id):
    req = requests[user_id][request_id]
    if len(req) == 0:
        abort(404)
    return jsonify({'req': req})

@app.route('/api/v1/users-dashboard/<int:user_id>/<category>/', methods = ['GET'])
def get_user_request_by_category(user_id, category):
    pass


@app.route('/api/v1/users-dashboard/0/requests/<status>/', methods = ['GET'])
def get_user_request_by_status(status):
    pass

@app.route('/api/v1/users-dashboard/<int:user_id>', methods = ['POST'])
def user_create_request(user_id):
    if not request.json or not 'title' in request.json:
        abort(400)
    reques = requests[user_id]
    req = {
        'id': reques[-1]['id'] + 1,
        'category': request.json['category'],
        'frequency': request.json['frequency'],
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'status': request.json['status']
        
    }
    # requests.append(req)
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

@app.route('/api/v1/admin-dashboard/users/<int:user_id>/requests/', methods=['GET'])
def admin_get_a_user_request(user_id):
    pass

@app.route('/api/v1/admin-dashboard/users/requests/', methods=['GET'])
def admin_get_users_requests():
    pass

@app.route('/api/v1/admin-dashboard/users/requests/<category>', methods=['GET'])
def admin_get_requests_by_category():
    pass

@app.route('/api/v1/admin-dashboard/users/requests/<status>', methods=['GET'])
def admin_get_requests_by_status():
    pass

@app.route('/api/v1/admin-dashboard/users/0/requests/0', methods=['PUT'])
def admin_modify_a_user_request():
    pass

if __name__ == '__main__':
    app.run(debug  =True)
