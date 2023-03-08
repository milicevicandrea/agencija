
def get_all(table):
    return table.query.all()


def filter_by_id(table, id):
    return table.query.filter_by(id=id).first_or_404()


def filter_by_guide(table, current_user):
    return table.query.filter_by(guide=current_user.id).all()


def filter_by_admin(table, current_user):
    return table.query.filter_by(created_by=current_user.id).all()


def filter_by_reservation(table, current_user):
    return table.query.filter_by(reserved_by=current_user.id).all()



