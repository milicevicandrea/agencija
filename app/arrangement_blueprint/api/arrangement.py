from app import app
from models import Destination, Reservation, User
from flask import jsonify, request
from app.arrangement_blueprint.schemas import arrangement_schema_response, arrangements_schema_response, arrangement_schema_request, arrangements_schema_request, reservation_schema_response, reservations_schema_response
from app.auth import token
from app.arrangement_blueprint.services import Arrangement
from app.user_blueprint.services import Users


# See all arrangements  (ALL)
@app.route('/arrangements', methods=['GET'])
def get_arrangements():
    result = Arrangement.get_all_arrangements(Destination)
    if len(result) != 0:
        return arrangements_schema_response.dump(result)
    else:
        return {
            'error': 'Bad Request'
        }, 404


# Create new arrangement (ADMIN)
@app.route('/arrangements/', methods=['POST'])
@token.token_required(1, '', '')
def create_arrangement(current_user):
    data = arrangement_schema_request.load(request.get_json())
    dest = Arrangement().create_arrangement(current_user, data, Destination)
    return arrangement_schema_response.dump(dest)


# Update arrangement (ADMIN, TRAVEL GUIDE)
@app.route('/arrangements/<id>/', methods=['PATCH'])
@token.token_required(1, 2, '')
def update_arrangement(current_user, id):
    data = request.get_json()
    result = Arrangement.update_arrangement(current_user, data, Destination, id)
    return arrangement_schema_response.dump(result)


# Delete arrangement (ADMIN)
@app.route('/arrangements/<id>/', methods=['DELETE'])
@token.token_required(1, '', '')
def delete_arrangement(current_user, id):
    return Arrangement().delete_arrangement(current_user=current_user, table=Destination, id=id)


# Get arrangement details (ADMIN)
@app.route('/arrangements/<id>/', methods=['GET'])
@token.token_required(1, '', '')
def get_arrangement_details(current_user, id):
    result = Arrangement.get_arrangement_details(current_user, Destination, id)
    return arrangement_schema_response.dump(result)


# Give guide (ADMIN)
@app.route('/arrangements/guide/<id>/', methods=['PATCH'])
@token.token_required(1, '', '')
def guide(current_user, id):
    data = request.get_json()
    result = Arrangement.guide(current_user, data, Destination, User, id)
    return result


# Get arrangement details by specific admin (ADMIN)
@app.route('/arrangements/created_by', methods=['GET'])
@token.token_required(1, '', '')
def get_arrangement_details_by_admin(current_user):
    result = Arrangement.get_arrangements_by_admin(current_user, Destination)
    if len(result) != 0:
        return arrangements_schema_response.dump(result)
    else:
        return {
            'error': 'Bad Request'
        }, 404


# Get arrangements by specific travel guide (Travel Guide)
@app.route('/arrangements/guided_by', methods=['GET'])
@token.token_required(2, '', '')
def get_arrangement_details_by_guide(current_user):
    result = Arrangement.get_arrangements_by_guide(current_user, Destination)
    if len(result) != 0:
        return arrangements_schema_response.dump(result)
    else:
        return {
            'error': 'Bad Request'
        }, 404


# Get arrangements with search (TOURIST)
@app.route('/arrangements/search', methods=['GET'])
@token.token_required(3, '', '')
def get_arrangement_search(current_user):
    data = request.get_json()
    result = Arrangement.search(data, current_user, Destination, Reservation)
    if len(result) != 0:
        return arrangements_schema_response.dump(result)
    else:
        return {
            'error': 'Bad Request'
        }, 404


# Get reservations (TOURIST)
@app.route('/users/reservations', methods=['GET'])
@token.token_required(3, '', '')
def see_reservations(current_user):
    result = Arrangement.get_reservations(current_user, Reservation)
    if len(result) != 0:
        return reservations_schema_response.dump(result)
    else:
        return {
            'error': 'Bad Request'
        }, 404


# Reservations (TOURIST)
@app.route('/user/<id>/reservations', methods=['POST'])
@token.token_required(3, '', '')
def make_a_reservation(current_user, id):
    data = request.get_json()
    result = Users().make_a_reservation(current_user, data, Destination, Reservation, id)
    return reservation_schema_response.dump(result)





