"""
Program: csvParser.py
Author: Bobby Parsons

Parses a CSV file of the populations of every county in Iowa and adds them up to get the state population
"""

import csv

class CountyDemos:

    def __init__(self, per_cap_income, med_house_income, med_fam_income, population, num_households):
        self.per_cap_income = per_cap_income
        self.med_house_income = med_house_income
        self.med_fam_income = med_fam_income
        self.population = population
        self.num_households = num_households


with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # initialize empty dictionary
    county={}
    for row in csv_reader:
        # skip the first line in the file because it is the header
        if line_count == 0:
            line_count += 1
            continue
        # create an item in dictionary county with a key of the county name and a value of the object
        if not (str(row[1]) == 'United States' or str(row[1]) == 'Iowa State'):
            county[str(row[1])] = CountyDemos(row[2],row[3],row[4],row[5],row[6])
        
        

print("Dallas County population: " + county['Dallas'].population)

pop_sum = 0
for key in county:
    pop_sum += int(county[key].population.replace(',',''))
print("Iowa population: " + str(pop_sum))