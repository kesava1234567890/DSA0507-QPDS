import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\leela\OneDrive\Desktop\QPDS\alphabet.csv")
start_date = pd.to_datetime('04-01-2020')
end_date = pd.to_datetime('05-01-2020')
df['date'] = pd.to_datetime(df['date'])
new_df = (df['date'] >= start_date) & (df['date'] <= end_date)
df1 = df.loc[new_df]
df2 = df1.set_index('date')
plt.figure(figsize=(10, 6))  
plt.suptitle('Stock Prices of Alphabet Inc.\n(April 1, 2020 - May 1, 2020)', fontsize=18, color='black')

plt.xlabel("Date", fontsize=16, color='black')
plt.ylabel("$ Price", fontsize=16, color='black')

df2['close'].plot(color='green')

plt.show()
