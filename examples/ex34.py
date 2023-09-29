import requests
import unittest


class TestEmployeeApi(unittest.TestCase):

    def setUp(self) -> None:
        self.url = 'http://localhost:1234/api/employees'

    def test_get_existing_employee(self):
        response = requests.get(f'{self.url}/121')
        self.assertEqual(200, response.status_code)

    def test_get_non_existing_employee(self):
        response = requests.get(f'{self.url}/100')
        self.assertEqual(404, response.status_code)

    def test_get_employee_data(self):
        response = requests.get(f'{self.url}/121')
        actual = response.json()
        expected = dict(id=121, name='John Scott', salary=23000, department='admin')
        self.assertEqual(expected, actual)

    def test_add_new_emp(self):
        new_emp = dict(id=200, name='Mahesh Kumar', salary=20300, department='admin')
        response = requests.post(self.url, json=new_emp)
        self.assertEqual(201, response.status_code)

    def test_add_new_emp_with_existing_id(self):
        new_emp = dict(id=121, name='John Scott', salary=23000, department='admin')
        response = requests.post(self.url, json=new_emp)
        self.assertEqual(400, response.status_code)