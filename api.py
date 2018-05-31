from flask import Flask, jsonify, abort, request, make_response, url_for


app = Flask(__name__)


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


@app.route('/')
def hello():
    return 'Hello, World!'

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

@app.route('/api/v1/users-dashboard/0/requests/', methods = ['GET', 'POST'])
def get_user_requests():
    return jsonify({'requests': [make_public_request(req) for req in requests]})

def make_public_request(req):
    new_request = {}
    for field in req:
        if field == 'id':
            new_request['uri'] = url_for('get_user_request', request_id=req['id'], _external=True)
        else:
            new_request[field] = req[field]
    return new_request



if __name__ == '__main__':
    app.run(debug=True)