import datetime
from datetime import date, datetime
from flask import jsonify
from sqlalchemy import or_
from werkzeug.exceptions import Conflict, BadRequest
from app import app, db
from marshmallow import ValidationError
from daos import arrangement_dao


class Arrangement:
    def __init__(self, mock_db=None):
        self.db = db if not mock_db else mock_db

    @staticmethod
    def get_all_arrangements(table):
        return arrangement_dao.get_all(table)

    @staticmethod
    def get_arrangement_details(current_user, table, id):
        return arrangement_dao.filter_by_id(table, id)

    @staticmethod
    def get_arrangements_by_guide(current_user, table):
        return arrangement_dao.filter_by_guide(table, current_user)

    @staticmethod
    def get_arrangements_by_admin(current_user, table):
        return arrangement_dao.filter_by_admin(table, current_user)

    @staticmethod
    def get_reservations(current_user, table):
        return arrangement_dao.filter_by_reservation(table, current_user)

    # @staticmethod
    # def get_arrangement_details(current_user, filter, table):
    #     if not table.query.filter_by(**filter).all():
    #         raise ValidationError("Wrong" + str(filter) + ".")
    #     else:
    #         return table.query.filter_by(**filter).all()

    def create_arrangement(self, current_user, data, table):
        """Creates new arrangement in the Destination table and returns it"""
        dest = table(**data)
        dest.created_by = current_user.id
        dest.guide = None
        self.db.session.add(dest)
        self.db.session.commit()
        return dest

    def update_arrangement(self, current_user, data, table, id):
        dest = arrangement_dao.filter_by_id(table, id)
        if self.db == db:
            if (dest.starts - date.today()).days < 5:
                raise Conflict("Too late to change.")

        if 'starts' in data:
            dest.starts = data['starts']
        if 'ends' in data:
            dest.ends = data['ends']
        if 'description' in data:
            dest.description = data['description']
        if 'destination' in data:
            dest.destination = data['destination']
        if 'number_of_people' in data:
            dest.number_of_people = data['number_of_people']
        if 'price' in data:
            dest.price = data['price']

        self.db.session.commit()
        return dest

    def guide(self, current_user, data, table1, table2, id):
        """Gives tourist guide to the destination specified by id and returns whole arrangement"""
        dest = arrangement_dao.filter_by_id(table1, id)
        if 'guide' in data:
            guide = arrangement_dao.filter_by_id(table2, data['guide'])
            if arrangement_dao.filter_by_id(table2, guide).account_type != 2:
                raise ValidationError("There is no guide with id " + str(data['guide']) + ".")
            else:
                dest.guide = guide
                self.db.session.commit()
        return dest

    def delete_arrangement(self, current_user, table, id):
        dest = arrangement_dao.filter_by_id(table, id)
        if self.db == db:
            if (dest.starts - date.today()).days < 5:
                raise Conflict("Too late to change.")
        self.db.session.delete(dest)
        self.db.session.commit()
        return jsonify({
            'success': 'Data deleted successfully'
        }), 204

    @staticmethod
    def search(data, current_user, table1, table2):
        """Provides search by destination or starting date and returns all
        matching arrangements"""
        if 'starts' in data and (datetime.strptime(data['starts'], '%Y-%m-%d').date() - date.today()).days < 5:
            raise BadRequest("There are no available arrangements for searched date.")
        putovanja = table1.query.outerjoin(table2, table1.id == table2.destination_id).filter(or_(table2.id.is_(None),table2.reserved_by != current_user.id))

        if 'destination' in data:
            putovanja = putovanja.filter(table1.destination == data['destination'])

        if 'starts' in data:
            putovanja = putovanja.filter(table1.starts == data['starts'])

        return putovanja.all()


