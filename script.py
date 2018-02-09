# Load required libraries and datasets

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#change this based on where your input data is stored
path = ""
df=pd.read_csv(path+'/train.csv')

#prints out first 5 rows of data
df.head()

#prints out aggregate stats of data
df.shape
df.info()

#finds columns that have missing data
for col in df:
    if(df[col].isnull().any()):
        print(col)
        
#fills missing data with "O" value
df=df.fillna(0)

#prints first 5 rows of a column with missing to check that the missing has been filled
df['host_response_rate'].head()
