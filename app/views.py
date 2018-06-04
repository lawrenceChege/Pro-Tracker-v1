"""API endpoints for the maintenance tracker app"""
from flask import Flask, jsonify, abort, request, render_template

app = Flask(__name__, static_url_path = "/static")

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
            },]}

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

@app.route('/', methods = ['GET'])
def index():
    return render_template('home.html')

#hii inaget request zote za kila user.
#inafaa kuwa ya admin
@app.route('/api/v1/requests/', methods = ['GET'])
def get_users_requests():
    """Gets requests for all users"""
    return jsonify({"requests": requests, "message": "all requests found successfully"}), 200

#hii inaget request zote za msee mmoja
@app.route('/api/v1/requests/<int:user_id>', methods = ['GET'])
def get_user_requests(user_id):
    """Gets requests for v single user"""
    req = requests[user_id]
    return jsonify({'req' : req,"message": "all user's requests"}),200

#hii inaget request moja ya msee specific
@app.route('/api/v1/requests/<int:user_id>/<int:request_id>/', methods = ['GET'])
def get_user_request(user_id, request_id):
    """Gets a specific request from a specific user"""
    req = requests[user_id][request_id]
    if len(req) == 0:
        abort(404)
    return jsonify({'req': req, "message":"Request successfully retrieved"}),200


#hii inacreate request mpya inaongeza kwa user mmoja
@app.route('/api/v1/requests/<int:user_id>', methods = ['POST'])
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
@app.route('/api/v1/requests/<int:user_id>/<int:request_id>/', methods=['PUT'])
def update_request(user_id, request_id):
    """Modifies a specific request to a specific user"""
    reqw=requests[user_id]
    req = [req for req in reqw if req['id'] == request_id]
    if len(req) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'category' in request.json and not isinstance(request.json['category'], str):
        return jsonify({"message" : "Please enter category as either repair or maintenance"})
    if 'frequency' in request.json and not isinstance(request.json['frequency'], str):
        return jsonify({"message" : "Frequency must be a string. Reccomended;once, daily, weekly, monthly or annually"})
    if 'title' in request.json and not isinstance(request.json['title'], str):
        return jsonify({"message" : "Title should be a string"})
    if 'description' in request.json and not isinstance(request.json['description'], str):
        return jsonify({"message" : "Description is a string"})
    if 'status' in request.json and not isinstance(request.json['status'], str) :
        return jsonify({"message" : "status  is a string"})

    req[0]['category'] = request.json.get('category', req[0]['category']),
    req[0]['frequency'] = request.json.get('frequency', req[0]['frequency']),
    req[0]['title'] = request.json.get('title', req[0]['title']),
    req[0]['description'] = request.json.get('description', req[0]['description']),
    req[0]['status'] = request.json.get('status', req[0]['status']),
    return jsonify({'req': req[0], "message":"Request successfully updated"})

#kudelete
@app.route('/api/v1/requests/<int:user_id>/<int:request_id>/', methods=['DELETE'])
def delete_request(user_id, request_id):
    """Deletes a reuest from a specific user"""
    reqw = requests[user_id]
    req = [req for req in reqw if req['id'] == request_id]
    if len(req) == 0:
        abort(404)
    reqw.remove(req[0])
    return jsonify({'result': True, "message":"Request successfuly deleted"})

if __name__ == '__main__':
    app.run()
