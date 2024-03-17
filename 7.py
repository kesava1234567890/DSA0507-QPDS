import pandas as pd
import numpy as np
df=pd.read_excel("C:/Users/leela/OneDrive/Desktop/QPDS/sales-data.xlsx")
table=pd.pivot_table(df,index='Item',values='Sale_amt',aggfunc=[np.max,np.min])
print(table)
