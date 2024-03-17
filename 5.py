import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/leela/OneDrive/Desktop/QPDS/alphabet.csv")
start_date=pd.to_datetime('04-01-2020')
end_date=pd.to_datetime('05-01-2020')
df['date']=pd.to_datetime(df['date'])
new_df=(df['date']>=start_date)&(df['date']<=end_date)
df1=df.loc[new_df]
df2=df1.set_index('date')
plt.figure(figsize=(6,6))
plt.suptitle('trading volume of alphabet inc. stock,\n 01-04-2020 to 01-05-2020',fontsize=16,color='black')
plt.xlabel("date",fontsize=12,color='black')
plt.ylabel("trading volume",fontsize=12,color='black')
df2['volume'].plot(kind='bar');
plt.show()
