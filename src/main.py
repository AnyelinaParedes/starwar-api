"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, FavoriteList, Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_user():
    Users = User.query.all()
    Users = list(map(lambda x: x.serialize(),Users))
    return jsonify(Users)


@app.route('/people', methods=['GET'])
def get_people():
    Peoples = People.query.all()
    Peoples = list(map(lambda x: x.serialize(),Peoples))
    return jsonify(Peoples)

@app.route('/people/<int:id>', methods=['GET'])
def people_id(id):
    People_id = People.query.get(id)
    return jsonify(People_id.serialize())

@app.route('/planets', methods=['GET'])
def get_planets():
    Planets_all = Planets.query.all()
    Planets_all = list(map(lambda x: x.serialize(),Planets_all))
    return jsonify(Planets_all)

@app.route('/planets/<int:id>', methods=['GET'])
def planets_id(id):
    Planets_id = Planets.query.get(id)
    return jsonify(Planets_id.serialize())

@app.route('/favorite', methods=['GET'])
def get_favorite():
    Favorites = FavoriteList.query.all()
    Favorites = list(map(lambda x: x.serialize(),Favorites))
    return jsonify(Favorites)

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
