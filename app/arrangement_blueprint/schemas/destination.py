from marshmallow import (Schema, fields, post_load, ValidationError, validates, validates_schema)
from app.user_blueprint.schemas import UserSchemaMinimal


class ArrangementSchemaMinimal(Schema):
    starts = fields.Date()
    ends = fields.Date()
    destination = fields.String()

    @validates_schema()
    def validate_schema(self, data, many, **kwargs):
        if data['starts'] >= data['ends']:
            raise ValidationError("Start date can't be after end date.")


class ArrangementSchemaResponse(ArrangementSchemaMinimal):
    id = fields.Integer(primary_key=True)
    description = fields.String()
    number_of_people = fields.Integer()
    price = fields.Integer()
    guide_rel = fields.Nested(UserSchemaMinimal)
    created_by_rel = fields.Nested(UserSchemaMinimal)


class ArrangementSchemaRequest(ArrangementSchemaMinimal):
    description = fields.String()
    number_of_people = fields.Integer()
    price = fields.Integer()


class ReservationSchemaResponse(Schema):
    id = fields.Integer(primary_key=True)
    destination_rel = fields.Nested(ArrangementSchemaMinimal)
    price = fields.Integer()
    reserved_by_rel = fields.Nested(UserSchemaMinimal)



