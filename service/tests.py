import unittest

import requests

URL = 'http://localhost:5001/get_form'


class TestPositive(unittest.TestCase):

    def test_1_valid_full_match(self):

        data = {
            "username": "Admin",
            "phone": "+79997775533",
            "lead_email": "admin@admin.ru",
            "created_at": "2000-05-12"
        }

        response = requests.post(URL, json=data)
        self.assertEqual(response.status_code, 200)

        expected_data = 'User profile'
        self.assertEqual(response.text, expected_data)

    def test_2_valid_w_additional_field(self):

        data = {
            "customer": "Zavod",
            "username": "Admin",
            "phone": "+79997775533",
            "lead_email": "admin@admin.ru",
            "created_at": "2000-05-12",
            "updated_at": "2001-08-27",
        }

        response = requests.post(URL, json=data)
        self.assertEqual(response.status_code, 200)

        expected_data = 'User profile'
        self.assertEqual(response.text, expected_data)

    def test_3_valid_additional_fields(self):

        data = {
            "username": "John Doe",
            "company_name": "CleanHouse",
            "description": "cleaning service",
            "created_at": "23.09.2022"
            }

        response = requests.post(URL, json=data)
        self.assertEqual(response.status_code, 200)

        expected_data = 'Order'
        self.assertEqual(response.text, expected_data)

    def test_4_valid_full_matching(self):

        data = {
            "ticket": "21/03/2023-abc",
            "created_at": "21.03.2023"
            }

        response = requests.post(URL, json=data)
        self.assertEqual(response.status_code, 200)

        expected_data = 'Support ticket'
        self.assertEqual(response.text, expected_data)

    def test_5_valid_additional_fields(self):

        data = {
            "phone": "+79485849365",
            "lead_email": "hb13718@list.ru",
            "updated_at": "12.12.2021",
            "customer": "Zavod",
            "ticket": "30/11/2021-wfkfi",
            "created_at": "30.11.2021"
            }

        response = requests.post(URL, json=data)
        self.assertEqual(response.status_code, 200)

        expected_data = 'Support ticket'
        self.assertEqual(response.text, expected_data)


class TestNegative(unittest.TestCase):

    def test_1_invalid_empty_data(self):
        data = {}

        response = requests.post(URL, json=data)
        self.assertEqual(response.status_code, 200)

        expected_data = '{}'
        self.assertEqual(response.text, expected_data)

    def test_2_invalid_no_matching(self):

        data = {
            "username": "Admin",
            "phone": "+79485849365",
            "lead_email": "hb13718@list.ru",
            "updated_at": "12.12.2021",
            "customer": "Zavod",
            "ticket": "30/11/2021-wfkfi",
            "description": "fix service"
            }

        response = requests.post(URL, json=data)
        self.assertEqual(response.status_code, 200)

        expected_data = {
            "username": "text",
            "phone": "phone",
            "lead_email": "email",
            "updated_at": "date",
            "customer": "text",
            "ticket": "text",
            "description": "text"
            }
        self.assertEqual(response.json(), expected_data)

    def test_3_invalid_json_error(self):
        data = {
            "sos_phone": +79995557777,
            "sos_email": "sos@sos.support.com",
        }

        response = requests.post(URL, data=data)
        self.assertEqual(response.status_code, 200)

        expected_data = {'error': 'JSONDecodeError'}
        self.assertEqual(response.json(), expected_data)

    def test_4_invalid_not_post(self):

        response = requests.get(URL)
        self.assertEqual(response.status_code, 405)

        expected_data = {"error": "405 Method not allowed"}
        self.assertEqual(response.json(), expected_data)


if __name__ == '__main__':
    unittest.main()
