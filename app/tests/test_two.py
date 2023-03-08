import random
from unittest import TestCase, mock
from unittest.mock import MagicMock

from app.arrangement_blueprint.services.arrangement import Arrangement
from app.user_blueprint.services.users import Users
from app.user_blueprint.schemas.user import UserSchemaResponse


class TestTwo(TestCase):
    id = random.randint(1, 25)

    def test_create_arrangement(self):
        data ={
                "starts": "2023-05-25",
                "ends": "2023-05-15",
                "description": "opis",
                "destination": "Moskva",
                "number_of_people": 15,
                "price": 800
                }
        test = Arrangement(MagicMock()).create_arrangement(MagicMock(), data, MagicMock())
        assert test
        self.assertEqual(test.guide, None)
        self.assertIsNot(test.created_by, None)
        self.assertIsNot(test.starts, None)
        self.assertIsNot(test.ends, None)
        self.assertIsNot(test.description, None)
        self.assertIsNot(test.destination, None)
        self.assertIsNot(test.number_of_people, None)
        self.assertIsNot(test.price, None)

    def test_update_arrangement(self):
        test = Arrangement(MagicMock()).update_arrangement(MagicMock(), {}, MagicMock(), self.id)
        assert test
        self.assertIsNot(test.created_by, None)

    def test_get_all_arrangements(self):
        test = Arrangement.get_all_arrangements(MagicMock())
        assert test
        #self.assertEqual(test.starts, None)

    def test_get_arrangement_details(self):
        test = Arrangement.get_arrangement_details(MagicMock(), MagicMock(), self.id)
        assert test

    def test_get_arrangements_by_guide(self):
        test = Arrangement.get_arrangements_by_guide(MagicMock(), MagicMock())
        assert test

    def test_get_arrangements_by_admin(self):
        test = Arrangement.get_arrangements_by_admin(MagicMock(), MagicMock())
        assert test

    def test_get_reservations(self):
        test = Arrangement.get_reservations(MagicMock(), MagicMock())
        assert test

    def test_search(self):
        test = Arrangement.search({}, MagicMock(), MagicMock(), MagicMock())
        assert test

    def test_guide(self):
        test = Arrangement(MagicMock()).guide(MagicMock(), {}, MagicMock(), MagicMock(), self.id)
        assert test

    def test_delete_arrangement(self):
        test = Arrangement(MagicMock()).delete_arrangement(MagicMock(), MagicMock(), self.id)
        assert test

    def test_get_details(self):
        test = Users.get_details(MagicMock(), MagicMock(), self.id)
        assert test

    def test_get_requests(self):
        test = Users.get_requests(MagicMock())
        assert test

    def test_filter_by_type(self):
        test = Users.filter_by_type(MagicMock(), MagicMock(), self.id)
        assert test

    def test_new_user(self):
        data = {"name": "ivana",
                "surname": "ivanovic",
                "email": "ivana@yahoo.com",
                "username": "ivana",
                "password": "ivana",
                "password_again": "ivana",
                "account_type": "Tourist"
                }
        test = Users(MagicMock()).new_user(data, MagicMock(), MagicMock())
        self.assertIsNot(test.name, None)
        self.assertIsNot(test.surname, None)
        self.assertIsNot(test.email, None)
        self.assertIsNot(test.username, None)
        self.assertIsNot(test.password, None)
        self.assertIsNot(test.account_type, None)
        self.assertEqual(test.account_type, 3)
        assert test

    def test_request_change(self):
        data = {"account_type": "Travel Guide"}
        test = Users(MagicMock()).request_change(MagicMock(), MagicMock(), MagicMock(), data)
        self.assertIsNot(test.user_id, None)
        assert test

    def test_make_a_reservation(self):
        data = {'number_of_people': 4}
        test = Users(MagicMock()).make_a_reservation(MagicMock(), data, MagicMock(), MagicMock(), self.id)
        assert test

    def test_update_roles(self):
        data = {'accept': 'No', 'comment': 'I do not want.'}
        test = Users(MagicMock()).update_roles(MagicMock(), data, MagicMock(), MagicMock(), self.id)
        assert test

    def test_update_user(self):
        test = Users(MagicMock()).update_user(MagicMock(), {}, MagicMock())
        assert test

    # @mock.patch('werkzeug.security.check_password_hash', create=True)
    # def test_login(self, mock_hash):
    #     mock_hash().return_value = True
    #     auth = UserSchemaResponse()
    #     auth.username = 'andjela'
    #     auth.password = '$andjela$'
    #     test = Users.login(auth, MagicMock())
    #     assert test

    def test_login(self):
        test = Users(MagicMock()).login(MagicMock(), MagicMock())
        assert test

