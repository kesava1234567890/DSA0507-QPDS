import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/leela/OneDrive/Desktop/QPDS/alphabet.csv")
start_date=pd.to_datetime('04-01-2020')
end_date=pd.to_datetime('05-01-2020')
df['date']=pd.to_datetime(df['date'])
new_df=(df['date']>=start_date)&(df['date']<=end_date)
df1=df.loc[new_df]
df2=df1.set_index('date')
x=['close'];y=['volume']
plt.figure(figsize=[15,10])
df2.plot.scatter(x,y,s=50);
plt.grid(True)
plt.title('trading volume /price of alphabet inc. stock ,\n01-04-2020 to 01-05-2020',fontsize=14,color='black')
plt.xlabel("stock price",fontsize=12,color='black')
plt.ylabel("trading volume",fontsize=12,color='black')
plt.show()
