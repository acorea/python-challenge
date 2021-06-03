#!/usr/bin/env python
# coding: utf-8

# In[16]:


#import csv
import os
import csv


# In[9]:


#Start month count at 0
total_months = 0


# In[10]:


#path to find budget csv
csvpath = os.path.join(".", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile)

    # Read the header row first 
    csvheader = next(csvfile)
    
       


# In[11]:


# Create new list
months_list = []
profits_list = []
change_profits_list = []


# In[22]:


# Loop to append to profits / months list and to total profits / months 
    for row in csvreader:
        profits_list.append(int(row[1]))
        months_list.append(row[0])
        Total_Profits = [sum(profits_list)]
        Total_Months += 1
            
      


# In[20]:


# Loop to calculate change in profits
   for i in range(1, Total_Months):
       change = profits_list[i] - profits_list[i-1]
       change_profits_list.append(change)


# In[21]:


# Variables to calcuate average change in profits          
    Total_change = sum(change_profits_list)
    Number_Change = len(change_profits_list)
    Average_change = "${:,.2f}".format(Total_change/Number_Change)


# In[ ]:


#calculate the min and max changes in profit


# In[ ]:


#calculate the month with the max profit change


# In[ ]:


#calculate the month with the min profit change


# In[ ]:


#Terminal Print 
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {Total_Months}")
    print(f"Total: {Total_Profits}")
    print(f"Average Change: {Average_change}")
    print(f"Greatest Increase in Profits: {max_month} {max_change_profit}")
    print(f"Greatest Decrease in Profits: {min_month} {min_change_profit}")


# In[ ]:


#Output Analysis to text file
    Text_File = open("PyBank.txt","w")
    Text_File.write(f'Financial Analysis\n')
    Text_File.write(f'-----------------------------\n')
    Text_File.write(f'Total Months: {Total_Months}\n')
    Text_File.write(f'Total: {Total_Profits}\n')
    Text_File.write(f'Average Change: {Average_change}\n')
    Text_File.write(f'Greatest Increase in Profits: {max_month} {max_change_profit}\n')
    Text_File.write(f'Greatest Decrease in Profits: {min_month} {min_change_profit}')
    Text_File.close()

