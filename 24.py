import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("C:/Users/leela/OneDrive/Desktop/QPDS/fdata.csv",sep=',',parse_dates=True,index_col=0)
df.plot()
plt.show()
