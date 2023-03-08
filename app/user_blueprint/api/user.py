from app import app
from models import User, ChangeRoles, AccountType
from flask import jsonify, request
from app.auth import token
from app.user_blueprint.schemas import user_schema_response, users_schema_response, \
    user_schema_request, change_role_schema, change_roles_schema
from app.user_blueprint.services import Users


# Login (ADMIN, TRAVEL GUIDE, TOURIST)
@app.route('/login', methods=['GET', 'POST'])
def login_user():
    auth = request.authorization
    return Users().login(auth, User)


# Signup (NOT LOGGED IN)
@app.route('/signup/', methods=['POST'])
def signup():
    data = request.get_json()
    user = Users().new_user(data, User, ChangeRoles)
    return user_schema_response.dump(user)


# Get user details (ADMIN, TOURIST)
@app.route('/users/<id>/', methods = ['GET'])
@token.token_required(1, 3, '')
def get_user_details(current_user, id):
    result = Users.get_details(current_user, User, id=id)
    return user_schema_response.dump(result)


# Update user (TOURIST)
@app.route('/users/', methods=['PATCH'])
@token.token_required(3, '', '')
def update_user(current_user):
    data = request.get_json()
    result = Users().update_user(current_user, data, User)
    return user_schema_response.dump(result)


# Request role change (TRAVEL GUIDE, TOURIST)
@app.route('/change_role_requests/', methods=['POST'])
@token.token_required(2, 3, '')
def request_role_change(current_user):
    data = request.get_json()
    print(data)
    result = Users().request_change(current_user, User, ChangeRoles, data)
    return change_role_schema.dump(result)


# Get role change requests (ADMIN)
@app.route('/change_role_requests/', methods=['GET'])
@token.token_required(1, '', '')
def get_change_role_requests(current_user):
    role = Users.get_requests(ChangeRoles)
    return change_roles_schema.dump(role)


# Accept or deny change role request (ADMIN)
@app.route('/change_role_requests/<id>/', methods=['PATCH'])
@token.token_required(1, '', '')
def update_role(current_user, id):
    data = request.get_json()
    result = Users().update_roles(current_user, data, ChangeRoles, User, id)
    return user_schema_response.dump(result)


# Filter by user type (ADMIN)
@app.route('/users/type/<id>/', methods=['GET'])
@token.token_required(1, '', '')
def filter_by_type(current_user, id):
    users = Users.filter_by_type(AccountType, User, id)
    return users_schema_response.dump(users)













