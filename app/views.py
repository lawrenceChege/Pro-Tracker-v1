from flask import Flask, jsonify, abort, request

app = Flask(__name__)

requests = [
    {
        "id": "0",
        "category": "maintenance",
        "title": "fogort password",
        "frequency": "once",
        "description": "i am stupid",
        "status": "Pending"
    },
    {
        "id": "1",
        "category": "repair",
        "title": "fogort hammer",
        "frequency": "once",
        "description": "i am also stupid",
        "status": "Pending"
    },
    {
        "id": "2",
        "category": "maintenance",
        "title": "Tissue out",
        "frequency": "daily",
        "description": "well, not cool",
        "status": "Pending"
    }
]

@app.route('/api/v1/users-dashboard/0/requests/', methods = ['GET'])
def get_user_requests():
    return jsonify ({'requests': requests})

@app.route('/api/v1/users-dashboard/0/requests/<int:request_id>/', methods = ['GET'])
def get_user_request(request_id):
    req = [req for req in requests if req['id']== request_id]
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
        'status': request.json['status', ""]
        
    }
    requests.append(req)
    return jsonify({'req': req}), 201


@app.route('/api/v1/users-dashboard/0/requests/<int:request_id>/', methods=['PUT'])
def update_request(request_id):
    req = [req for req in requests if req['id'] == request_id]
    if len(req) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'category' in request.json and type(request.json['category']) != unicode:
        abort(400)
    if 'frequency' in request.json and type(request.json['frequency']) is not unicode:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'status' in request.json and type(request.json['status']) is not unicode:
        abort(400)

    req[0]['category'] = request.json.get('category', req[0]['category']),
    req[0]['frequency'] = request.json.get('frequency', req[0]['frequency']),
    req[0]['title'] = request.json.get('title', req[0]['title']),
    req[0]['description'] = request.json.get('description', req[0]['description']),
    req[0]['status'] = request.json.get('status', req[0]['status']),
    return jsonify({'req': req[0]})

@app.route('/api/v1/users-dashboard/0/requests/<int:request_id>/', methods=['DELETE'])
def delete_request(request_id):
    req = [req for req in requests if req['id'] == request_id]
    if len(req) == 0:
        abort(404)
    requests.remove(req[0])
    return jsonify({'result': True})



if __name__ == '__main__':
    app.run(debug  =True)
