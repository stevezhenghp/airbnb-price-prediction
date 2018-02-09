# Load required libraries and datasets

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#change this based on where your input data is stored
path = ""
df=pd.read_csv(path+'/train.csv')
df.head()
df.shape
df.info()
for col in df:
    if(df[col].isnull().any()):
        print(col)
df=df.fillna(0)
df['host_response_rate'].head()
