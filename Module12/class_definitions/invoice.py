"""
Program: invoice.py
Author: Bobby Parsons

Contains a class to store information about an invoice, plus a driver to demonstrate the class
"""
class Invoice:
    def __init__(self, invoice_id, customer_id, lname, fname, phone, addr, items={}):
        self.invoice_id = int(invoice_id)
        self.customer_id = int(customer_id)
        self.last_name = str(lname)
        self.first_name = str(fname)
        self.phone_number = str(phone)
        self.address = str(addr)
        self.items_with_price = items

    def __str__(self):
        output = "Customer #" + str(self.customer_id) + ":"
        output = output + self.first_name + " " + self.last_name + "\n"
        return output
    
    def __repr__(self):
        output = [str(self.customer_id), self.last_name, self.first_name, self.phone_number, self.address]
        return str(output)

    def add_item(self, item_to_add):
        self.items_with_price.update(item_to_add)

    def create_invoice(self):
        SALES_TAX = 0.06
        subtotal = 0
        for item in self.items_with_price:
            print(item + ".....$" + str(self.items_with_price[item]))
            subtotal = subtotal + self.items_with_price[item]
        tax = subtotal * SALES_TAX
        total = tax + subtotal
        print("Tax.........$" + '%.2f' % tax)
        print("Total.......$" + '%.2f' % total)


# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()