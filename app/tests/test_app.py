# import unittest
# from unittest.mock import MagicMock
#
# import requests
# from requests.auth import HTTPBasicAuth
# from app.user_blueprint.api.user import login_user
# from models import User
# from flask import request
# import app.arrangement_blueprint.services.arrangement as service
# from app.arrangement_blueprint.services import Arrangement
# from models import Destination
#
# arrangement = Arrangement
#
# class TestAPI(unittest.TestCase):
#     URL = "http://127.0.0.1:5000/arrangements"
#     URL1 = "http://127.0.0.1:5000/login"
#     URL2 = "http://127.0.0.1:5000/users"
#     token_admin = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdWJsaWNfaWQiOiI3MWU0MWI2NS1mMzY4LTQ2ZjktYmU5Yy04MmE5MGEzN2M3NzkiLCJleHAiOjE2Nzc4NDA1MjN9.NVY4A5WpjujmrURS_tFJAd4smxbDSaA4LqoKi_yZHmk'
#     token_guide = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdWJsaWNfaWQiOiI0ZDQ3NThmOS1mZGJiLTQ0ZTgtOTAyNi1jNGE5YjJhNTcyNWIiLCJleHAiOjE2Nzc4NDA1NDh9.HMzx3fjG7xVTPAF-VrygtbAkOsEZhaqg041ZM06FcpM'
#     token_tourist = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdWJsaWNfaWQiOiI5YzZiOTg1Yy1lNWI4LTQyNWMtOGY4OS00Y2Y4NzlmMzkyODUiLCJleHAiOjE2Nzc4NDA0OTV9.4AP9Cu3g3uwLu6GflgqzidMY62eIE2mCq0u7H2xUMUo'
#
#     def test_1_get_all_arrangements(self):
#         resp = requests.get(self.URL)
#         self.assertEqual(resp.status_code, 200)
#         self.assertEqual(len(resp.json()), 15)
#         print("Test 1 completed.")
#
#     def test_2_get_one_arrangement(self):
#         resp = requests.get(self.URL+'/1', headers={'x-access-tokens': self.token_admin})
#         # login_token = requests.get(self.URL1, headers={'username': 'andjela', 'password': 'andjela'})
#         # login_token = requests.get(self.URL1,authorization={'username': 'andjela', 'password': 'andjela'})
#         # print(login_token)
#         # resp = requests.get(self.URL+'/1', headers={'x-access-tokens': str(login_token)})
#         self.assertEqual(resp.status_code, 200)
#         self.assertIn("created_by_rel", resp.json(), "Wrong search.")
#         print("Test 2 completed.")
#
#     def test_3_get_details_by_admin(self):
#         resp = requests.get(self.URL+'/created_by', headers={'x-access-tokens': self.token_admin})
#         self.assertEqual(resp.status_code, 200)
#         self.assertGreaterEqual(len(resp.json()), 1)
#         print("Test 3 completed.")
#
#     def test_4_get_details_by_guide(self):
#         resp = requests.get(self.URL+'/guided_by', headers={'x-access-tokens': self.token_guide})
#         self.assertEqual(resp.status_code, 200)
#         self.assertGreaterEqual(len(resp.json()), 1)
#         print("Test 4 completed.")
#
#     def test_5_get_arrangements_with_search(self):
#         resp = requests.get(self.URL+'/guided_by', headers={'x-access-tokens': self.token_tourist},\
#                             params={'starts': '2023-11-05'})
#         correctness = resp.status_code == 200 or resp.status_code == 404
#         self.assertTrue(correctness)
#         print("Test 5 completed.")
#
#     def test_6_get_reservations(self):
#         resp = requests.get(self.URL2+'/reservations', headers={'x-access-tokens': self.token_tourist})
#         correctness = resp.status_code == 200 or resp.status_code == 404
#         self.assertTrue(correctness)
#         print("Test 6 completed.")
#
#     def test_7_create_arrangement(self):
#         # resp = requests.post(self.URL, headers={'x-access-tokens': self.token_admin},\
#         #                      params={'starts': '2023-05-05',
#         #                              'ends': '2023-05-15',
#         #                              'description': 'opis',
#         #                              'destination': 'Lisabon',
#         #                              'number_of_people': 15,
#         #                              'price': 2000})
#         # self.assertEqual(resp.status_code, 200)
#         # self.assertGreaterEqual(len(resp.json()), 1)
#         # self.assertIn("starts", resp.json(), "Wrong search.")
#         #
#         # print("Test 7 completed.")
#         data = {'starts': '2023-05-05',
#                  'ends': '2023-05-15',
#                  'description': 'opis',
#                  'destination': 'Lisabon',
#                  'number_of_people': 15,
#                  'price': 2000}
#         current_user = MagicMock(id=17)
#         import pdb; pdb.set_trace()
#         result = arrangement.create_arrangement(data=data, table=MagicMock(), current_user=current_user)
#         assert result
#         print("Test 7 completed.")
#
#
# if __name__ == "__main__":
#     tester = TestAPI()
#
#     tester.test_1_get_all_arrangements()
#     tester.test_2_get_one_arrangement()
#     tester.test_3_get_details_by_admin()
#     tester.test_4_get_details_by_guide()
#     tester.test_5_get_arrangements_with_search()
#     tester.test_6_get_reservations()
#     tester.test_7_create_arrangement()
