import jwt
from functools import wraps
from flask import jsonify, request
from models import User
from app import app
from models import AccountType


# TOKEN new comment
def token_required(wanted_role1, wanted_role2, wanted_role3):
    def decorator_1(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            token = None
            if 'x-access-tokens' in request.headers:
                token = request.headers['x-access-tokens']

            if not token:
                return jsonify({'message': 'A valid token is missing.'})

            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], 'HS256')
                current_user = User.query.filter_by(public_id=data['public_id']).first()
                if current_user.account_type != int(wanted_role1) and current_user.account_type != int(wanted_role2) and current_user.account_type != int(wanted_role3):
                    return jsonify({'message': 'You do not have roles for this action!'})
            except:
                return jsonify({'message': 'Token is invalid.'})

            return f(current_user, *args, **kwargs)

        return decorator

    return decorator_1
