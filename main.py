import os
import csv
# csvpath = "os.path.join('..','PyBank','raw_data','budget_data_1.csv')
#filepath = "C:\\Users\\Anish Tendolkar\\datasciencebootcamp\\python_challenge\\Zip\\PyBank\\raw_data\\budget_data_1.csv"
#filepath = "C:\\Users\\Anish Tendolkar\\datasciencebootcamp\\python_challenge\\Zip\\PyBank\\raw_data\\budget_data_1.csv"
#IF YOU UNCOMMENT THE LINE ABOVE THE DATA BELOW WILL RUN THROUGH BOTH THE CSV FILES AND RETURN NUMBERS BASED ON BOTH THE CSV FILES.
#txtpath = os.path.join("Zip","PyParagraph","raw_data","paragraph_1.txt")
filepath = os.path.join("Zip","PyBank","raw_data","budget_data_1.csv")
filepaths = os.path.join("Zip","PyBank","raw_data","budget_data_2.csv")
Months = 0
Total_Revenue = 0
change = 0
prev_revenue = 0
greatest_increase = 0
greatest_decrease = 9999999999999999999999
idate = ""
ddate = ""
revenue_changes = []
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
        #change = change
        #prev_revenue = prev_revenue
        change = int(row[1]) - prev_revenue
        # print(change)
        #date = int(row[0])
        # Reset the value of prev_revenue to the row I completed my analysis
        prev_revenue = int(row[1])
        # print(prev_revenue)

        # #Determine the greatest increase
        if (change > greatest_increase):
            greatest_increase = change
            # print(type(row))
            # print(row)
            idate = row[0]
#greatest decrease
        if (change < greatest_decrease):
            greatest_decrease = change
            ddate = row[0]

        # Add to the changes list
        revenue_changes.append(int(row[1]))

    # Set the Revenue average
    revenue_avg = sum(revenue_changes) / len(revenue_changes)



    print("Total Months: " , Months)
    print("Total Revenue: " + "$" , Total_Revenue)
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    print("Greatest Increase: " + idate + " $"+str(greatest_increase) +"\n")
    print("Greatest Decrease: " + ddate + " $"+str(greatest_decrease) +"\n")

    file_to_output = "PyBankAnswer.txt"
    with open(file_to_output, "w") as txt_file:
        txt_file.write("Total Months: ")
        txt_file.write(str(Months))
        txt_file.write("\n")
        txt_file.write("Total Revenue: ")
        txt_file.write(str(Total_Revenue))
        txt_file.write("\n")
        txt_file.write("Average Change: ")
        txt_file.write(str(round(sum(revenue_changes) / len(revenue_changes),2)))
        txt_file.write("\n")
        txt_file.write("Greatest Increase: ")
        txt_file.write(idate + " $"+str(greatest_increase))
        txt_file.write("\n")
        txt_file.write("Greatest Decrease: ")
        txt_file.write(ddate + " $"+str(greatest_decrease))

mon = 0
TR = 0
chan = 0
p = 0
gi = 0
gd = 9999999999999999999999
id = ""
dd = ""
revenue_chans = []
with open(filepaths) as csvfile:
    reader = csv.reader(csvfile)
    # for row in reader:
    #     print(row)
    next(reader,None)
    data = list(reader)
    mon = len(data)
    for row in data:
        cur_month = int(row[1])
        TR += int(row[1])
        #The average chan in revenue between mon over the entire period
        #chan = chan
        #PR = PR
        chan = int(row[1]) - p
        # print(chan)
        #date = int(row[0])
        # Reset the value of PR to the row I completed my analysis
        P = int(row[1])
        # print(PR)

        # #Determine the greatest increase
        if (chan > gi):
            gi = chan
            # print(type(row))
            # print(row)
            id = row[0]
#greatest decrease
        if (chan < gd):
            gd = chan
            dd = row[0]

        # Add to the chans list
        revenue_chans.append(int(row[1]))

    # Set the Revenue average
    revenue_avg = sum(revenue_chans) / len(revenue_chans)

    print("Total Months: " , mon)
    print("Total Revenue: " + "$" , TR)
    print("Average Change: " + "$" + str(round(sum(revenue_chans) / len(revenue_chans),2)))
    print("Greatest Increase: " + id + " $"+str(gi) +"\n")
    print("Greatest Decrease: " + dd + " $"+str(gd) +"\n")

    output = "PyBankAnswer2.txt"
    with open(output, "w") as txt_file:
        txt_file.write("Total Months: ")
        txt_file.write(str(mon))
        txt_file.write("\n")
        txt_file.write("Total Revenue: ")
        txt_file.write(str(TR))
        txt_file.write("\n")
        txt_file.write("Average Change: ")
        txt_file.write(str(round(sum(revenue_chans) / len(revenue_chans),2)))
        txt_file.write("\n")
        txt_file.write("Greatest Increase: ")
        txt_file.write(id + " $"+str(gi))
        txt_file.write("\n")
        txt_file.write("Greatest Decrease: ")
        txt_file.write(dd + " $"+str(gd))




            # Total_Revenue = Total_Revenue + int(row[1])
