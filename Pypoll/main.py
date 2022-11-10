import csv
import os
#path to collect datat from resources folder
csvpath = os.path.join("Resources","budget_data.csv")

#read csv file
with open(csvpath, 'r') as csvfile:
    