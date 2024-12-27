from flask import Blueprint, render_template, jsonify

# Blueprint for routes
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/test_mongo')
def test_mongo():
    from . import mongo
    mongo.db.test.insert_one({"message": "Hello, MongoDB!"})
    data = mongo.db.test.find_one({"message": "Hello, MongoDB!"})
    return jsonify({"message": data['message']})

