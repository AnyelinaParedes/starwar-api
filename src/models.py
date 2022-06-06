from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    # def __repr__(self):
    #     return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(120), unique=False, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=True)
    eye_color = db.Column(db.String(120), unique=False, nullable=True)
    img = db.Column(db.String(250),unique=False, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "gender": self.gender,
            "height": self.height,
            "eye_color": self.eye_color,
            "img": self.img
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    terrain = db.Column(db.String(120), unique=False, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=True)
    img = db.Column(db.String(250),unique=False, nullable=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "terrain": self.terrain,
            "climate": self.climate,
            "img": self.img

        }

class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(120), unique=False, nullable=False)
    starship_class = db.Column(db.String(120), unique=False, nullable=True)
    passengers = db.Column(db.Integer, unique=False, nullable=True)
    img = db.Column(db.String(250),unique=False, nullable=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "model":self.model,
            "starship_class": self.starship_class,
            "passengers": self.passengers,
            "img": self.img

        }


# class FavoriteList(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
#     user = db.relationship(User)
#     people = db.relationship(People)

#     def serialize(self):
#         return {
#             "id": self.id,
#             "user_id":self.user_id,
#             "people_id":self.people_id,
            
            
#         }

class FavoriteList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    starships_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    people = db.relationship(People)
    planets = db.relationship(Planets)
    starships = db.relationship(Starships)
    user = db.relationship(User)

    def serialize(self):
        return {
            "id": self.id,
            "user_id":self.user_id,
            "people_id":self.people_id,
            "planets_id":self.planets_id,
            "starships_id": self.starships_id,
            
        }