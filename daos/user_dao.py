
def filter_by_id(table, id):
    return table.query.filter_by(id=id).first_or_404()


def get_all(table):
    return table.query.all()


def filter_by_account_type(table, wanted_type):
    return table.query.filter_by(account_type=wanted_type.id).all()


def filter_by_user_id(table, data):
    return table.query.filter_by(username=data['username']).first().id


def filter_by_username(table, auth):
    return table.query.filter_by(username=auth.username).first_or_404()
