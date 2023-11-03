## Healthcare Persistency of a Drug
## Data Cleaning

"""
The script performs the following cleaning processes:
- IMPUTER v.1.0.0
- Convert dataset into lowercase
- Convert categorical values into binary {'n' , 'y'}
- Save file as a .csv file

"""

# Libraries
import pandas as pd
import numpy as np

# Load Dataframe
df = pd.read_excel("Healthcare_dataset.xlsx", sheet_name= 'Dataset')


###############################################################################################################################################################
# IMPUTER   v.1.0.0

"""
Theshold ::: < 10 %
Values ::: "Unknown" | "Others" | "Other/Unknown"

The script will extract the count of "Unknown", "Others", "Other/Unknown" and create a
Dataframe of all of the columns in the df that contain the values specified, and calculate
the percentage of those values. 

Any of the columns whose count is less than 10% will be imputed by the mode.

"""

# Create a dataframe to store the columns with counts of unknowns
unknown_value = pd.DataFrame()

# Finds "Unknown" and "Other" values and counts them, then gets stored in the dataframe
for column in df:
    if any((df[column] == 'Unknown')):
        unknown_value[column] = (df[column] == 'Unknown' ).value_counts()
        
    elif any((df[column] == 'Other/Unknown')):
        unknown_value[column] = (df[column] == 'Other/Unknown' ).value_counts() 
    
    elif any((df[column] == 'Others')):
        unknown_value[column] = (df[column] == 'Others' ).value_counts() 



# Removes the index label
unknown_value.index.name = None

# Transpose the dataframe
unknown_value = unknown_value.T

# Converts the columns as str
unknown_value.columns = unknown_value.columns.astype(str)

# Rename the columns
unknown_value = unknown_value.rename(columns={'True': 'Unknown_Others', 'False': 'Categorized'})

# Unknown/Others percentage
unknown_value['Pct_of_Unknown_Other'] = (100 * (unknown_value['Unknown_Others'] / (unknown_value['Categorized'] + unknown_value['Unknown_Others']))).round(2)


def mode_imputer(): 

    """
    This script will impute the column values categorized as "Unknown".

    It will iterate through the unknown_value dataframe and save the 
    indexes in the list variable and then will iterate through the 
    df and impute each element in the list.
    """ ;

    columns_to_impute = []
    for column_name, pct in unknown_value['Pct_of_Unknown_Other'].items():
        if pct < 10:
            columns_to_impute.append(column_name)


    for column in columns_to_impute:
        mode_value = df[column].mode()[0]
        df[column] = df[column].replace({'Unknown': mode_value, 'Others': mode_value, 'Other/Unknown': mode_value})

    return df

mode_imputer()
###############################################################################################################################################################

###################################################################
# LOWERCASE

# Convert Dataset into lowercase
df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
df.columns = df.columns.str.lower()
##################################################################

#############################################################
# BINARY VALUE CONVERSION

# Convert Categorical values into binary {'n' , 'y'}
for column in df.columns:
    if set(df[column].unique()) == {'n','y'}:
        df[column] = df[column].replace({'n' : 0 , 'y' : 1})
#############################################################


###########################################
# SAVE FILE

# Save the loaded sheet as a .csv file
df.to_csv('healthcare_data_cleaned.csv', index=False)
###########################################







##### END OF SCRIPT #######