from .destination import ArrangementSchemaResponse, ArrangementSchemaRequest, ReservationSchemaResponse

arrangement_schema_response = ArrangementSchemaResponse()  #TODO koristi _ i bez velikih slova, prebaci inicijalizacij u api
arrangements_schema_response = ArrangementSchemaResponse(many=True)

arrangement_schema_request = ArrangementSchemaRequest()
arrangements_schema_request = ArrangementSchemaRequest(many=True)

reservation_schema_response = ReservationSchemaResponse()
reservations_schema_response = ReservationSchemaResponse(many=True)

