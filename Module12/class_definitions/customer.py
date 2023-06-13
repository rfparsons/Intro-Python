"""
Program: customer.py
Author: Bobby Parsons

Contains a class to store information about a customer, plus a driver to demonstrate the class
"""
from custom_exceptions import customer_exceptions
import re


class Customer:
    """Customer class"""

    def __init__(self, id, lname, fname, phone):#, addr):
        if 1000 <= int(id) <= 9999:
            self.customer_id = int(id)
        else:
            raise customer_exceptions.InvalidCustomerIdException

        if str(lname).isalpha():
            self.last_name = str(lname)
        else:
            raise customer_exceptions.InvalidNameException

        if str(fname).isalpha():
            self.first_name = str(fname)
        else:
            raise customer_exceptions.InvalidNameException

        if re.match(r"\d{3}-\d{3}-\d{4}$", phone): #regular expression modified from http://regexlib.com/REDetails.aspx?regexp_id=22
            self.phone_number = str(phone)
        else:
            raise customer_exceptions.InvalidPhoneNumberFormat

        #self.address = str(addr)
    
    def __str__(self):
        output = "Customer #" + str(self.customer_id) + ": "
        output = output + self.first_name + " " + self.last_name
        return output
    
    def __repr__(self):
        output = [str(self.customer_id), self.last_name, self.first_name, self.phone_number]#, self.address]
        return str(output)


    def display(self):
        output = "Customer #" + str(self.customer_id) + ":\n"
        output = output + self.first_name + " " + self.last_name + "\n"
        #output = output + self.address + "\n"
        output = output + "Phone: " + self.phone_number + "\n"
        return output

if __name__ == "__main__":
    customer1 = Customer(4646, "Parsons", "Robert", "515-151-5151")#, "1 Street Lane, Urbandale, IA")
    print(customer1.display())

    # try: 
    #     customer2 = Customer("A113", "Parsons", "Robert", "(515) 151-5151", "1 Street Lane, Urbandale, IA")
    # except:
    #     pass
    # print(customer2.display())
