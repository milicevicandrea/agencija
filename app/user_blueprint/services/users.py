from flask import jsonify, make_response
from app import app, db
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import datetime
import jwt
from marshmallow import ValidationError
from app.user_blueprint.schemas import user_schema_request
from models import User
from daos import user_dao


class Users():
    def __init__(self, mock_db=None):
        self.db = db if not mock_db else mock_db

    @staticmethod
    def get_details(current_user, table, id):
        if current_user.account_type == 1:
            user = user_dao.filter_by_id(table, id)
        else:
            user = user_dao.filter_by_id(current_user, id)
        return user

    @staticmethod
    def get_requests(table):
        """Get all requests for role change"""
        return user_dao.get_all(table)

    @staticmethod
    def filter_by_type(table1, table2, id):
        wanted_type = user_dao.filter_by_id(table1, id)
        return user_dao.filter_by_account_type(table2, wanted_type)

    def new_user(self, data, table1, table2):
        """Create new user in User table and return it"""
        if data['password'] != data['password_again']:
            raise ValidationError("Password must be unique.")
        del data['password_again']
        result = user_schema_request.load(data)
        user = table1(**result)
        user.public_id = str(uuid.uuid4())
        user.password = generate_password_hash(data['password'], method='sha256')
        user.account_type = 3
        self.db.session.add(user)
        self.db.session.commit()
        if data['account_type'] != 'Tourist':
            req = table2(
                user_id=user_dao.filter_by_user_id(User, data),
                wanted_account_type=data['account_type']
            )
            self.db.session.add(req)
            self.db.session.commit()

        return user

    def login(self, auth, table):
        if not auth or not auth.username or not auth.password:
            return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})
        user = user_dao.filter_by_username(table, auth)
        if self.db == db:
            if check_password_hash(user.password, auth.password):
                token = jwt.encode(
                    {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=130)},
                    app.config['SECRET_KEY'])
                return jsonify({'token': token})
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

    def request_change(self, current_user, table1, table2, data):
        """Make a request for role change and return that request"""
        if not 'account_type' in data:
            raise ValidationError("Required information are missing.")
        user = user_dao.filter_by_username(table1, current_user)
        req = table2(
            user_id=user.id,
            wanted_account_type=data['account_type']
        )
        self.db.session.add(req)
        self.db.session.commit()
        return req

    def make_a_reservation(self, current_user, data, table1, table2, id):
        dest = user_dao.filter_by_id(table1, id)
        price = dest.price * 3
        if data['number_of_people'] > 3:
            for i in range(3, data['number_of_people'] + 1):
                price = price + dest.price * 0.9
        else:
            price = data['number_of_people'] * dest.price

        res = table2(
            destination_id=dest.id,
            price=price,
            reserved_by=current_user.id
        )
        self.db.session.add(res)
        dest.number_of_people = dest.number_of_people - data['number_of_people']
        self.db.session.commit()
        return res

    def update_roles(self, current_user, data, table1, table2, id):
        """Admin decides if the role change request will be accepted or not;
        returns user with the new/old account type"""
        role = user_dao.filter_by_id(table1, id)
        user = user_dao.filter_by_id(table2, role.user_id)
        if 'accept' not in data or 'accept' == 'No':
            role.admin = current_user.id
            self.db.session.commit()
            return jsonify({
                'email': data['comment']
            }), 400
        else:
            if role.wanted_account_type == 'Admin':
                user.account_type = 1
            else:
                if role.wanted_account_type == 'Travel Guide':
                    user.account_type = 2
            role.admin = current_user.id
            role.changed = datetime.datetime.utcnow()
            self.db.session.commit()
        return user

    def update_user(self, current_user, data, table):
        user = user_dao.filter_by_id(table, current_user.id)
        if 'name' in data:
            user.name = data['name']
        if 'surname' in data:
            user.surname = data['surname']
        if 'email' in data:
            user.email = data['email']
        if 'username' in data:
            user.username = data['username']
        if 'password' in data:
            user.password = data['password']
        if 'password_again' in data:
            user.password_again = data['password_again']
        if 'account_type' in data:
            user.account_type = data['account_type']

        self.db.session.commit()
        return user




