import unittest
from class_definitions import customer
from custom_exceptions import customer_exceptions


class ExceptionTests(unittest.TestCase):
    def setUp(self):
        self.customer1 = customer.Customer(4646, "Parsons", "Robert", "515-151-5151")

    def tearDown(self):
        del self.customer1

    def test_id_valid(self):
        self.assertEquals(self.customer1.customer_id, 4646)

    def test_first_name_valid(self):
        self.assertEquals(self.customer1.first_name, "Robert")
        
    def test_last_name_valid(self):
        self.assertEquals(self.customer1.last_name, "Parsons")
    
    def test_phone_valid(self):
        self.assertEquals(self.customer1.phone_number, "515-151-5151")
    
    def test_id_out_of_range(self):
        with self.assertRaises(customer_exceptions.InvalidCustomerIdException):
            customer.Customer(46464, "Parsons", "Robert", "515-151-5151")

    def test_invalid_first_name(self):
        with self.assertRaises(customer_exceptions.InvalidNameException):
            customer.Customer(4646, "Parsons", "80884", "515-151-5151")

    def test_invalid_last_name(self):
        with self.assertRaises(customer_exceptions.InvalidNameException):
            customer.Customer(4646, "Parson$", "Robert", "515-151-5151")

    def test_invalid_phone(self):
        with self.assertRaises(customer_exceptions.InvalidPhoneNumberFormat):
            customer.Customer(4646, "Parsons", "Robert", "(515) 151-5151")

    def test_customer_str(self):
        self.assertEqual(str(self.customer1), 'Customer #4646: Robert Parsons')

if __name__ == '__main__':
    unittest.main()