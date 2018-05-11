import os
import csv
# csvpath = "os.path.join('..','PyBank','raw_data','budget_data_1.csv')
#filepath = "C:\\Users\\Anish Tendolkar\\datasciencebootcamp\\python_challenge\\Zip\\PyBank\\raw_data\\budget_data_1.csv"
#filepath = "C:\\Users\\Anish Tendolkar\\datasciencebootcamp\\python_challenge\\Zip\\PyBank\\raw_data\\budget_data_1.csv"
#IF YOU UNCOMMENT THE LINE ABOVE THE DATA BELOW WILL RUN THROUGH BOTH THE CSV FILES AND RETURN NUMBERS BASED ON BOTH THE CSV FILES.
#txtpath = os.path.join("Zip","PyParagraph","raw_data","paragraph_1.txt")
#filepath = os.path.join("Zip","PyBank","raw_data","budget_data_1.csv")
filepaths = os.path.join("Zip","PyBank","raw_data","budget_data_2.csv")
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
