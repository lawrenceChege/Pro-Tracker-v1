"""API endpoints for the maintenance tracker app"""
from flask import Flask, jsonify, abort, request, make_response, url_for

app = Flask(__name__, static_url_path = "")

# dictionary containing user requests with user ids as the key
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

#details za user
person = {
    "firstname": "lawrence",
    "lastname": "chege",
    "email": "mbuchez8@gmail.com",
    "password": "noyoudont"

}
#request moja
req = {
    "category": "repair",
    "frequency": "once",
    "title": "fogort hammer",
    "description": "i am also stupid",
    "status": "Approved"
}
#details za admin
admin = {

    "email": "admin@gmail.com",
    "password": "admin1234"

}

#function ya kutengeneza uri
def make_public_request(requests):

    new_request = {}
    for field in req:
        if field == 'id':
            new_request['uri'] = url_for('get_user_request', request_id=req['id'], _external=True)
        else:
            new_request[field] = req[field]
    return new_request

#error handler ya bad request
@app.errorhandler(400)
def Bad_request(error):
    """Handle error 400"""
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

#error handler ya page not found
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return make_response(jsonify({'error': 'Not found'}), 404)
#ukifanya vitu hufai .like kuweka put kwa url haina id
@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors"""
    return make_response(jsonify({'error': 'Method Not Allowed '}), 405)

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return make_response(jsonify({'error': 'Internal Server error'}), 500)

#hii inaget request zote za kila user.
#inafaa kuwa ya admin
@app.route('/api/v1/users-dashboard/', methods = ['GET'])
def get_users_requests():
    """Gets requests for all users"""
    return jsonify({"requests": requests, "message": "all requests found successfully"}), 200

#hii inaget request zote za msee mmoja
@app.route('/api/v1/users-dashboard/<int:user_id>', methods = ['GET'])
def get_user_requests(user_id):
    """Gets requests for v single user"""
    req = requests[user_id]
    return jsonify({'req' : req,"message": "all user's requests"}),200

#hii inaget request moja ya msee specific
@app.route('/api/v1/users-dashboard/<int:user_id>/<int:request_id>/', methods = ['GET'])
def get_user_request(user_id, request_id):
    """Gets a specific request from a specific user"""
    req = requests[user_id][request_id]
    if len(req) == 0:
        abort(404)
    return jsonify({'req': req, "message":"Request successfully retrieved"}),200


#hii inacreate request mpya inaongeza kwa user mmoja
@app.route('/api/v1/users-dashboard/<int:user_id>', methods = ['POST'])
def user_create_request(user_id):
    """creates a new request to a specific user"""
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
    reques.append(req)
    return jsonify({'req': req, "message":'Request Added Successfully'}),201


#hii ni ya kuedit
@app.route('/api/v1/users-dashboard/<int:user_id>/<int:request_id>/', methods=['PUT'])
def update_request(user_id, request_id):
    """Modifies a specific request to a specific user"""
    reqw=requests[user_id]
    req = [req for req in reqw if req['id'] == request_id]
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
    return jsonify({'req': req[0], "message":"Request successfully updated"})

#kudelete
@app.route('/api/v1/users-dashboard/<int:user_id>/<int:request_id>/', methods=['DELETE'])
def delete_request(user_id, request_id):
    """Deletes a reuest from a specific user"""
    reqw = requests[user_id]
    req = [req for req in reqw if req['id'] == request_id]
    if len(req) == 0:
        abort(404)
    reqw.remove(req[0])
    return jsonify({'result': True, "message":"Request successfuly deleted"})

#*******************#**************#*************#**************#************#**********#

#hizi zimekataa
@app.route('/api/v1/users-dashboard/<int:user_id>/<category>/', methods = ['GET'])
def get_user_request_by_category(user_id, category):
    pass

#pia hii
@app.route('/api/v1/users-dashboard/0/requests/<status>/', methods = ['GET'])
def get_user_request_by_status(status):
    pass


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
