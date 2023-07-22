from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


class User(UserMixin,db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    username = db.Column(db.String(100), nullable = False, unique = True)
    email = db.Column(db.String(180), nullable = False, unique = True)
    password_hash = db.Column(db.String(), nullable = False)
    recipes = db.relationship('Recipe', backref = 'author', lazy=True)


    def __repr__(self):
        return f'<User: {self.username}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def from_dict(self, user_obj):
        for attribute, value in user_obj.items():
            setattr(self, attribute, value)

    def get_id(self):
        return str(self.user_id)

    def hash_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)
    
class Recipe(db.Model):
    recipe_id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(), nullable = False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable= False)

    def __repr__(self):
        return f'<Recipe: {self.body}>'
    

    def commit(self):
        db.session.add(self)
        db.session.commit()