# In the first commit we will see how to load and view data set
import pandas as pd 

#Loading the CSV File
data= pd.read_csv('data/sample.csv')
print(data) 

# .to_string() forces panda to print entire DataFrame, Useful for smaller datasets.
# For larger datasets this method can flood your teminal, be slow and unreadable.
# Use Carefully
print(data.to_string())
# or
pd.set_option('display.max_columns', None) # removes restrictions for columns and display all columns.
pd.set_option('display.max_rows', None)    # removes restrictions for rows and displan all rows.
print(data)                        

# restrict the rows display to specific amount
# Everytime you print data only 8 rows will be shown unless this configuration is changed
pd.options.display.max_rows= 8
print('\nNumber of rows default display setting is:',pd.options.display.max_rows)       
# resetting to default value which is 60
pd.reset_option('display.max_rows')


                

# Basic Inspection
print('Shape:',data.shape)              # prints number of rows and columns
print('\nColumns: ',data.columns)       # print only number of columns 

print('\nFirst 5 rows:')
print(data.head())

print('\nPrint DataFrame Info:')
print(data.info())                      # Important for inspection, displays null values data as well.

print('\nStatistical Summary:')         # Different statistics measures for every columns
print(data.describe(include='all'))
