"""
Program: customer.py
Author: Bobby Parsons

Contains a class to store information about a customer, plus a driver to demonstrate the class
"""

class Customer:
    """Customer class"""

    def __init__(self, id, lname, fname, phone, addr):
        self.customer_id = int(id)
        self.last_name = str(lname)
        self.first_name = str(fname)
        self.phone_number = str(phone)
        self.address = str(addr)
    
    def __str__(self):
        output = "Customer #" + str(self.customer_id) + ":"
        output = output + self.first_name + " " + self.last_name + "\n"
        return output
    
    def __repr__(self):
        output = [str(self.customer_id), self.last_name, self.first_name, self.phone_number, self.address]
        return str(output)

    def display(self):
        output = "Customer #" + str(self.customer_id) + ":\n"
        output = output + self.first_name + " " + self.last_name + "\n"
        output = output + self.address + "\n"
        output = output + "Phone: " + self.phone_number + "\n"
        return output

customer1 = Customer(4646, "Parsons", "Robert", "(515) 151-5151", "1 Street Lane, Urbandale, IA")
print(customer1.display())

try: 
    customer2 = Customer("A113", "Parsons", "Robert", "(515) 151-5151", "1 Street Lane, Urbandale, IA")
except:
    pass
print(customer2.display())