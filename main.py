import os
import csv
# csvpath = "os.path.join('..','PyBank','raw_data','budget_data_1.csv')
filepath = "C:\\Users\\Anish Tendolkar\\datasciencebootcamp\\python_challenge\\Zip\\PyBank\\raw_data\\budget_data_1.csv"
Months = 0
Total_Revenue = 0
with open(filepath) as csvfile:
    reader = csv.reader(csvfile)
    # for row in reader:
    #     print(row)
    next(reader,None)
    data = list(reader)
    Months = len(data)
    for row in data:
        cur_month = int(row[1])
        Total_Revenue += int(row[1])
        #The average change in revenue between months over the entire period



    print("Months: " , Months)
    print("Total_Revenue: " , Total_Revenue)


            # Total_Revenue = Total_Revenue + int(row[1])
