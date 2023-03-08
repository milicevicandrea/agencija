from .user import UserSchemaResponse, UserSchemaRequest, UserSchemaMinimal, ChangeRoleSchema, AccountTypeSchema

user_schema_minimal = UserSchemaMinimal()
users_schema_minimal = UserSchemaMinimal(many=True)

user_schema_response = UserSchemaResponse()
users_schema_response = UserSchemaResponse(many=True)

user_schema_request = UserSchemaRequest()
users_schema_request = UserSchemaRequest(many=True)

change_role_schema = ChangeRoleSchema()
change_roles_schema = ChangeRoleSchema(many=True)

account_type_schema = AccountTypeSchema()
account_types_schema = AccountTypeSchema(many=True)
