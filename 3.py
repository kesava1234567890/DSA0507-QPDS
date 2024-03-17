import pandas as pd
emp=pd.read_csv("C:/Users/leela/OneDrive/Desktop/QPDS/job title.csv")
print("JOB ID    JOB TITLE    min_salary    max_salary")
res=emp.sort_values('JOB_TITLE')
for index, row in res.iterrows():
    print(row['JOB_ID'].ljust(15),row['JOB_TITLE'].ljust(35),str(row['MIN_SALARY']).ljust(9),row['MAX_SALARY'])
