from flask import Flask, request, jsonify
from flask_restful import Resource
from models.user import User, UserExperience
from db import db


class getUser(Resource):
    def get(self):
        response = []
        users = User.query.all()
        for user in users:
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'experiences': [{
                    'id': exp.id,
                    'experience': exp.experience
                } for exp in user.experiences]
            }
            response.append(user_data)
        return jsonify(response)
        

class createUser(Resource):
    def post(self):
        data = request.get_json()
        if not data or ('username' not in data) or ('email' not in data) or ('experience' not in data):
            return jsonify({'message' : "Cannot create user. Please provide a name, email-id and your experience"}, 400)
        new_user = User(username = data['username'], email = data['email'])
        db.session.add(new_user)
        db.session.commit()
        new_experience = UserExperience(user_id = new_user.id, experience = data['experience'])
        db.session.add(new_experience)
        db.session.commit()
        return jsonify({'message': "User added successfully"}, 201)

class updateUser(Resource):
    def put(self, user_id):
        user = User.query.get(user_id)
        experience = UserExperience.query.get(user.experiences[0].id)
        print(experience)

        data = request.get_json()
        if "username" in data:
            user.username = data["username"]

        if "email" in data:
            user.email = data["email"]
        
        if "experience" in data:
            experience.experience = data["experience"]

        db.session.commit()
        return jsonify({"message" : "Updated successfully!", "data": {"username" : user.username, "email" : user.email, "experience" : experience.experience}})

class deleteUser(Resource):
    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found or user does not exist"}, 404)
        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "User deleted successfully!"}, 200)  