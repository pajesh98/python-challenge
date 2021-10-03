import os
import csv



#Define the variables
total_number_of_months = 0
total = 0
Avg_changes = []
date_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_descrease = 0
greatest_descrease_month = 0

csvpath = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')

#Open the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    row = next(csvreader)
   
#Calculate the Net Amount and total number of months
    previous_row = int(row[1])
    total_number_of_months += 1
    total  += int(row[1])
    
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    #Read the rows after the header
    for row in csvreader:
        total_number_of_months += 1
        total  += int(row[1])
        


        changes = int(row[1]) - previous_row
        Avg_changes.append(changes)
        previous_row = int(row[1])
        date_count.append(row[0])


        #Calculate the greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        #Calculate the greatest descrease
        if int(row[1]) < greatest_descrease:
            greatest_descrease = int(row[1])
            greatest_descrease_month = row[0]
Average_Change = sum(Avg_changes) / len(Avg_changes)

print(f"Financial Analysis")
print(f"------------------------------------------------")
print(f"Total Months: {total_number_of_months}")
print(f"Total: ${total}")
print(f"Average Change:  ${Average_Change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month}   ({max(Avg_changes)})")
print(f"Greatest Decrease in Profits: {greatest_descrease_month} ({min(Avg_changes)})")


#Path of the output file.
output_file = os.path.join('.', 'PyBank',  'budget_data_revised.text')

#write the data to the textfile.
with open(output_file, 'w',) as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_number_of_months}\n")
    txtfile.write(f"Total: ${total}\n")
    txtfile.write(f"Average Change: ${Average_Change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${max(Avg_changes)})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_descrease_month}, (${min(Avg_changes)})\n")


    
        



        



