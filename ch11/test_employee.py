import unittest
from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.test_employee = Employee('Michael', 'Shell', 50000)

    def test_give_default_raise(self):
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.pay, 55000)

    def test_give_custom_raise(self):
        self.test_employee.give_raise(10000)
        self.assertEqual(self.test_employee.pay, 60000)


if __name__ == '__main__':
    unittest.main()
