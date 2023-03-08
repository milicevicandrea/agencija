# Create schema (marshmallow)
from marshmallow import (Schema, fields, post_load, validates_schema, ValidationError)


class UserSchemaMinimal(Schema):
    name = fields.String(required=False, allow_none=True)
    email = fields.Email(required=False, allow_none=True)


class AccountTypeSchema(Schema):
    id = fields.Integer(primary_key=True)
    account_type = fields.String(required=False, allow_none=True)


class UserSchemaResponse(UserSchemaMinimal):
    id = fields.Integer(primary_key=True)
    surname = fields.String(required=False, allow_none=True)
    username = fields.String(required=False, allow_none=True)
    password = fields.String(required=False, allow_none=True)
    password_again = fields.String(required=False, allow_none=True)
    account_type_rel = fields.Nested(AccountTypeSchema)


class UserSchemaRequest(UserSchemaMinimal):
    surname = fields.String()
    username = fields.String()
    password = fields.String()
    password_again = fields.String()
    account_type = fields.String()


class ChangeRoleSchema(Schema):
    id = fields.Integer(primary_key=True)
    user_rel = fields.Nested(UserSchemaMinimal)
    wanted_account_type = fields.String(required=False, allow_none=True)
    admin_rel = fields.Nested(UserSchemaMinimal)
    changed = fields.DateTime()

