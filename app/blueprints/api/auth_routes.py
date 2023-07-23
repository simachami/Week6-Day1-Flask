from flask import request, jsonify
from flask_jwt_extended import create_access_token, unset_jwt_cookies
from . import bp as api
from app.models import User


@api.post('/signup')
def sign_up():
    content, response = request.json, {}
    print(content)
    if User.query.filter_by(email=content['email']).first():
      response['email error']=f'{content["email"]} is already taken/ Try again'
    if User.query.filter_by(username=content['username']).first():
      response['username error']=f'{content["username"]} is already taken/ Try again'
    if 'password' not in content:
       response['message'] = "Please include password"
    u = User()
    u.from_dict(content)
    try:
      u.hash_password(u.password)
      u.commit()
      return jsonify({'message': f'{u.username} is registered'}, 200)
    except:
      return jsonify(response),400
    
@api.post('/signin')
def sign_in():
    username, password = request.json.get('username'), request.json.get('password')
    u = User.query.filter_by(username=username).first()
    if u and u.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify({'access_token':access_token}), 200
    else:
        return jsonify({'message': 'Username or password is not valid. Please try again!'}), 400

@api.post('/logout')
def logout():
    response = jsonify({'message': 'Logout was successful'})
    unset_jwt_cookies(response)
    return response