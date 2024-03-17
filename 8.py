import pandas as pd
import numpy as np
df = pd.read_excel("C:/Users/leela/OneDrive/Desktop/QPDS/sales-data.xlsx")
pivot_table = pd.pivot_table(df, index=["Item"], values="Units", aggfunc=np.sum)
print(pivot_table)
