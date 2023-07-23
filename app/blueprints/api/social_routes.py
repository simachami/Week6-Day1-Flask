from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from . import bp as api
from app.models import Recipe, User

@api.post('/publish-recipe')
@jwt_required()
def publish_recipe():
    body = request.json.get('body')
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    try:
        r = Recipe(body=body, user_id = user.user_id)
        r.commit()
    except:
        jsonify(message='ERROR! Please try again!'), 404
    return jsonify({'message': 'recipe successfully published', 'logged_in_as': username}), 200


@api.get('/user-recipes/<username>')
@jwt_required()
def get_user_recipes(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'message': 'Username is invalid'}), 400
    user_recipes = user.recipes
    return jsonify({
      'message':'success',
      'posts': [{ 'body':post.body, 'timestamp':post.timestamp} for post in user_recipes ]
   })