"""API endpoints for the maintenance tracker app"""
from flask import Flask, jsonify, abort, request, render_template
from app.users import User_login
import config
import psycopg2

app = Flask(__name__, static_url_path = "/static")
conn= psycopg2.connect("dbname='tracker' user='postgres' password='       ' host='localhost'")
cur = conn.cursor()
@app.route('/', methods = ['GET'])
def index():
    return render_template('home.html')

# #hii inaget request zote za kila user.
# #inafaa kuwa ya admin
# @app.route('/api/v1/requests/', methods = ['GET'])
# def get_users_requests():
#     """Gets requests for all users"""
#     return jsonify({"requests": requests, "message": "all requests found successfully"}), 200

# #hii inaget request zote za msee mmoja
# @app.route('/api/v1/requests/<int:user_id>', methods = ['GET'])
# def get_user_requests(user_id):
#     """Gets requests for v single user"""
#     req = requests[user_id]
#     return jsonify({'req' : req,"message": "all user's requests"}),200

# #hii inaget request moja ya msee specific
# @app.route('/api/v1/requests/<int:user_id>/<int:request_id>/', methods = ['GET'])
# def get_user_request(user_id, request_id):
#     """Gets a specific request from a specific user"""
#     req = requests[user_id][request_id]
#     if len(req) == 0:
#         abort(404)
#     return jsonify({'req': req, "message":"Request successfully retrieved"}),200


#hii inacreate request mpya inaongeza kwa user mmoja
@app.route('/api/v1/requests/', methods = ['POST'])
def user_create_request(user_id):
    """creates a new request to a specific user"""
    if not request.json or not 'title' in request.json:
        abort(400)
    if 'category' in request.json and not isinstance(request.json['category'], str):
        return jsonify({"message" : "Please enter category as either repair or maintenance"})
    if 'frequency' in request.json and not isinstance(request.json['frequency'], str):
        return jsonify({"message" : "Frequency must be a string. Reccomended;once, daily, weekly, monthly or annually"})
    if 'title' in request.json and not isinstance(request.json['title'], str):
        return jsonify({"message" : "Title should be a string"})
    if 'description' in request.json and not isinstance(request.json['description'], str):
        return jsonify({"message" : "Description is a string"})
    category, title, frequency, description, = request.json['category'],request.json['frequency'],request.json['title'],request.json.get('description', "")
    req = {
        'category': category,
        'frequency': frequency,
        'title': title,
        'description': description,
        'status': "pending",
        'user_id': user_id
    }
    try:
            cur.execute("""SELECT * FROM requests""")
            result = cur.fetchall()
            if title in result:
                return "Request already exists!"
            else:
                cur.execute(""" INSERT INTO requests (category,
                                                        frequency,
                                                        title,
                                                        description,
                                                        status,
                                                        user_id) VALUES (%(category)s,
                                                                        %(frequency)s,
                                                                        %(title)s,
                                                                        %(description)s,
                                                                        %(status)s,
                                                                        %(user_id)s)""", req)
                conn.commit()
                return "Request created successfully!"
    except:
        print ("I could not  select from requests")

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
