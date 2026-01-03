# In the first commit we will see how to load and view data set
import pandas as pd 

#Loading the CSV File
data= pd.read_csv('data/sample.csv')
print(data['name'])   


## STEP 2: Standardizing column names
data.columns=(data.columns
              .str.strip()              # remove extra spaces
              .str.lower()              # avoids case bugs
              .str.replace(' ', '_'))   # Python- friendly names
print(data) 


## STEP 3: Strip whitespace in string columns
string_columns= data.select_dtypes(include=['object','string']).columns
for col in string_columns:
    data[col]= (data[col]
                .astype('string')
                .str.strip()
                .str.replace(r'\s+',' ',regex=True))     #Step_4_Part1: changing multiple whitespaces in between strings to only 1       
    # its important to choose astype(str) even if the column is string because NaN(empty cell) is type float.
    # if we dont convert it for now the called function gives error. #astype('string'), keeps NaN as Nan instead
    # of converting it to string and manages not giving an error.


## STEP 4: Convert empty spaces to NA
data= data.replace(r'^\s*$',pd.NA,regex=True)           #Step_4_Part1: replacing empty values with NA

## STEP 5: Normalise Gender values and City names:
# Normalise Gender values
data['gender']=(
    data['gender']
    .str.upper()
    .replace({'M': 'Male', 'F': 'Female'})
)
data['city']= (
    data['city']
    .str.replace('"','', regex=False)
    .str.title()
)      # title() standardise city names


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


                

## STEP 1: Basic Inspection
print('Shape:',data.shape)              # prints number of rows and columns
print('\nColumns: ',data.columns)       # print only number of columns 

print('\nFirst 5 rows:')
print(data.head())

print('\nPrint DataFrame Info:')
print(data.info())                      # Important for inspection, displays null values data as well.

print('\nStatistical Summary:')         # Different statistics measures for every columns
print(data.describe(include='all'))
