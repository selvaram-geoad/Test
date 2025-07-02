from flask import Flask, jsonify
from flask_restful import Api
from dotenv import load_dotenv
from db import db
from endpoints.endpoints import endPoints_list
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:vs260210@localhost/dummy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
CORS(app)

def register_endpoint(api, resource, url):
    api.add_resource(resource, url)

for endpoint in endPoints_list:
    register_endpoint(api, endpoint["resource"], endpoint["url"])

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)



 