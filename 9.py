import pandas as pd
import numpy as np
df=pd.read_excel(r"C:/Users/leela/OneDrive/Desktop/QPDS/sales-data.xlsx")
print(pd.pivot_table(df,index=["Region","Manager","SalesMan"],values="Sale_amt",aggfunc=np.sum))
