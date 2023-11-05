import numpy as np
import pandas as pd
df = pd.read_csv('Price of Tomato Karnataka(2016-2018).csv');
df.groupby(df['Arrival Date'])
print(df.head(50))
    