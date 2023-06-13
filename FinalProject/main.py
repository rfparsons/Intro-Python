"""
Program: main.py
Author: Bobby Parsons

Program that creates a full BOM from a list of parts provided by the user 
"""
import csv
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from tkinter import ttk
from supplier_library import suppliers

input_file_path = ''

def identify_supplier(part_number=''):
    prefix = part_number.split('-')[0]
    if prefix == 'am':
        return 'am'
    elif prefix == 'rev':
        return 'rev'
    else:
        return None

def pick_input_file():
    global input_file_path
    input_file_path = tkinter.filedialog.askopenfilename(filetypes=[("CSV file", ("*.csv"))], defaultextension='.csv')
    file_path_label.config(text="File path: " + input_file_path)


def main(input_file):
    # initialize empty array
    parts=[]
    # Store data in an array of dictionaries
    # {'supplier' : 'REV Robotics', 'part_name' : 'NEO Motor', 'part_no': 'rev-21-1650', 'quantity' : 2, 'price' : 40.0, 'total' : '=D1 * E1'}
    try:
        with open(input_file, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            line = 0
            total_lines = sum(1 for row in csv_reader) # only way to do this for some reason according to stuff online
            error_log = ''

            csv_file.seek(0) # Reset to beginning of file since I already iterated to get the total lines

            for row in csv_reader:
                part_number = row[0].lower()
                part_quantity = int(row[1])
                supplier_id = identify_supplier(part_number)
                supplier = ''
                progress_pct = (line + 1) / total_lines

                try:
                    line = line + 1
                    if supplier_id == 'am':
                        part = suppliers.andymark_item(part_number)
                        supplier = 'AndyMark'
                    elif supplier_id == 'rev':
                        part = suppliers.rev_item(part_number)
                        supplier = 'REV Robotics'
                    else:
                        error_log = error_log + 'Error: Could not identify supplier on line ' + str(line) + ' (' + part_number + ')\n'
                        continue

                    part_price = part.get_price()
                    if not hardcode_total.get():
                        total_str = '=(D' + str(line + 1) + ' * E' + str(line + 1) + ')'
                    else:
                        total_str = str(part_quantity * part_price)

                    parts.append({'supplier' : supplier,
                    'part_name' : part.get_name(), 
                    'part_no': part_number, 
                    'quantity' : part_quantity, 
                    'price' : part_price,
                    'total' : total_str})

                except suppliers.ItemNotFoundException:
                    error_log = error_log + 'Could not find item on line ' + str(line) + ' (' + part_number + '). Maybe a price isn\'t available on the page?'
                
                progress['value'] = progress_pct * 100
                m.update_idletasks()


        output_file = tkinter.filedialog.asksaveasfilename(filetypes=[("CSV file", ("*.csv"))], defaultextension='.csv')
        with open(output_file, mode='w', newline='') as csv_file:
            fieldnames = ['supplier', 'part_name', 'part_no', 'quantity', 'price', 'total']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for part in parts:
                writer.writerow(part)

            if error_log != '':
                tkinter.messagebox.showerror("Error", message="Errors in file:\n" + error_log)
            tkinter.messagebox.showinfo(message="Finished processing!\nYour file is at:\n" + output_file)
    except FileNotFoundError:
        tkinter.messagebox.showerror("Error", message="File not found.")

m = tkinter.Tk() # where m is the name of the main window object
m.title('FRC BOM Generator')

pick_file = tkinter.Button(m, text='Select Input File', width=25, command=pick_input_file)
pick_file.grid(row=1)

file_path_label = tkinter.Label(m, text="File path:")
file_path_label.config(text="File path:")
file_path_label.grid(row=2)

hardcode_total = tkinter.BooleanVar()
hardcode_total_check = tkinter.Checkbutton(m, text="Hardcode total column?", variable=hardcode_total)#, command=lambda: print(hardcode_total.get()))
hardcode_total_check.grid(row=3)

start_button = tkinter.Button(m, text='Start!', width=25, command=lambda: main(input_file_path))
start_button.grid(row=4)

progress = ttk.Progressbar(m, length=150, mode='determinate')
progress.grid(row=5)
#progress['value'] = 50

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)

m.mainloop()