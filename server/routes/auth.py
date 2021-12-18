from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from db.database import storage_db
from storage.scores import Scores
scores_database = Scores()

auth = Blueprint("auth", __name__)

@auth.route("/scores")
def get_scores():
    return jsonify(scores_database.get_scores())


@auth.route("/save_scores", methods=["POST"])
def save_scores():
    score = request.form["score"]
    check = scores_database.add_score(score)
    if check:
        return jsonify({"status": False})

    return jsonify({"status": True})


'''@auth.route("/users")
def get_users():
    return jsonify(storage_db.get_users())

@auth.route("/rooms")
def get_rooms():
    return jsonify(storage_db.get_rooms())

@auth.route("/register", methods=["POST"])
def create_user():
    user = request.form['user']
    password = request.form['password']
    password = generate_password_hash(password)
    return jsonify(storage_db.create_user(user, password))

@auth.route("/login", methods=["POST"])
def login():
    user = request.form['user']
    password = request.form['password']
    return jsonify(storage_db.authenticate(user, password))

@auth.route("/create_room", methods=["POST"])
def create_room():
    user = request.form['user']
    return jsonify(storage_db.create_room(user))

@auth.route("/join_room", methods=["POST"])
def join_room():
    room_id = request.form['id']
    user = request.form['user']
    return jsonify(storage_db.join_room(room_id, user))'''