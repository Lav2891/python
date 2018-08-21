# -*- coding: utf-8 -*-
import csv
# csv file name
filename = "Salary_Data.csv"
# initializing the titles and rows list
fields = []
rows = []
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
