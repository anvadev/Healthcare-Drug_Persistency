## Healthcare Persistency of a Drug
## Data Cleaning

"""
The script performs the following cleaning processes:
- Convert dataset into lowercase
- Convert categorical values into binary {'n' , 'y'}
- Save file as a .csv file


"""

# Libraries
import pandas as pd
import numpy as np

# Load Dataframe
df = pd.read_excel("Healthcare_dataset.xlsx", sheet_name= 'Dataset')



# Convert Dataset into lowercase
df_lower = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
df_lower.columns = df_lower.columns.str.lower()


# Convert Categorical values into binary {'n' , 'y'}
for column in df_lower.columns:
    if set(df[column].unique()) == {'n','y'}:
        df[column] = df[column].replace({'n' : 0 , 'y' : 1})


# Save the loaded sheet as a .csv file
df.to_csv('output_file.csv', index=False)





